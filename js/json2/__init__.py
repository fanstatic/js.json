from fanstatic import Library, Resource
from js.jquery import jquery

library = Library('jquery_json2', 'resources')

# Define the resources in the library like this.
# For options and examples, see the fanstatic documentation.
# resource1 = Resource(library, 'style.css')

jquery_json2 = Resource(library, 'json2.js', depends=[jquery])
