import os
import jaxoplanet

html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")
if os.environ.get("READTHEDOCS", "") == "True":
    html_context = {"READTHEDOCS": True}

language = "en"
master_doc = "index"

extensions = [
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_design",
    "myst_nb",
    "IPython.sphinxext.ipython_console_highlighting",
]

myst_enable_extensions = ["dollarmath", "colon_fence"]
source_suffix = {
    ".rst": "restructuredtext",
    ".ipynb": "myst-nb",
}
templates_path = ["_templates"]

# General information about the project.
project = "jaxoplanet-case-studies"
copyright = "2025 Simons Foundation, Inc."

exclude_patterns = ["_build"]
html_theme = "sphinx_book_theme"
html_title = "jaxoplanet case studies"
html_logo = "_static/logo.png"
html_favicon = "_static/favicon.png"
html_static_path = ["_static"]
html_show_sourcelink = False
html_theme_options = {
    "path_to_docs": "docs",
    "repository_url": "https://github.com/lgrcia/jaxoplanet-case-studies",
    "repository_branch": "main",
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "notebook_interface": "jupyterlab",
        "colab_url": "https://colab.research.google.com/",
    },
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
    "use_download_button": True,
    "use_sidenotes": True,
}
nb_execution_mode = "cache"
nb_execution_excludepatterns = []
nb_execution_timeout = -1
