# Generated by Django 5.0.6 on 2024-05-15 09:30

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50, verbose_name='Tag')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Tag ',
                'verbose_name_plural': 'Teglar ',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Mahsulot brendi')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Brend ',
                'verbose_name_plural': 'Brendlar',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Mahsulot kategoriyasi')),
                ('image', models.ImageField(upload_to='categories/', verbose_name='Kategoriya rasmi')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Kategoriya ',
                'verbose_name_plural': 'Kategoriyalar',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Mahsulot rangi')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Rang ',
                'verbose_name_plural': 'Mahsulot ranglari',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True, verbose_name="Mahsulot o'lchami")),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': "Mahsulot o'lchami ",
                'verbose_name_plural': "Mahsulot o'lchamlari",
            },
        ),
        migrations.CreateModel(
            name='Sort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Mahsulot turi')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Tur ',
                'verbose_name_plural': 'Turlari',
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Maqola nomi')),
                ('content', models.TextField(verbose_name='Maqola matni')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Vaqti')),
                ('image', models.ImageField(upload_to='blog/', verbose_name='Maqola rasmi')),
                ('slug', models.SlugField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Maqola muallifi')),
                ('tag', models.ManyToManyField(to='asmo.blogtags', verbose_name='Tag')),
            ],
            options={
                'verbose_name': 'Maqola ',
                'verbose_name_plural': 'Maqolalar ',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Mahsulot nomi')),
                ('description', models.TextField(verbose_name='Mahsulot tasnifi')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Mahsulot narxi')),
                ('image', models.ImageField(upload_to='products/', verbose_name='Mahsulot rasmi')),
                ('image1', models.ImageField(upload_to='products/', verbose_name='Mahsulot rasmi')),
                ('image2', models.ImageField(upload_to='products/', verbose_name='Mahsulot rasmi')),
                ('weight', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name="Mahsulot og'irligi")),
                ('materials', models.CharField(max_length=100, verbose_name='Mahsulot materiali')),
                ('quantity', models.IntegerField(default=0, verbose_name='Mahsulot soni')),
                ('slug', models.SlugField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asmo.brand', verbose_name='Mahsulot brendi')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asmo.category', verbose_name='Mahsulot kategoriyasi')),
                ('color', models.ManyToManyField(to='asmo.color', verbose_name='Mahsulot rangi')),
                ('size', models.ManyToManyField(blank=True, to='asmo.size', verbose_name="Mahsulot o'lchami")),
                ('sort', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asmo.sort', verbose_name='Mahsulot turi')),
            ],
            options={
                'verbose_name': 'Mahsulot ',
                'verbose_name_plural': 'Mahsulotlar',
            },
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200, verbose_name='Izoh')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Vaqt')),
                ('rating', models.IntegerField(default=0, verbose_name='Reyting')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asmo.product', verbose_name='Mahsulot')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
            ],
            options={
                'verbose_name': 'Izoh ',
                'verbose_name_plural': 'Izohlar',
            },
        ),
    ]
