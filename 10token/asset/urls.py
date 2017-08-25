from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.AssetSearchList.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)$', views.AssetDetail.as_view(), name='detail'),
    # url(r'^search/', views.AssetSearchList.as_view(), name='search'),
]
