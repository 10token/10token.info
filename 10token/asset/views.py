from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Asset
from django.utils import timezone

# def assets_list(request):
#     assets = Asset.objects.filter().order_by('published_date')
#     return render(request, 'asset/assets_list.html', {'assets': assets})

class assets_list(LoginRequiredMixin, ListView):
    model = Asset

    # slug_field = 'name'
    # slug_url_kwarg = 'name'
    #
    # def get_context_data(self, **kwargs):
    #     context = super(assets_list, self).get_context_data(**kwargs)
    #     # context['now'] = timezone.now()
    #     return context



class asset_detail(LoginRequiredMixin, DetailView):
    model = Asset
    # These next two lines tell the view to index lookups by username
    # slug_field = 'name'
    # slug_url_kwarg = 'name'

# def asset_detail(request, pk):
#     asset = get_object_or_404(Asset, pk=pk)
#     return render(request, 'asset/asset_detail.html', {'asset': asset})
