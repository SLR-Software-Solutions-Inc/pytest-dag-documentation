project = "pytest-dag"
author = "SLR Software Solutions Inc."
copyright = "2026, SLR Software Solutions Inc."

extensions = [
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_title = "pytest-dag documentation"
html_static_path = ["_static"]

# MyST markdown support
myst_enable_extensions = [
    "deflist",
    "fieldlist",
]

# RTD-style left nav depth / behavior
html_theme_options = {
    "navigation_depth": 4,
    "collapse_navigation": False,
    "sticky_navigation": True,
    "titles_only": False,
}
