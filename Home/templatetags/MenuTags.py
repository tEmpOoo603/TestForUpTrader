from django import template
import Home.views as views
from Home.models import MenuItem, Menu

register = template.Library()

@register.filter('draw_menu')
def  draw_menu(menu_name):
    menu = Menu.objects.get(name=menu_name)
    menu_items = MenuItem.objects.filter(menu=menu)
    return menu_items