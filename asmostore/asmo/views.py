import stripe
from django.contrib import messages
from django.contrib.auth import logout, login
from django.db.models import Max, Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.views.generic import TemplateView, ListView
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ProductReviewForm, ShippingAddressForm, RegisterForm, LoginForm, UserProfileForm, BlogReviewForm
from .models import ProductReview, Product, User, Color, Category, Size, Sort, Brand, BlogPost, BlogTags, UserProfile, \
    Wishlist, BlogReview, OrderProduct
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from .utils import CartAuthenticatedUser


def index(request):
    context = {
        'products': Product.objects.all(),
        'title': 'ASMO | Asosiy sahifa',
        'brands': Brand.objects.all(),
        'blogs': BlogPost.objects.all(),
        'categories': Category.objects.all(),
        'order_products': [],
        'cart_total_price': 0,
        'cart_total_quantity': 0
    }
    if request.user.is_authenticated:
        cart_info = CartAuthenticatedUser(request)
        context['order_products'] = cart_info.get_cart_info()['order_products']
        context['cart_total_price'] = cart_info.get_cart_info()['cart_total_price']
        context['cart_total_quantity'] = cart_info.get_cart_info()['cart_total_quantity']

    return render(request, 'asmo/index.html', context)



# ===================================================FOR SHOP PAGE======================================================


# def products(request):
#     context = {
#         'products': Product.objects.all(),
#         'categories': Category.objects.all(),
#         'colors': Color.objects.all(),
#         'brands': Brand.objects.all(),
#         'sorts': Sort.objects.all(),
#         'title': 'ASMO | Barcha mahsulotlar'
#     }
#     if request.user.is_authenticated:
#         cart_info = CartAuthenticatedUser(request)
#         context.update({
#             'order_products': cart_info.get_cart_info()['order_products'],
#             'cart_total_price': cart_info.get_cart_info()['cart_total_price'],
#             'cart_total_quantity': cart_info.get_cart_info()['cart_total_quantity']
#         })
#     return render(request, 'asmo/shop.html', context)

def products(request):
    context = {
        'categories': Category.objects.all(),
        'colors': Color.objects.all(),
        'brands': Brand.objects.all(),
        'sorts': Sort.objects.all(),
        'title': 'ASMO | Barcha mahsulotlar'
    }

    all_products = Product.objects.all()
    paginator = Paginator(all_products, 8)
    page_number = request.GET.get('page')
    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context['products'] = products

    if request.user.is_authenticated:
        cart_info = CartAuthenticatedUser(request)
        context.update({
            'order_products': cart_info.get_cart_info()['order_products'],
            'cart_total_price': cart_info.get_cart_info()['cart_total_price'],
            'cart_total_quantity': cart_info.get_cart_info()['cart_total_quantity']
        })

    return render(request, 'asmo/shop.html', context)


def products_0_50(request):
    categories = Category.objects.all()
    colors = Color.objects.all()
    brands = Brand.objects.all()
    sorts = Sort.objects.all()
    products_50 = Product.objects.filter(price__gte=0, price__lte=50)
    context = {
        'products_50': products_50,
        'categories': categories,
        'colors': colors,
        'brands': brands,
        'sorts': sorts,
        'title': f'ASMO | Barcha mahsulotlar'
    }
    if request.user.is_authenticated:
        cart_info = CartAuthenticatedUser(request)
        context.update({
            'order_products': cart_info.get_cart_info()['order_products'],
            'cart_total_price': cart_info.get_cart_info()['cart_total_price'],
            'cart_total_quantity': cart_info.get_cart_info()['cart_total_quantity']
        })
    return render(request, 'asmo/shop.html', context)


