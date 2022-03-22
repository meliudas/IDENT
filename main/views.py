from django.db.models import Q
from django.shortcuts import render
# from django.utils.text import Truncator
from django.utils.text import Truncator

from main.models import *


def index(request):
    sliders = Slider.objects.all()
    banner = Banner.objects.filter(is_active=True).get()
    page = Page.objects.all()
    new = New.objects.filter(is_active=True)[:4]
    mainpage = MainPage.objects.all()
    album = Album.objects.all()
    photoalbum = PhotoAlbum.objects.all()
    albumblog = AlbumBlog.objects.all()
    pagephone = Pagephone.objects.all()
    return render(request, 'index.html', locals())



def search(request):
    news = New.objects.filter(is_active=True)[:4]
    # search_box = request.GET.get("search-box", None)
    results = []
    if request.method == "GET":
        query = request.GET.get('query')
        results = New.objects.filter(Q(title__istartswith=query) | Q(title__icontains=query)
                                     | Q(title__iendswith=query) | Q(description__istartswith=query)
                                     | Q(description__icontains=query) | Q(description__iendswith=query))
    return render(request, 'search.html', locals())


# TODO чтоб работали пробелы в поиске


def about(request):
    about = About.objects.all()
    return render(request, 'about.html', locals())

def service(request):
    service = Service.objects.all()
    servicehelp = ServiceHelp.objects.all()
    return render(request, 'service.html',locals())

def contact(request):
    contacts = Contact.objects.all()
    contactdils = ContactDil.objects.all()
    contphone = ContPhone.objects.all()
    return render(request, 'contacts.html', locals())

def catalog(request):
    return render(request, 'catalog.html')

def product_inner(request):
    product = Product.objects.all()
    return render(request, 'product-inner.html', locals())



def news(requst):
    news = New.objects.filter(is_active=True)[:4]

    return render(requst, 'news.html', locals())

def news_detail(requst, pk):
    # new = New.objects.filter(is_active=True)[:4]

    news_detail = New.objects.get(pk=pk)
    return render(requst, 'newsdetail.html', locals())

