Read the Docs Light-Dark Theme
------------------------------

A clean variant of the [read the docs theme](https://github.com/readthedocs/sphinx_rtd_theme)
with grayscale styling and optional light mode / dark mode toggling.
This theme is currently used with the [proplot](https://github.com/lukelbd/proplot.git)
and [climopy](https://github.com/lukelbd/climopy.git) projects.
Please refer to the published [proplot](https://proplot.readthedocs.io)
and [climopy](https://climopy.readthedocs.io) documentation for
demonstrations of the theme.

Theme Usage
-----------

In your `conf.py` file, add the entry ``'sphinx_rtd_light_dark'`` to the `extensions` list,
and set the variable `html_theme` to ``'sphinx_rtd_light_dark'``. Example `conf.py`:

```python
extensions = [
  ...
  'sphinx_rtd_light_dark',
  ...
]
html_theme = 'sphinx_rtd_light_dark'
```