def products_50_100(request):
    categories = Category.objects.all()
    colors = Color.objects.all()
    brands = Brand.objects.all()
    sorts = Sort.objects.all()
    products_100 = Product.objects.filter(price__gte=50, price__lte=100)
    context = {
        'products_100': products_100,
        'categories': categories,
        'colors': colors,
        'brands': brands,
        'sorts': sorts,
        'title': f'ASMO | Barcha mahsulotlar'
    }
    if request.user.is_authenticated:
        cart_info = CartAuthenticatedUser(request)
        context.update({
            'order_products': cart_info.get_cart_info()['order_products'],
            'cart_total_price': cart_info.get_cart_info()['cart_total_price'],
            'cart_total_quantity': cart_info.get_cart_info()['cart_total_quantity']
        })
    return render(request, 'asmo/shop.html', context)


def products_100_150(request):
    categories = Category.objects.all()
    colors = Color.objects.all()
    brands = Brand.objects.all()
    sorts = Sort.objects.all()
    products_150 = Product.objects.filter(price__gte=100, price__lte=150)
    context = {
        'products_150': products_150,
        'categories': categories,
        'colors': colors,
        'brands': brands,
        'sorts': sorts,
        'title': f'ASMO | Barcha mahsulotlar'
    }
    if request.user.is_authenticated:
        cart_info = CartAuthenticatedUser(request)
        context.update({
            'order_products': cart_info.get_cart_info()['order_products'],
            'cart_total_price': cart_info.get_cart_info()['cart_total_price'],
            'cart_total_quantity': cart_info.get_cart_info()['cart_total_quantity']
        })
    return render(request, 'asmo/shop.html', context)


def products_150_200(request):
    categories = Category.objects.all()
    colors = Color.objects.all()
    brands = Brand.objects.all()
    sorts = Sort.objects.all()
    products_200 = Product.objects.filter(price__gte=150, price__lte=200)
    context = {
        'products_200': products_200,
        'categories': categories,
        'colors': colors,
        'brands': brands,
        'sorts': sorts,
        'title': f'ASMO | Barcha mahsulotlar'
    }
    if request.user.is_authenticated:
        cart_info = CartAuthenticatedUser(request)
        context.update({
            'order_products': cart_info.get_cart_info()['order_products'],
            'cart_total_price': cart_info.get_cart_info()['cart_total_price'],
            'cart_total_quantity': cart_info.get_cart_info()['cart_total_quantity']
        })
    return render(request, 'asmo/shop.html', context)


def products_200_plus(request):
    categories = Category.objects.all()
    colors = Color.objects.all()
    brands = Brand.objects.all()
    sorts = Sort.objects.all()
    products_plus = Product.objects.filter(price__gte=200)
    context = {
        'products_plus': products_plus,
        'categories': categories,
        'colors': colors,
        'brands': brands,
        'sorts': sorts,
        'title': f'ASMO | Barcha mahsulotlar'
    }
    if request.user.is_authenticated:
        cart_info = CartAuthenticatedUser(request)
        context.update({
            'order_products': cart_info.get_cart_info()['order_products'],
            'cart_total_price': cart_info.get_cart_info()['cart_total_price'],
            'cart_total_quantity': cart_info.get_cart_info()['cart_total_quantity']
        })
    return render(request, 'asmo/shop.html', context)

# ===================================================END SHOP PAGE======================================================

# ===================================================FOR SORT PAGE======================================================


def product_sort(request, sort_slug):
    products_sort = Product.objects.filter(sort__slug=sort_slug)
    categories = Category.objects.all()
    colors = Color.objects.all()
    brands = Brand.objects.all()
    sorts = Sort.objects.all()
    context = {
        'products_sort': products_sort,
        'categories': categories,
        'colors': colors,
        'brands': brands,
        'sorts': sorts,
        'title': f'ASMO | Barcha mahsulotlar'
    }
    if request.user.is_authenticated:
        cart_info = CartAuthenticatedUser(request)
        context.update({
            'order_products': cart_info.get_cart_info()['order_products'],
            'cart_total_price': cart_info.get_cart_info()['cart_total_price'],
            'cart_total_quantity': cart_info.get_cart_info()['cart_total_quantity']
        })
    return render(request, 'asmo/shop.html', context)


