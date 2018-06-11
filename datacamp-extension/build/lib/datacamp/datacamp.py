from docutils import nodes
try:
    from sphinx.util.compat import Directive
except ImportError:
    from docutils.parsers.rst import Directive

class datacamp(nodes.General, nodes.Element):
	pass

def html_visit_datacamp_node(self, node):
	pass

def html_depart_datacamp_node(self, node):
	pass

def tex_visit_datacamp_node(self, node):
	pass

def tex_depart_datacamp_node(self, node):
	pass

class DatacampDirective(Directive):
	has_content = True
	option_spec = {
        "codefile": directives.unchanged,
        "lang": directives.unchanged
    }

    def run(self):
    	node = datacamp()
    	node['asdf'] = 'fdsa'

    	return [node]

def setup(app):
	app.add_node(datacamp, 
		html=(html_visit_datacamp_node, html_depart_datacamp_node), 
		latex=(tex_visit_datacamp_node, tex_depart_datacamp_node))
	app.add_directive('datacamp', DatacampDirective)
