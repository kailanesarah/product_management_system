from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from brand.models import Brand
from brand.forms import BrandForm
from django.urls import reverse_lazy  # Importe reverse_lazy
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render


class BrandListView(ListView):
    model = Brand
    template_name = 'list_brands.html'
    context_object_name = 'brands'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset.order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand_forms = {
            brand.pk: BrandForm(
                instance=brand, prefix=f'{brand.pk}'
            )
            for brand in context['brands']
            if brand.pk  # <- só cria se tiver pk
        }
        context['brand_forms'] = brand_forms
        return context


class BrandCreateView(CreateView):
    model = Brand
    template_name = 'create_brands.html'
    form_class = BrandForm

    def get_success_url(self):
        return reverse_lazy('brand_list_view')


class BrandUpdateView(UpdateView):
    model = Brand
    template_name = 'update_modal.html'
    form_class = BrandForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['prefix'] = str(self.object.pk)
        return kwargs

    def get_success_url(self):
        return reverse_lazy('brand_list_view')

    def form_valid(self, form):
        form.save()
        return JsonResponse({'success': 'Marca atualizada!'})

    def form_invalid(self, form):
        print("Erros do form:", form.errors)
        return render(self.request, self.template_name, {'form': form, 'brand': self.object}, status=400)


class BrandDeleteView(DeleteView):
    model = Brand
    template_name = 'delete_confirm.html'

    def get_success_url(self):
        return reverse_lazy('brand_list_view')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({'success': True})
