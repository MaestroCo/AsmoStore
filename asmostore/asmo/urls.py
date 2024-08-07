from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('shop/', views.products, name='shop'),
    path('products/price/0_50/', views.products_0_50, name='products_0_50'),
    path('products/price/50_100/', views.products_50_100, name='products_50_100'),
    path('products/price/100_150/', views.products_100_150, name='products_100_150'),
    path('products/price/150_200/', views.products_150_200, name='products_150_200'),
    path('products/price/200_plus/', views.products_200_plus, name='products_200_plus'),
    path('product-<slug:slug>-detail/', views.product_detail, name='product_detail'),

    path('products-sort/<slug:sort_slug>/', views.product_sort, name='products_sort'),

    path('products-color/<slug:color_slug>/', views.product_color, name='product_color'),

    path('products-brand/<slug:brand_slug>/', views.product_brand, name='product_brand'),

    path('blogs/', views.blog, name='blogs'),
    path('blogs/<slug:tag_slug>/', views.blogs_tag, name='blogs_tag'),
    path('blog-detail/<slug:slug>/', views.blog_detail, name='blog_detail'),

    path('about/', views.aboutus, name='about'),

    path('cart/', views.cart, name='cart'),
    path('to-cart/<slug:product_slug>/<str:action>/', views.to_cart, name='to_cart'),
    path('clear-cart/', views.clear_cart, name='clear_cart'),
    path('delete-cart/<slug:product_slug>/', views.delete_cart, name='delete_cart'),

    path('user-login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='user_register'),
    path('my-accaunt/<str:username>/', views.user_profile, name='user_profile'),
    path('user-profile-edit/<str:username>/', views.user_profile_edit, name='user_profile_edit'),
    path('add-to-wishlist/<slug:product_slug>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('my-wishlist/', views.wishlist_view, name='my_wishlist'),
    path('remove-from-wishlist/<slug:product_slug>/', views.remove_from_wishlist, name='remove_from_wishlist'),

    path('contact-us/', views.contact_us, name='contact_us'),
    path('payment/', views.create_checkout_sessions, name='payment'),
    # path('payment/', views.success_payment, name='payment'),
    path('success/', views.success_payment, name='success'),
    path('delete-review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('delete-review-blog/<int:review_id>/', views.blog_del_review, name='blog_delete_review')
]
