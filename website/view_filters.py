from django_filters import FilterSet, CharFilter, ModelChoiceFilter, ChoiceFilter

from website.models import Product, CategoryProduct


class ProductFilter(FilterSet):
    """Filtro de los Productos
    """

    name = CharFilter(lookup_expr='icontains')
    category = ModelChoiceFilter(queryset=CategoryProduct.objects.all().order_by('name'),
                                 empty_label=u'Todas las categorias')
    price = ChoiceFilter(choices=[(u'$', u'$100'), (u'$$', u'$200'), (u'$$$', u'$300')],
                         method='filter_price', empty_label=u'Cualquier precio')
    product_gender = ChoiceFilter(choices=Product.SEX_CHOICE, empty_label=u'Todos los generos')

    def filter_price(self, queryset, name, value):

        if value == u'$':
            return Product.objects.filter(price__lte=100)
        elif value == u'$$':
            return Product.objects.filter(price__lte=200)
        elif value == u'$$$':
            return Product.objects.filter(price__lte=300)
        else:
            return Product.objects.all()

    class Meta:
        model = Product
        fields = ['category', 'price', 'product_gender']
