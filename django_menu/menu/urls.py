from django.urls import path
from . import views
from django.conf.urls import url

app_name='menu'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^submenu_1/$', views.Submenu1View.as_view(), name='submenu_1'),
    url(r'^submenu_2/$', views.Submenu2View.as_view(), name='submenu_2'),
    url(r'^submenu_3/$', views.Submenu3View.as_view(), name='submenu_3'),
    url(r'^submenu_4/$', views.Submenu4View.as_view(), name='submenu_4'),
    url(r'^submenu_1/option_1/$', views.Option1View.as_view(), name='option_1'),
    url(r'^submenu_1/option_2/$', views.Option2View.as_view(), name='option_2'),
]
