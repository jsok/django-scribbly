from django import template

register = template.Library()

def get_item(dictionary, key):
    return dictionary.get(key)
register.filter("dict_lookup", get_item)

@register.tag
def nav_is_active(parser, token):
    import re
    args = token.split_contents()
    template_tag = args[0]
    if len(args) < 2:
        raise template.TemplateSyntaxError, "%r tag requires at least one argument" % template_tag
    return NavSelectedNode(args[1:])


class NavSelectedNode(template.Node):
    def __init__(self, patterns):
        self.patterns = patterns

    def render(self, context):
        path = context['request'].path
        for p in self.patterns:
            pValue = template.Variable(p).resolve(context)
            if path == pValue:
                return "active"
        return ""

