from django import template
register = template.Library()

def product_title(value):
    return value[0:50]+'  ....'


register.filter('product_title', product_title)





