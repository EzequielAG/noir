from django.views.generic.base import TemplateView

from website.models import ImageBanner, ImageCategoryBanner


class BannerMixin(object):
    """Herramienta para los banners
    """

    def banners_published(self):
        "Devuelve las imagenes publicadas ordenadas por la posicion"
        return ImageBanner.objects.filter(published=True).order_by('position')

    def get_banners(self, category):
        "Devuelve una lista de banners segun la categoria"
        return self.banners_published().filter(category=category)


class HomeView(BannerMixin, TemplateView):

    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        category = ImageCategoryBanner.objects.get(place="Inicio")
        context['banners'] = self.get_banners(category=category)

        return context
