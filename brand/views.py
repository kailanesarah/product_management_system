from django.views.generic import ListView
from brand.models import Brand


class BrandListView(ListView):
    model = Brand
    template_name = 'list_brands.html'
    context_object_name = 'brands'

    def get_queryset(self):  # trás os dados do banco de dados de forma personalizada, por exemplo, quero apenas produtos de tal marca, é isso que esse método faz
        # O super respeita as regras da view, por isso a gente pega os objetos assim, ao invés de Brand.objects.all(), assim a gente já travalha em cima dos dados
        queryset = super().get_queryset()
        name = self.request.GET.get('name')  

        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset.order_by('id')
