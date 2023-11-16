from django import template
from django.urls import reverse

import Home.views as views
from Home.models import MenuItem, Menu

register = template.Library()

# @register.filter('draw_menu')
# def  draw_menu(menu_name):
#     descendants = Menu.objects.get(name=menu_name)
#     menu_items = descendants.child_items.all()
#     return menu_items

@register.filter('draw_menu')
def draw_menu(menu_name):
    menu = Menu.objects.get(name=menu_name)
    menu_items = MenuItem.objects.filter(menu=menu)
    for i in menu_items:
        if i.parent_id is not None:
            i.url = menu_items.get(pk=i.parent_id).url + '/' + i.url
    return menu_items