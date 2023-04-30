import re
import uuid
import os

from mistletoe.html_renderer import HTMLRenderer
from mistletoe.latex_renderer import LaTeXRenderer
from mistletoe import block_token
from mistletoe import span_token

CWD = os.path.abspath(os.path.dirname(__file__))

class SpfRenderer(HTMLRenderer, LaTeXRenderer):
    """
    MRO will first look for render functions under HTMLRenderer,
    then LaTeXRenderer.
    """
    mathjax_src = '<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-MML-AM_CHTML"></script>\n'

    def __init__(self, depth=5, omit_title=True, filter_conds=[], *extras):
        super().__init__(*extras)
        self._headings = []
        self.depth = depth
        self.omit_title = omit_title
        self.filter_conds = filter_conds
        self.numbering = [0]
        with open(os.path.join(CWD,"white_clean.css"), "r") as f:
            self.style = f.read()
        with open(os.path.join(CWD,"button.js"), "r") as f:
            self.js = f.read()
        

    @property
    def toc(self):
        """
        Returns table of contents as a block_token.List instance.
        """
        def get_indent(level):
            if self.omit_title:
                level -= 1
            return ' ' * 4 * (level - 1)

        def build_list_item(heading):
            level, content = heading
            template = '{indent}- {content}\n'
            return template.format(indent=get_indent(level), content=content)

        lines = [build_list_item(heading) for heading in self._headings]
        items = block_token.tokenize(lines)
        return items[0]


    def render_heading(self, token):
        """
        Overrides super().render_heading; stores rendered heading first,
        then returns it.
        """
        template = '<h{level}>{inner}</h{level}>'
        inner = self.render_inner(token)
        rendered = template.format(level=token.level, inner=inner)
    
        content = self.parse_rendered_heading(rendered)

        s_details = " "
        e_details = " "
        
        if not (self.omit_title and token.level == 1
                or token.level > self.depth
                or any(cond(content) for cond in self.filter_conds)):
            self._headings.append((token.level, content))
        if token.level >= 2:
            if len(self.numbering) > token.level-1:
                while len(self.numbering)> token.level-1:
                    self.numbering.pop()
                    s_details += "</details>"
            if len(self.numbering) == token.level-1:
                self.numbering[token.level-2]+= 1
            else:
                s_details ="<details><summary></summary>"
                self.numbering.append(1)

        if token.level != 1:
            numbered_template = s_details+'<br /><h{level}><strong,id={numbering}>{numbering}.</strong> {inner}</h{level}>'+e_details
            return numbered_template.format(numbering=".".join([str(n) for n in self.numbering]), level=token.level, inner=inner)

        else:
            return rendered
    @staticmethod
    def parse_rendered_heading(rendered):
        """
        Helper method; converts rendered heading to plain text.
        """
        return re.sub(r'<.+?>', '', rendered)
    

    def render_math(self, token):
        """
        Ensure Math tokens are all enclosed in two dollar signs.
        """
        if token.content.startswith('$$'):
            return self.render_raw_text(token)
        return '\({}\)'.format(self.render_raw_text(token)[1:-1])
    

    @staticmethod
    def render_line_break(token: span_token.LineBreak) -> str:
        return '\n' if token.soft else '<br />\n'
    
    def render_document(self, token):
        """
        Append CDN link for MathJax to the end of <body>.
        """
        head = "<head>"+self.style+"</head>"
        
        text = head+self.js+super().render_document(token)
        text, correspondances = self.parse_labels(text)
        text = self.parse_refs(text, correspondances)
        return text + "</details>" + self.mathjax_src 

    def parse_labels(self, text):
        new_text = ""
        correspondances = {}
        for sentence in text.split('\n'):
            if "\slabel" in sentence:
                label = re.findall(r"(\\slabel{)(.*?)\}", sentence)[0][1]
                numbering = re.findall(r"<strong,id=(.*?)>", sentence)[0]
                correspondances[label]=numbering
        
        text = re.sub(r"(\\slabel{)(.*?)\}" ,r'<a id="\2"></a>', text)
        return text, correspondances
    
    def parse_refs(self, text, correspondances):
        def make_ref(match_obj):
            label = match_obj.group(2)
            return '<a href="#'+label+'">'+correspondances[label]+'</a>'
        text = re.sub(r"(\\sref{)(.*?)\}", make_ref, text)
        return text
