# -*- coding: utf-8 -*-
from django.views.generic.edit import FormView

from website.models import ImageBanner, ImageCategoryBanner
from website.forms import ContactForm


class BannerMixin(object):
    """Herramienta para los banners
    """

    def banners_published(self):
        "Devuelve las imagenes publicadas ordenadas por la posicion"
        return ImageBanner.objects.filter(published=True).order_by('position')

    def get_unique(self, names):
        "Devuelve una lista sin elementos repetidos"
        unique_names = []

        [unique_names.append(x) for x in names if x not in unique_names]

        return unique_names

    def get_banners(self, category, name=None):
        "Devuelve una lista de banners segun la categoria"
        banners = []

        sizes = ['S', 'M', 'B']

        if name is None:
            names = self.banners_published().filter(category=category)\
                                            .values_list('name', flat=True)
        else:
            names = self.banners_published().filter(category=category)\
                                            .filter(name__istartswith=name)\
                                            .values_list('name', flat=(True))

        unique_names = self.get_unique(names)

        for name in unique_names:
            banner_sizes = {}
            for size in sizes:
                try:
                    banner_sizes[size] = self.banners_published().get(name=name, image_size=size)
                except ImageBanner.DoesNotExist:
                    banner_sizes[size] = None

            banners.append(banner_sizes)

        return banners


class HomeView(BannerMixin, FormView):
    """Pagina de Inicio
    """

    template_name = 'home/home.html'
    form_class = ContactForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        category = ImageCategoryBanner.objects.get(place="Inicio")
        context['main_banners'] = self.get_banners(category=category, name='home')
        context['gender_banners'] = self.get_banners(category=category, name='gender')

        return context