# ===================================================FOR COLOR PAGE=====================================================


def product_color(request, color_slug):
    products_color = Product.objects.filter(color__slug=color_slug)
    categories = Category.objects.all()
    colors = Color.objects.all()
    brands = Brand.objects.all()
    sorts = Sort.objects.all()
    context = {
        'products_color': products_color,
        'categories': categories,
        'colors': colors,
        'brands': brands,
        'sorts': sorts,
        'title': f'ASMO | Barcha mahsulotlar'
    }
    if request.user.is_authenticated:
        cart_info = CartAuthenticatedUser(request)
        context.update({
            'order_products': cart_info.get_cart_info()['order_products'],
            'cart_total_price': cart_info.get_cart_info()['cart_total_price'],
            'cart_total_quantity': cart_info.get_cart_info()['cart_total_quantity']
        })
    return render(request, 'asmo/shop.html', context)


# ===================================================FOR COLOR PAGE=====================================================


def product_brand(request, brand_slug):
    products_brand = Product.objects.filter(brand__slug=brand_slug)
    categories = Category.objects.all()
    colors = Color.objects.all()
    brands = Brand.objects.all()
    sorts = Sort.objects.all()
    context = {
        'products_color': products_brand,
        'categories': categories,
        'colors': colors,
        'brands': brands,
        'sorts': sorts,
        'title': f'ASMO | Barcha mahsulotlar'
    }
    if request.user.is_authenticated:
        cart_info = CartAuthenticatedUser(request)
        context.update({
            'order_products': cart_info.get_cart_info()['order_products'],
            'cart_total_price': cart_info.get_cart_info()['cart_total_price'],
            'cart_total_quantity': cart_info.get_cart_info()['cart_total_quantity']
        })
    return render(request, 'asmo/shop.html', context)

# ===================================================FOR BLOG PAGE=====================================================


def blog(request):
    all_blogs = BlogPost.objects.all()
    paginator = Paginator(all_blogs, 2)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)

    context = {
        'blogs': blogs,
        'blog_tags': BlogTags.objects.all(),
        'products_quantity': Product.objects.filter(Q(quantity__lte=10) & ~Q(image='')),
        'tags': BlogPost.objects.all(),
        'title': "Blog"
    }

    if request.user.is_authenticated:
        cart_info = CartAuthenticatedUser(request)
        context.update({
            'order_products': cart_info.get_cart_info()['order_products'],
            'cart_total_price': cart_info.get_cart_info()['cart_total_price'],
            'cart_total_quantity': cart_info.get_cart_info()['cart_total_quantity']
        })

    return render(request, 'asmo/blog.html', context)


def blogs_tag(request, tag_slug):
    context = {
        'products_quantity': Product.objects.filter(Q(quantity__lte=10) & ~Q(image='')),
        'tags': BlogPost.objects.all(),
        'title': "Blog",
        'blog_tags': BlogTags.objects.all(),
        'blogs_tag': BlogPost.objects.filter(tag__slug=tag_slug)
    }
    if request.user.is_authenticated:
        cart_info = CartAuthenticatedUser(request)
        context.update({
            'order_products': cart_info.get_cart_info()['order_products'],
            'cart_total_price': cart_info.get_cart_info()['cart_total_price'],
            'cart_total_quantity': cart_info.get_cart_info()['cart_total_quantity']
        })
    return render(request, 'asmo/blog.html', context)


# def blog_detail(request, slug):
#     blog = BlogPost.objects.get(slug=slug)
#     products_quantity = Product.objects.filter(Q(quantity__lte=10) & ~Q(image=''))
#     tags = blog.tag.all()
#
#     context = {
#         'blog': blog,
#         'products_quantity': products_quantity,
#         'tags': tags,
#         'blog_tags': BlogTags.objects.all(),
#         'title': "Blog"
#     }
#
#     if request.user.is_authenticated:
#         cart_info = CartAuthenticatedUser(request).get_cart_info()
#         context.update({
#             'order_products': cart_info['order_products'],
#             'cart_total_price': cart_info['cart_total_price'],
#             'cart_total_quantity': cart_info['cart_total_quantity']
#         })
#
#     return render(request, 'asmo/blog_detail.html', context)


