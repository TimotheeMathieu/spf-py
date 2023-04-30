import click
from spf_py.renderer import SpfRenderer
from mistletoe import Document


    
@click.command()
@click.argument('filename')
def cli(filename):
    """Example script."""
    with open(filename, 'r') as fin:
        with SpfRenderer() as renderer:     
            doc = Document(fin)
            rendered = renderer.render(doc) 
    print(rendered)
