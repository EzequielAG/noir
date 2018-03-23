from django.contrib import admin

from website.models import Product, ImageProduct, CategoryProduct, ImageBanner,\
    ImageCategoryBanner, Contact


class ImageProductInline(admin.TabularInline):

    model = ImageProduct
    extra = 1


class ProductAdmin(admin.ModelAdmin):

    inlines = [ImageProductInline]
    list_display = ('code', 'name', 'description', 'published', 'outstanding', 'price',
                    'position', 'product_gender')
    list_display_links = ('name', )
    list_filter = ['published', 'outstanding', 'category', 'price']
    search_fields = ['code', 'name']
    list_per_page = 20
    ordering = ['name']


class ContactAdmin(admin.ModelAdmin):

    list_display = ('name', 'mail', 'cell_phone', 'submited_on', 'read')
    list_display_links = ('name', )
    search_fields = ['name', 'code', 'cell_phone']
    list_filter = ['read']
    readonly_fields = ('name', 'mail', 'cell_phone', 'submited_on', 'message')
    list_per_page = 20


class ImageBannerAdmin(admin.ModelAdmin):

    list_display = ('name', 'title', 'category', 'image_size', 'published')
    list_display_links = ('name', 'title')
    search_fields = ['name', 'title']
    list_filter = ['category', 'image_size', 'published']
    list_per_page = 20


admin.site.register(Product, ProductAdmin)
admin.site.register(CategoryProduct)
admin.site.register(ImageBanner, ImageBannerAdmin)
admin.site.register(ImageCategoryBanner)
admin.site.register(Contact, ContactAdmin)
