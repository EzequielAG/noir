from django.conf.urls import url

from website.views import HomeView, ProductListView

urlpatterns = [

    # Pagina inicial
    url(r'^$', HomeView.as_view(),
        name='home'),

    # Productos
    url(r'^productos$', ProductListView.as_view(),
        name='products'),
]
