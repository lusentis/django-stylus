from django import template

from stylus.compiler import Compiler

register = template.Library()

@register.tag(name='stylus')
def stylus(parser, token):
    try:
        tokens = token.split_contents()
        tag_name, files = tokens[0], tokens[1:]
    except IndexError:
        raise template.TemplateSyntaxError, "%s tag requires at least one filename." % tag_name
    return StylusNode(files)


class StylusNode(template.Node):
    def __init__(self, files):
        self.compiler = Compiler(files)
    
    def render(self, context):
        return self.compiler.compile()
