# Create local pygments copies for custom.js usage
# WARNING: Must update these files whenever static/custom.js changes
# from pygments.styles import get_all_styles
import os
from pygments.formatters import HtmlFormatter
base = os.path.join('static', 'pygments')
if not os.path.isdir(base):
    os.mkdir(base)
for style in ('pastie', 'monokai'):  # or get_all_styles()
    file = os.path.join(base, style + '.css')
    if os.path.isfile(file):
        continue
    with open(file, 'w') as f:
        f.write(HtmlFormatter(style=style).get_style_defs('.highlight'))