def blog_detail(request, slug):
    blog = BlogPost.objects.get(slug=slug)
    products_quantity = Product.objects.filter(Q(quantity__lte=10) & ~Q(image=''))
    reviews = BlogReview.objects.filter(blog=blog).order_by('-date')
    tags = blog.tag.all()

    context = {
        'blog': blog,
        'reviews': reviews,
        'products_quantity': products_quantity,
        'tags': tags,
        'blog_tags': BlogTags.objects.all(),
        'title': "Blog"
    }

    if request.method == 'POST':
        form = BlogReviewForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.blog = blog
                comment.save()
                return redirect('blog_detail', slug=slug)
        else:
            return redirect('login')
    else:
        form = BlogReviewForm()

    if request.user.is_authenticated:
        cart_info = CartAuthenticatedUser(request).get_cart_info()
        context.update({
            'order_products': cart_info['order_products'],
            'cart_total_price': cart_info['cart_total_price'],
            'cart_total_quantity': cart_info['cart_total_quantity']
        })

    context['form'] = form

    return render(request, 'asmo/blog_detail.html', context)




# ===================================================FOR ABOUT PAGE=====================================================


def aboutus(request):
    context = {'title': "Biz haqimizda"}
    if request.user.is_authenticated:
        cart_info = CartAuthenticatedUser(request)
        context.update({
            'order_products': cart_info.get_cart_info()['order_products'],
            'cart_total_price': cart_info.get_cart_info()['cart_total_price'],
            'cart_total_quantity': cart_info.get_cart_info()['cart_total_quantity']
        })
    return render(request, 'asmo/about.html', context)


# ==============================================FOR PRODUCT DETAIL PAGE=================================================


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category=product.category).exclude(slug=slug)
    reviews = ProductReview.objects.filter(product=product).order_by('-date')
    form = ProductReviewForm()
    context = {
        'product': product,
        'title': "ASMO | Mahsulot",
        'related_products': related_products,
        'reviews': reviews,
        'form': form,
        'order_products': [],
        'cart_total_price': 0,
        'cart_total_quantity': 0
    }

    if request.user.is_authenticated:
        cart_info = CartAuthenticatedUser(request)
        context.update({
            'order_products': cart_info.get_cart_info()['order_products'],
            'cart_total_price': cart_info.get_cart_info()['cart_total_price'],
            'cart_total_quantity': cart_info.get_cart_info()['cart_total_quantity']
        })

    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.product = product
                review.save()
                messages.success(request, 'Izohingiz muvaffaqiyatli qo\'shildi.')
                return redirect('product_detail', slug=slug)
            else:
                messages.error(request, 'Izoh qo\'shishda xato yuz berdi.')
        else:
            return redirect('login')

    return render(request, 'asmo/product_detail.html', context)


# ==================================================FOR CART PAGE=======================================================


# def cart(request):
#     cart_info = CartAuthenticatedUser(request)
#     context = {
#         'order_products': cart_info.get_cart_info()['order_products'],
#         'cart_total_price': cart_info.get_cart_info()['cart_total_price'],
#         'cart_total_quantity': cart_info.get_cart_info()['cart_total_quantity'],
#         'title': 'Savat'
#     }
#     return render(request, 'asmo/cart.html', context)

