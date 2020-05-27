from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.errors import ExtensionError
try:
    from sphinx.util.compat import Directive
except ImportError:
    from docutils.parsers.rst import Directive

"""
Datacamp extension:

Constructs datacamp nodes while reading through the .rst documents.
"""

class datacamp(nodes.General, nodes.Element):
	pass

def latex_visit_datacamp_node(self, node):
	self.body.append('$$\\text{Sjá heimasíðu bókarinnar á edbook.hi.is til að leika ykkur með R kóðann}$$')

def latex_depart_datacamp_node(self, node):
	pass

def html_visit_datacamp_node(self, node):
	"""
	Construction of html elements while traversing through already created nodes and
	making adjustments accordingly
	"""
	language = node['lang'].lower()
	if node['height']:
		self.body.append('<div data-datacamp-exercise data-lang="'+language+'" data-height="'+node['height']+'">')
	else:
		self.body.append('<div data-datacamp-exercise data-lang="'+language+'" data-height="auto">')
	if node['library']:
		self.body.append('<code data-type="pre-exercise-code">')
		if language == 'python':
			for lib in node['library']:
				self.body.append('import ' + lib)
		else:
			for lib in node['library']:
				self.body.append('library('+lib+')')
		self.body.append('</code>')

	self.body.append('<code data-type="sample-code">')
	self.body.append(node['code'])
	self.body.append('</code>')
	self.body.append('</div>')


def html_depart_datacamp_node(self, node):
	pass


class DatacampDirective(Directive):
	has_content = True
	option_spec = {
		"lang": directives.unchanged,
		"library": directives.unchanged,
		"height": directives.unchanged
	}

	def run(self):
		env = self.state.document.settings.env

		lang = 'r'
		library = []
		height = None
		code = '\n'.join(self.content)
		
		if 'lang' in self.options:
			lang = self.options.get('lang')
		if 'library' in self.options:
			library = self.options.get('library').split(', ')
		if 'height' in self.options:
			height = self.options.get('height')
			
		node = datacamp()
		node['lang'] = lang
		node['library'] = library
		node['height'] = height
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
		latex = (latex_visit_datacamp_node, latex_depart_datacamp_node))
	app.add_config_value('datacamp_path', None, False)
	app.add_directive('datacamp', DatacampDirective)
	app.add_stylesheet('css/datacamp-custom.css')

	app.connect('builder-inited', builder_inited)