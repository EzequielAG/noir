from django.contrib import admin

from models import Product, ImageProduct, CategoryProduct, ProductGender,\
    ImageBanner, ImageCategoryBanner, FAQ, Contact

admin.site.register(Product)
admin.site.register(ImageProduct)
admin.site.register(CategoryProduct)
admin.site.register(ProductGender)
admin.site.register(ImageBanner)
admin.site.register(ImageCategoryBanner)
admin.site.register(FAQ)
admin.site.register(Contact)
