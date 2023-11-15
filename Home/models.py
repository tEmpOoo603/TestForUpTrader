from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название меню', unique=True)

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='child_items')
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=256)

