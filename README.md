# spf -- Structured proofs
This program is a parser to make structured proof in html using markdown syntax.

According to its inventor, structured proof are "A method of writing proofs is described that makes it harder to prove things
that are not true. The method, based on hierarchical structuring, is simple and practical." 
The method was first described by Leslie Lamport in his article [How to Write a Proof](https://lamport.azurewebsites.net/pubs/lamport-how-to-write.pdf). This article has a sequel [How to Write a 21st Century Proof](https://lamport.azurewebsites.net/pubs/proof.pdf) with more ideas on the same theme.

This repository proposes one way to construct structured proofs writen in markdown and rendered as html. 
I do not exactly follow Lamport's way of doing structured proof and this repository is hacky at best. Use at your own discretion. For example look [here](https://timotheemathieu.github.io/assets/np.html) for a proof of Neyman-Pearson's Lemma done using `spf_py`.


## Install

To install this package, use pip:
```bash
pip install git+https://github.com/TimotheeMathieu/spf-py
```

## Examples

I included some examples in the `examples` folder. 

## Usage


- The first level of header "#" is the title of the document, The headers "##" to "#####" are transformed to steps.
- I implemented a small label/reference scheme. The anchor is done using `\slabel{keyword}` in a line containing a step (i.e. the line must begin by "##" or "###" or...) and the reference `\sref{keyword}` will render as an hyper-ref with name the number of the step referenced.

