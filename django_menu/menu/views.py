from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Menu

class IndexView(generic.ListView):
    template_name = 'menu/index.html'
    context_object_name = 'latest_menu_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Menu.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class Submenu1View(generic.ListView):
    template_name = 'menu/submenu_1.html'
    context_object_name = 'latest_menu_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Menu.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class Submenu2View(generic.ListView):
    template_name = 'menu/submenu_2.html'
    context_object_name = 'latest_menu_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Menu.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class Submenu3View(generic.ListView):
    template_name = 'menu/submenu_3.html'
    context_object_name = 'latest_menu_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Menu.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class Submenu4View(generic.ListView):
    template_name = 'menu/submenu_4.html'
    context_object_name = 'latest_menu_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Menu.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class Option1View(generic.ListView):
    template_name = 'menu/option_1.html'
    context_object_name = 'latest_menu_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Menu.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class Option2View(generic.ListView):
    template_name = 'menu/option_2.html'
    context_object_name = 'latest_menu_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Menu.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]