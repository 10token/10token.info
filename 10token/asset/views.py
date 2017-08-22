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


# class assets_list(LoginRequiredMixin, ListView):
#     # model = Asset
#     slug_field = 'name'
#     slug_url_kwarg = 'name'
#     # paginate_by = 10




class asset_detail(LoginRequiredMixin, DetailView):
    model = Asset
    # These next two lines tell the view to index lookups by username
    slug_field = 'name'
    slug_url_kwarg = 'name'
