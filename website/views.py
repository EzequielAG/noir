# -*- coding: utf-8 -*-
from django.template.loader import render_to_string
from django.views.generic import CreateView, DetailView
from django.core.mail.message import EmailMessage

from django_filters.views import FilterView

from website.models import ImageBanner, ImageCategoryBanner, Contact, Product
from website.forms import ContactForm
from website.view_filters import ProductFilter


class BannerMixin(object):
    """Herramienta para los banners
    """

    def get_banners_published(self):
        "Devuelve las imagenes publicadas ordenadas por la posicion"
        return ImageBanner.objects.filter(published=True).order_by('position')

    def get_unique(self, names):
        "Devuelve una lista sin elementos repetidos"
        unique_names = []

        [unique_names.append(x) for x in names if x not in unique_names]

        return unique_names

    def get_banners(self, place, name=None):
        "Devuelve una lista de banners segun la categoria"
        category = ImageCategoryBanner.objects.get(place=place)
        banners = []

        sizes = ['S', 'M', 'B']

        if name is None:
            names = self.get_banners_published().filter(category=category)\
                                                .values_list('name', flat=True)
        else:
            names = self.get_banners_published().filter(category=category)\
                                                .filter(name__istartswith=name)\
                                                .values_list('name', flat=(True))

        unique_names = self.get_unique(names)

        for name in unique_names:
            banner_sizes = {}
            for size in sizes:
                try:
                    banner_sizes[size] = self.get_banners_published().get(name=name,
                                                                          image_size=size)
                except ImageBanner.DoesNotExist:
                    banner_sizes[size] = None

            banners.append(banner_sizes)

        return banners


class ProductMixin(object):
    """Herramienta para los productos
    """

    def get_product_published(self, attribute='position'):
        "Devuelve los productos publicados por un orden"
        return Product.objects.filter(published=True).order_by(attribute)

    def get_product_outstanding(self):
        "Devuelve los productos destacados"
        return self.get_product_published().filter(outstanding=True)

    # def get_product_category
    # def get_product_product_gender


class HomeView(BannerMixin, ProductMixin, CreateView):
    """Pagina de Inicio
    """

    template_name = 'home/home.html'
    form_class = ContactForm
    model = Contact
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['main_banners'] = self.get_banners(place='Inicio', name='home')
        context['gender_banners'] = self.get_banners(place='Inicio', name='gender')
        context['testimonials_banners'] = self.get_banners(place='Inicio', name='testimonial')
        context['testimonial_background'] = self.get_banners(place='Inicio', name='testimonial')[0]
        context['product_outstanding'] = self.get_product_outstanding()[:6]

        return context

    def form_valid(self, form):
        self.object = form.save()
        subject = u"[Noir Style] Consulta realizada "\
                  u"por %(nombre)s" % {'nombre': self.object.name}
        message = render_to_string('emails_templates/email_consultation.txt',
                                   {'consultation': self.object})
        email = EmailMessage(subject, message, 'consultation@noirstyle.com',
                             ['eze94ale@gmail.com'], reply_to=[self.object.mail])
        email.send()
        # messages.info(self.request, 'La consulta fue enviada con éxito')
        return super(HomeView, self).form_valid(form)


class ProductListView(BannerMixin, ProductMixin, FilterView):
    """Pagina de Productos
    """

    template_name = 'product/product_list.html'
    filterset_class = ProductFilter
    paginate_by = 12
    queryset = Product.objects.filter(published=True).order_by('date')
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)

        context['product_banner'] = self.get_banners(place='Productos')[0]

        return context


class ProductDetailView(BannerMixin, ProductMixin, DetailView):
    """Pagina de Detalle de un Producto
    """

    template_name = 'product/product_detail.html'
    model = Product
    context_object_name = 'product'

    def get_main_product_category(self):
        "Devuelve la categoria más representativa del premio"

        try:
            main_category = self.object.category.order_by('-pk')[0]
        except IndexError:
            main_category = None

        return main_category

    def get_related_products(self):
        "Devuelve que queryset con los premios realcionados"
        visible_products = self.get_product_published()

        product_category = self.get_main_product_category()

        related_products = visible_products.exclude(pk=self.object.pk)

        if product_category:
            related_products = related_products.filter(category=product_category)

        return related_products

    def get_queryset(self):
        queryset = super(ProductDetailView, self).get_queryset()

        queryset = self.get_product_published()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)

        product = self.object

        context['product_banner'] = self.get_banners(place='Productos', name='product_detalle')[0]

        context['product_med_images'] = product.get_images('S')

        context['product_categories'] = product.category.all()

        context['related_products'] = self.get_related_products()[:4]

        return context
