from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Asset
from django.utils import timezone

from .forms import AssetSearchForm
from search_views.search import SearchListView
from search_views.filters import BaseFilter


class AssetFilter(BaseFilter):
    search_fields = {
        'search_text' : ['name'],
        # 'token_id_exact' : { 'token_id' },
    }

class AssetSearchList(SearchListView):
    model = Asset
    paginate_by = 30
    template_name = "asset/asset_list.html"
    form_class = AssetSearchForm
    filter_class = AssetFilter


class AssetSelected(ListView):
    model = Asset
    context_object_name = 'asset'
    # slug_field = 'name'
    # slug_url_kwarg = 'name'
    # queryset = Asset.objects.filter(selected=True)
    template_name = 'asset/asset_list.html'
    paginate_by = 10

    def get_queryset(self):
        """
        Список наших объектов будет состоять лишь из отмеченных модераторами токенов
        """
        return Asset.objects.filter(selected=True)

class AssetDetail(DetailView):
    model = Asset
    # These next two lines tell the view to index lookups by username
    slug_field = 'token_id'
    slug_url_kwarg = 'token_id'
