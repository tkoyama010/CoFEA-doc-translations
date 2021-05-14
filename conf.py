# BASEDIR is set by <lang>/conf.py
"""
Use "-D language=<LANG>" option to build a localized CoFEA document.
For example::

    sphinx-build -D language=ja -b html . _build/html

This conf.py do:

- Specify `locale_dirs` and `gettext_compact`.
- Overrides source directory as 'CoFEA/docs/`.

"""
import os
from sphinx.util.pycompat import execfile_
import shutil
import sys

shutil.copytree("CoFEA/docs/benchmarks", "benchmarks")
BASEDIR = os.path.dirname(os.path.abspath(__file__))

execfile_(os.path.join(BASEDIR, "CoFEA/docs/conf.py"), globals())

locale_dirs = [os.path.join(BASEDIR, "locale/")]
gettext_compact = False

sys.path.insert(0, os.path.abspath("CoFEA/meshpresso"))