# def cart(request):
#     # Cart ma'lumotlarini olish
#     cart_info = CartAuthenticatedUser(request)
#     cart_context = {
#         'order_products': cart_info.get_cart_info()['order_products'],
#         'cart_total_price': cart_info.get_cart_info()['cart_total_price'],
#         'cart_total_quantity': cart_info.get_cart_info()['cart_total_quantity'],
#         'cart_total_price_shipping': cart_info.get_cart_info()['cart_total_price_shipping'],
#         'title': 'Savat'
#     }
#
#     # ShippingAddressForm bilan ishlash
#     if request.method == 'POST':
#         form = ShippingAddressForm(request.POST)
#         if form.is_valid():
#             if request.user.is_authenticated:
#                 shipping_address = form.save(commit=False)
#                 shipping_address.customer = request.user
#                 shipping_address.save()
#                 return redirect('index')
#         else:
#             cart_context['form'] = form
#     else:
#         form = ShippingAddressForm()
#         cart_context['form'] = form
#
#     return render(request, 'asmo/cart.html', cart_context)
def cart(request):
    if request.user.is_authenticated:
        cart_info = CartAuthenticatedUser(request)
    else:
        cart_info = None

    cart_context = {
        'order_products': cart_info.get_cart_info()['order_products'] if cart_info else [],
        'cart_total_price': cart_info.get_cart_info()['cart_total_price'] if cart_info else 0,
        'cart_total_quantity': cart_info.get_cart_info()['cart_total_quantity'] if cart_info else 0,
        'cart_total_price_shipping': cart_info.get_cart_info()['cart_total_price_shipping'] if cart_info else 0,
        'title': 'Savat'
    }
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                shipping_address = form.save(commit=False)
                shipping_address.customer = request.user
                shipping_address.save()
                return redirect('index')
            else:
                pass
        else:
            cart_context['form'] = form
    else:
        form = ShippingAddressForm()
        cart_context['form'] = form

    return render(request, 'asmo/cart.html', cart_context)


def to_cart(request, product_slug, action):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
    else:
        quantity = 1
    if request.user.is_authenticated:
        CartAuthenticatedUser(request, product_slug, action, quantity)
        current_page = request.META.get('HTTP_REFERER', 'index')
        return redirect(current_page)
    else:
        return redirect('login')


def clear_cart(request):
    if request.user.is_authenticated:
        cart_info = CartAuthenticatedUser(request)
        order = cart_info.get_cart_info()['order']
        order_products = order.orderproduct_set.all()
        for order_product in order_products:
            product = order_product.product
            product.quantity += order_product.quantity
            product.save()
            order_product.delete()
        return redirect('cart')
    else:
        messages.error(request, 'Ro\'yxatdan o\'ting')
        return redirect('login')



def delete_cart(request, product_slug):
    if request.user.is_authenticated:
        try:
            cart_info = CartAuthenticatedUser(request)
            order = cart_info.get_cart_info()['order']
            product = Product.objects.get(slug=product_slug)
            order_product = order.orderproduct_set.get(product=product)
            product.quantity += order_product.quantity
            product.save()
            order_product.delete()
            messages.success(request, 'Mahsulot savatchadan o\'chirildi.')
        except (OrderProduct.DoesNotExist, Product.DoesNotExist):
            messages.error(request, 'Mahsulot savatchada mavjud emas.')
        current_page = request.META.get('HTTP_REFERER', 'cart')
        return redirect(current_page)
    else:
        messages.error(request, 'Iltimos, ro\'yxatdan o\'ting.')
        return redirect('login')

# ==================================================FOR ACCAUNT PAGE====================================================


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'{user.username} saytga muvaffaqiyatli kirdingiz!')
            return redirect('index')
        else:
            messages.error(request, 'Login yoki parol noto‘g‘ri. Iltimos, qayta urinib ko‘ring.')
    else:
        form = LoginForm()
    return render(request, 'asmo/user_login.html', {'form': form, 'title': 'Login'})


def user_logout(request):
    logout(request)
    messages.success(request, 'Profildan muvaffaqqiyatli chiqildi')
    return redirect('login')


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Bu username mavjud. Boshqa username tanlang.')
            return redirect('user_register')
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'{user.username}, siz saytga muvaffaqiyatli ro\'yxatdan o\'tdingiz!')
            return redirect('index')
    else:
        form = RegisterForm()

    context = {
        'form': form,
        'title': 'Ro\'yxatdan o\'tish'
    }
    return render(request, 'asmo/user_register.html', context)


