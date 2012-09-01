from django import template

register = template.Library()

@register.filter
def dict_lookup(dictionary, key):
    return dictionary.get(key)

@register.tag
def nav_get_active_class(parser, token):
    import re
    args = token.split_contents()
    template_tag = args[0]
    if len(args) < 1:
        raise template.TemplateSyntaxError, "%r tag requires at least one argument" % template_tag
    return NavSelectedNode(args[1])

class NavSelectedNode(template.Node):
    def __init__(self, url):
        self.url = url

    def render(self, context):
        path = context['request'].path
        pValue = template.Variable(self.url).resolve(context)
        if path.startswith(pValue):
            return "active"
        else:
            return ""

