from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator


class Size(models.Model):
    name = models.CharField(max_length=10, unique=True, verbose_name='Mahsulot o\'lchami')
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mahsulot o\'lchami '
        verbose_name_plural = 'Mahsulot o\'lchamlari'


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Mahsulot kategoriyasi')
    image = models.ImageField(upload_to='categories/', verbose_name='Kategoriya rasmi')
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategoriya '
        verbose_name_plural = 'Kategoriyalar'


class Color(models.Model):
    name = models.CharField(max_length=15, verbose_name='Mahsulot rangi')
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Rang '
        verbose_name_plural = 'Mahsulot ranglari'


class Brand(models.Model):
    name = models.CharField(max_length=25, verbose_name='Mahsulot brendi')
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brend '
        verbose_name_plural = 'Brendlar'


class Sort(models.Model):
    name = models.CharField(max_length=100, verbose_name='Mahsulot turi')
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tur '
        verbose_name_plural = 'Turlari'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Mahsulot nomi')
    description = models.TextField(verbose_name='Mahsulot tasnifi')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Mahsulot narxi')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Mahsulot kategoriyasi')
    image = models.ImageField(upload_to='products/', verbose_name='Mahsulot rasmi')
    image1 = models.ImageField(upload_to='products/', verbose_name='Mahsulot rasmi')
    image2 = models.ImageField(upload_to='products/', verbose_name='Mahsulot rasmi')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Mahsulot brendi')
    size = models.ManyToManyField(Size, verbose_name='Mahsulot o\'lchami', blank=True)
    color = models.ManyToManyField(Color, verbose_name='Mahsulot rangi')
    weight = models.FloatField(null=True, blank=True, verbose_name='Mahsulot og\'irligi', validators=[MinValueValidator(0.0)])
    materials = models.CharField(max_length=100, verbose_name='Mahsulot materiali')
    sort = models.ForeignKey(Sort, on_delete=models.CASCADE, verbose_name='Mahsulot turi', null=True, blank=True)
    quantity = models.IntegerField(default=0, verbose_name='Mahsulot soni')
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mahsulot '
        verbose_name_plural = 'Mahsulotlar'


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Foydalanuvchi')
    comment = models.CharField(max_length=200, verbose_name='Izoh')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Vaqt')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Mahsulot')
    rating = models.IntegerField(default=0, verbose_name='Reyting')

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Izoh '
        verbose_name_plural = 'Izohlar'


class BlogTags(models.Model):
    tag = models.CharField(max_length=50, verbose_name='Tag')
    slug = models.SlugField()

    def __str__(self):
        return f'{self.tag}'

    class Meta:
        verbose_name = 'Tag '
        verbose_name_plural = 'Teglar '


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Maqola muallifi')
    title = models.CharField(max_length=255, verbose_name='Maqola nomi')
    content = models.TextField(verbose_name='Maqola matni')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Vaqti')
    image = models.ImageField(upload_to='blog/', verbose_name='Maqola rasmi')
    tag = models.ManyToManyField(BlogTags, verbose_name='Tag')
    slug = models.SlugField()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Maqola '
        verbose_name_plural = 'Maqolalar '


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Mijoz", null=True)
    firstname = models.CharField(max_length=100, verbose_name="Ismi")
    lastname = models.CharField(max_length=100, verbose_name="Familiyasi")

    def __str__(self):
        return f"{self.user}"


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, verbose_name="Mijoz", null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Xarid vaqti")
    is_active = models.BooleanField(default=True, verbose_name="Xolat")

    def __str__(self):
        return f"{self.customer}"

    @property
    def get_cart_total_price(self):
        order_products = self.orderproduct_set.all()
        total_price = sum([product.get_cart_price for product in order_products])
        return total_price

    @property
    def get_cart_quantity(self):
        order_products = self.orderproduct_set.all()
        totat_quantity = [product.quantity for product in order_products]
        total_quantity_sum = sum(totat_quantity)
        return total_quantity_sum


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, verbose_name="Xarid", null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, verbose_name="Maxsulot", null=True)
    quantity = models.IntegerField(default=0, verbose_name="Soni")
    added = models.DateTimeField(auto_now_add=True, verbose_name="Xarid vaqti")

    def __str__(self):
        return f"{self.product}"

    @property
    def get_cart_price(self):
        total_price = self.quantity * self.product.price
        return total_price


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, verbose_name="Mijoz", null=True)
    address = models.CharField(max_length=255, verbose_name="Manzil")
    city = models.CharField(max_length=255, verbose_name="Shahar")
    district = models.CharField(max_length=50, verbose_name="Tuman")
    zipcode = models.CharField(max_length=100, verbose_name="Pochta kodi")
    mobile = models.CharField(max_length=100, verbose_name="Mobil raqami")
    email = models.EmailField(verbose_name="Email manzili", max_length=100)

    def __str__(self):
        return f"{self.customer}"


class UserProfile(models.Model):
    photo = models.ImageField(upload_to='img_users/', null=True, blank=True, verbose_name='Rasm')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Foydalanuvchi')
    first_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Ism')
    last_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Familiya')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Telefon')
    telegram = models.URLField(null=True, blank=True, verbose_name='Telegram')


    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = 'Foydalanuvchi profili'
        verbose_name_plural = 'Foydalanuvchi profillari'


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Foydalanuvchi')
    products = models.ManyToManyField(Product, verbose_name='Mahsulotlar')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqti')

    def __str__(self):
        return f"{self.user.username}'s Wishlist"

    class Meta:
        verbose_name = 'Xohish ro\'yxati'
        verbose_name_plural = 'Xohish ro\'yxatlari'


class BlogReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Foydalanuvchi')
    comment = models.CharField(max_length=200, verbose_name='Izoh')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Vaqt')
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, verbose_name='Blog')

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Blog izoh '
        verbose_name_plural = 'Blog izohlari'
