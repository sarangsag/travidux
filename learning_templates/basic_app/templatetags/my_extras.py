from django import template

register=template.Library()
@register.filter(name="cut")
def cut(value,arg):
    """
    this cuts all the values of "argg" from the string

    """
    return value.replace(arg,'')

# register.filter('cut',cut)
