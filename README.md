# library_template
A structure that can be a starting point for developers who want to create projects that depend on OpenMDAO.

This is the simplest working repository. 

This sample repo is fully installable using:
`pip install -e .`

**NOTE**: *You can create the docs from scratch by changing into `your_project` and typing: 
`jupyter-book create docs/`. We have already done this for you.*

Then build using `jupyter-book build docs/`

Inside of `/test` we have added a dir with two files to test your notebooks and enforce some rules 
we have in our style guide which can be found in our docs repo 
[here](https://github.com/OpenMDAO/OpenMDAO_Book/tree/main/openmdao_book/other_useful_docs/developer_docs/doc_style_guide.ipynb). 
These tests will run with run with `testflo`. Reference 
[our repo workflow](https://github.com/OpenMDAO/OpenMDAO_Book/tree/main/.github/workflows) if you 
would like to set up GitHub Actions.

Use this working example to build your own repository!

Find a more detailed explanation of how to get this all working at:
http://openmdao.org/twodocs/other/repo_guide/index.html