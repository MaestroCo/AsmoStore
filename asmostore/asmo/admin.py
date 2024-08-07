from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import (Category, Color, Product, ProductReview, Sort, Size, User, Brand, BlogPost, BlogTags, Customer,
                     Order, OrderProduct, ShippingAddress, Wishlist, BlogReview)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_image']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name',)}

    def get_image(self, obj):
            return mark_safe(f'<img src="{obj.image.url if obj.image else None}" width="75">')

    get_image.short_description = 'Kategoriya rasmi'


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'category', 'price', 'quantity', 'get_image', 'get_image2', 'get_image3']
    list_display_links = ['name']
    list_filter = ['category', 'price', 'quantity', 'brand', 'category']
    search_fields = ['name', 'description', 'brand']
    ordering = ['name']
    prepopulated_fields = {'slug': ('name', 'price', 'quantity', )}

    def get_image(self, obj1):
            return mark_safe(f'<img src="{obj1.image.url if obj1.image else None}" width="75">')

    get_image.short_description = 'Mahsulot rasmi 1'

    def get_image2(self, obj2):
            return mark_safe(f'<img src="{obj2.image1.url if obj2.image1 else None}" width="75">')

    get_image2.short_description = 'Mahsulot rasmi 2'

    def get_image3(self, obj3):
            return mark_safe(f'<img src="{obj3.image2.url if obj3.image2 else None}" width="75">')

    get_image3.short_description = 'Mahsulot rasmi 3'


@admin.register(Sort)
class SortAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(ProductReview)
class ProductReview(admin.ModelAdmin):
    list_display = ['user', 'product', 'rating', 'date']
    list_display_links = ['user', 'product']
    search_fields = ['user', 'product', 'comment']


@admin.register(Brand)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date', 'get_image']
    list_display_links = ['title']
    prepopulated_fields = {'slug': ('title', 'author', )}
    search_fields = ['title', 'author', 'content']

    def get_image(self, obj):
            return mark_safe(f'<img src="{obj.image.url if obj.image else None}" width="75">')

    get_image.short_description = 'Maqola rasmi'


@admin.register(BlogTags)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['tag']
    list_display_links = ['tag']
    prepopulated_fields = {'slug': ('tag', )}


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'firstname', 'lastname')
    search_fields = ('firstname', 'lastname', 'user__username')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'created', 'is_active', 'get_cart_total_price', 'get_cart_quantity')
    list_filter = ('is_active', 'created')
    search_fields = ('customer__firstname', 'customer__lastname', 'customer__user__username')

@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'get_cart_price', 'added')
    search_fields = ('order__customer__firstname', 'order__customer__lastname', 'product__name')

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('customer', 'address', 'city', 'district', 'zipcode', 'mobile', 'email')
    list_filter = ('city', 'district')
    search_fields = ('customer__firstname', 'customer__lastname', 'customer__user__username', 'address')


@admin.register(Wishlist)
class WishListAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_products_count', 'created_at', 'updated_at']
    list_display_links = ['user', 'get_products_count']

    def get_products_count(self, obj):
        return obj.products.count()
    get_products_count.short_description = 'Mahsulotlar'


@admin.register(BlogReview)
class BlogReview(admin.ModelAdmin):
    list_display = ['user', 'blog', 'date']
    list_display_links = ['user', 'blog']
    search_fields = ['user', 'blog', 'comment']
