from django.conf.urls import url

from website.views import HomeView, ProductListView, ProductDetailView

urlpatterns = [

    # Pagina inicial
    url(r'^$', HomeView.as_view(),
        name='home'),

    # Productos
    url(r'^productos$', ProductListView.as_view(),
        name='products'),
    url(r'^producto/(?P<pk>\d+)$', ProductDetailView.as_view(),
        name='product_detail')
]