def user_profile(request, username):
    user = User.objects.get(username=username)
    if request.user != user:
        messages.error(request, 'Siz faqat o\'zingizni profilingizni ko\'ra olasiz!')
        return redirect('login')
    context = {
        'user': user,
        'title': f'{user.username} profili',
    }

    try:
        user_profile = UserProfile.objects.get(user=user)
        context['user_profile'] = user_profile
    except:
        pass
    return render(request, 'asmo/my_accaunt.html', context)


def user_profile_edit(request, username):
    user = get_object_or_404(User, username=username)
    user_profile, created = UserProfile.objects.get_or_create(user=user)
    if request.user != user:
        messages.error(request, f'{user.username}, siz faqat o\'z profilingizni tahrirlay olasiz.')
        return redirect('login')
    else:
        if request.method == 'POST':
            form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profil muvaffaqiyatli yangilandi.')
                return redirect('user_profile', username=user.username)
        else:
            form = UserProfileForm(instance=user_profile)

    context = {
        'form': form,
        'title': f'{user.username} - Profilni Tahrirlash'
    }
    return render(request, 'asmo/profile_edit.html', context)


def add_to_wishlist(request, product_slug):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, slug=product_slug)
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        if product not in wishlist.products.all():
            wishlist.products.add(product)
            current_page = request.META.get('HTTP_REFERER', 'shop')
            return redirect(current_page)
        else:
            return redirect('shop')
    else:
        return redirect('login')


def wishlist_view(request):
    if request.user.is_authenticated:
        wishlist = Wishlist.objects.filter(user=request.user).first()
        if wishlist:
            products_in_wishlist = wishlist.products.all()
        else:
            products_in_wishlist = []

        context = {
            'products_in_wishlist': products_in_wishlist,
            'title': 'Tanlangan mahsulotlar'
        }
        return render(request, 'asmo/my_wishlist.html', context)
    else:
        return redirect('login')


def remove_from_wishlist(request, product_slug):
    wishlist = get_object_or_404(Wishlist, user=request.user)
    product = get_object_or_404(Product, slug=product_slug)

    if product in wishlist.products.all():
        wishlist.products.remove(product)
        return redirect('my_wishlist')
    else:
        return redirect('my_wishlist')



# ==================================================FOR CONTACT PAGE====================================================


def contact_us(request):
    context = {'title': "Aloqa"}
    if request.user.is_authenticated:
        cart_info = CartAuthenticatedUser(request)
        context.update({
            'order_products': cart_info.get_cart_info()['order_products'],
            'cart_total_price': cart_info.get_cart_info()['cart_total_price'],
            'cart_total_quantity': cart_info.get_cart_info()['cart_total_quantity']
        })
    return render(request, 'asmo/contact.html', context)


# ==================================================FOR PAYMENT PAGE====================================================


def create_checkout_sessions(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    user_cart = CartAuthenticatedUser(request)
    cart_info = user_cart.get_cart_info()
    total_price = cart_info['cart_total_price_shipping']
    total_quantity = cart_info['cart_total_quantity']
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'Asmo Store mahsulotlari'
                },
                'unit_amount': int(total_price * 100)
            },
            'quantity': total_quantity
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('success')),
        cancel_url=request.build_absolute_uri(reverse('success')),
    )
    return redirect(session.url, 303)


def success_payment(request):
    return render(request, 'asmo/success.html')


def delete_review(request, review_id):
    del_review = ProductReview.objects.get(id=review_id)
    if request.user == request.user:
        del_review.delete()
        current_page = request.META.get('HTTP_REFERER', 'index')
        return redirect(current_page)
    return redirect('login')


def blog_del_review(request, review_id):
    del_review = BlogReview.objects.get(id=review_id)
    if request.user == request.user:
        del_review.delete()
        current_page = request.META.get('HTTP_REFERER', 'index')
        return redirect(current_page)
    return redirect('login')


