from django import template
register = template.Library()

@register.filter
def keyvalue(dictionary, key):
    return dictionary[key]

register.filter("keyvalue", keyvalue)

@register.filter
def typevalue(value):
    return type(value)

register.filter("typevalue", typevalue)