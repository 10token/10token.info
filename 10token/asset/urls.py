from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.AssetSearchList.as_view(), name='list'),
    url(r'^token/(?P<pk>[0-9]+)/$', views.asset_detail.as_view(), name='detail'),
    # url(r'^search/', views.AssetSearchList.as_view(), name='search'),
]
