'''
Use sphinx's extension "apidoc" to generate the documentation.

Step on the folder '2-documenting'.

Uncomment from the conf.py file:
    import os
    import sys
    sys.path.insert(0, os.path.abspath('..'))

Add extensions to conf.py:
    extensions = [
                'sphinx.ext.autodoc',
                'sphinx.ext.viewcode'
                ]

Run:
    '$ sphinx-apidoc -o docs source'

    -o : output
        docs folder

    source : package I want to generate documentation for

Go to /docs and run:
    '$ make clean html'

'''
pass