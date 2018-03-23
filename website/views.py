# -*- coding: utf-8 -*-
from django.template.loader import render_to_string
from django.views.generic.edit import CreateView
from django.core.mail.message import EmailMessage

from website.models import ImageBanner, ImageCategoryBanner, Contact
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


class HomeView(BannerMixin, CreateView):
    """Pagina de Inicio
    """

    template_name = 'home/home.html'
    form_class = ContactForm
    model = Contact
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        category = ImageCategoryBanner.objects.get(place="Inicio")
        context['main_banners'] = self.get_banners(category=category, name='home')
        context['gender_banners'] = self.get_banners(category=category, name='gender')

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
