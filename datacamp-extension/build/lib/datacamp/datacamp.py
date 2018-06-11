from docutils import nodes
from docutils.parsers.rst import directives
try:
    from sphinx.util.compat import Directive
except ImportError:
    from docutils.parsers.rst import Directive

"""
UNDER CONSTRUCTION:
	Todo: -Various options that datacamp offers. -Enable Latex add on.
"""

class datacamp(nodes.General, nodes.Element):
	pass

def html_visit_datacamp_node(self, node):
	language = node['lang']
	libraries = node['library']
	code = node['code']
	
	if language.lower() == 'r':
		self.body.append('<div data-datacamp-exercise data-lang="r">')
		if libraries:
			self.body.append('<code data-type="pre-exercise-code">')
			for library in libraries:
				self.body.append('library('+library+')')
			self.body.append('</code>')
		self.body.append('<code data-type="sample-code">')
		self.body.append(code)
		self.body.append('</code>')
		self.body.append('</div>')
	else:
		self.body.append('<div data-datacamp-exercise data-lang="python">')
		if libraries:
			self.body.append('<code data-type="pre-exercise-code">')
			for library in libraries:
				self.body.append('import ' + library)
			self.body.append('</code>')
		self.body.append('<code data-type="sample-code">')
		self.body.append(code)
		self.body.append('</code>')
		self.body.append('</div>')

def html_depart_datacamp_node(self, node):
	pass

def tex_visit_datacamp_node(self, node):
	pass

def tex_depart_datacamp_node(self, node):
	pass

class DatacampDirective(Directive):
	has_content = True
	option_spec = {
		"lang": directives.unchanged,
		"library": directives.unchanged,
		"solution": directives.unchanged
	}

	def run(self):
		lang = 'r'
		library = []
		
		if 'lang' in self.options:
			lang = self.options.get('lang')
		if 'library' in self.options:
			library = self.options.get('library').split(', ')
		code = '\n'.join(self.content)
		
		node = datacamp()
		node['lang'] = lang
		node['library'] = library
		node['code'] = code

		return [node]

def builder_inited(app):
	datapath = app.config.datacamp_path
	if not datapath:
		raise ExtensionError('datacamp_path config value must be set for the '
			'datacamp extension to work')
	if datapath:
		app.add_javascript(datapath)

def setup(app):
	app.add_node(datacamp, 
		html=(html_visit_datacamp_node, html_depart_datacamp_node), 
		latex=(tex_visit_datacamp_node, tex_depart_datacamp_node))

	app.add_config_value('datacamp_path', None, False)
	app.add_directive('datacamp', DatacampDirective)
	app.add_stylesheet('css/datacamp-custom.css')

	app.connect('builder-inited', builder_inited)
