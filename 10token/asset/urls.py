from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.assets_list.as_view(), name='list'),
    url(r'^token/(?P<pk>[0-9]+)/$', views.asset_detail.as_view(), name='detail'),
]
