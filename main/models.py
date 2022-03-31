from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Products(models.Model):
    pass

class Slider(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Фото')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Banner(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Page(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class New(models.Model):
    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
        ordering = ['-date']

    # news = models.CharField(max_length=255, verbose_name='Название')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='news', verbose_name='Фото')
    # url = models.URLField(verbose_name='Ссылка на новость', blank=True)
    date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False, verbose_name='Актуально')

    def __str__(self):
        return self.title



class Pagephone(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')


    def __str__(self):
        return self.title


class MainPage(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Фото')

    def __str__(self):
        return self.title



class Album(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Фото')

    def __str__(self):
        return self.title



class PhotoAlbum(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название', default=True)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Фото')

    def __str__(self):
        return self.title

class ContPhone(models.Model):
    image = models.ImageField(verbose_name='Фото')


class AlbumBlog(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Фото')

    def __str__(self):
        return self.title


class Service(models.Model):

    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

# class Hashtag(models.Model):
#     title = models.CharField(max_length=255, verbose_name='Hashtag')
#
#     def __str__(self):
#         return self.title

class ServiceHelp(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title


class NewsDetail(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')
    is_active = models.BooleanField(default=False, verbose_name='Актуально')

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')


class Product(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_at']
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now=True)
    # hashtags = models.ManyToManyField(to='Hashtag')


    def __str__(self):
        return self.title

#
# class SimProduct(models.Model):
#     title = models.CharField(max_length=255, verbose_name='Название')
#     image = models.ImageField(verbose_name='Фото')
#     description = models.TextField(verbose_name='Описание')
#
#     def __str__(self):
#         return self.title
class Catalog(models.Model):
    image = models.ImageField(verbose_name="Фото")


class Category(models.Model):
    image = models.ImageField(verbose_name="Фото",)
    title = models.CharField(max_length=255, verbose_name="Название")
    desc = models.TextField(max_length=255, verbose_name="Описание")
    is_active = models.BooleanField(default=False, verbose_name="Актуально")

    def __str__(self):
        return self.title


# class Company(models.Model):
#     title = models.CharField(max_length=255, verbose_name='Название')
#     image = models.ImageField(verbose_name='Фото')
#     description = models.TextField(verbose_name='Описание')
#
#     def __str__(self):
#         return self.title


CONTACTS_CHOICES = [
        ('DC', 'Диллерские центры'),
        ('SC', 'Cервисные центры'),
    ]


class Contact(models.Model):
    # image = models.ImageField(verbose_name='Фото', default=True)
    # header = models.TextField(verbose_name='Загаловок', default=True)
    title = models.CharField(max_length=50, verbose_name='Название')
    address = models.CharField(max_length=255, verbose_name='Адрес', default='')
    number = PhoneNumberField(region='KG', verbose_name='Номер')
    email = models.EmailField(max_length=255, verbose_name='Почта', default='')
    choices = models.CharField(max_length=255, choices=CONTACTS_CHOICES)

    def __str__(self):
        return self.title


class ContactDil(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название', default='')
    address = models.CharField(max_length=255, verbose_name='Адрес', default='')
    number = PhoneNumberField( region='KG', verbose_name='Номер', default='')
    email = models.EmailField(max_length=255, verbose_name='Почта', default='')
    choices = models.CharField(max_length=255, choices=CONTACTS_CHOICES, default='')

    def __str__(self):
        return self.title