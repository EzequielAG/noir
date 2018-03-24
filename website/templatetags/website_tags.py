from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def add_to_querystring(context, *args, **kwargs):
    "Agrega los valores al querystring reemplazando las claves"
    querystring = context['request'].GET.copy()
    for k, v in kwargs.items():
        querystring[k] = v
    return querystring.urlencode()
