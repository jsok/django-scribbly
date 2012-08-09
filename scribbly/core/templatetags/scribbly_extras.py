from django.template import Library

register = Library()

def get_item(dictionary, key):
    return dictionary.get(key)
register.filter("dict_lookup", get_item)
