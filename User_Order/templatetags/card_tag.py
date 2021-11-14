from django import template
from User_Order.models import Oreder


register = template.Library()

@register.filter
def cart_total(user):
    order = Oreder.objects.filter(user=user, ordered=False)
    if order.exists():
        return order[0].orderitems.count()
    else:
        return 0

