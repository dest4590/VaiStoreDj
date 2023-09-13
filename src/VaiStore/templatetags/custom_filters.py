from django import template

register = template.Library()

@register.filter
def split_by_whitespace(value):
    return value.split('\n')