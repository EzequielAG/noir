from django.conf.urls import url

from website.views import HomeView

urlpatterns = [

    # Pagina inicial
    url(r'^$', HomeView.as_view(),
        name='home'),
]
