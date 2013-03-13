from fanstatic import Library, Resource
from fanstatic.core import render_js

library = Library('json2', 'resources')

def earlier_than_ie8(url):
    """Native JSON support was introduced in IE8."""
    return '<!--[if lt IE 8]>%s<![endif]-->' % render_js(url)

json2 = Resource(library, 'json2.js', renderer=earlier_than_ie8)
