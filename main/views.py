from django.db.models import Q
from django.shortcuts import render
# from django.utils.text import Truncator

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
    context = {"sliders":sliders,"banner":banner, "page":page, "new":new,"mainpage":mainpage,"album":album,"photoalbum":photoalbum,
               'albumblog':albumblog,"pagephone":pagephone}
    return render(request, 'index.html', context)



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
    context = {"about":about}
    return render(request, 'about.html', context)


def service(request):
    service = Service.objects.all()
    servicehelp = ServiceHelp.objects.all()
    context = {"service":service,"servicehelp":servicehelp }
    return render(request, 'service.html',context)


def contact(request):
    contacts = Contact.objects.all()
    contactdils = ContactDil.objects.all()
    contphone = ContPhone.objects.all()
    context = {"contacts":contacts,"contactdils":contactdils, "contphone":contphone }
    return render(request, 'contacts.html', context)

def catalog(request):
    catalog = Catalog.objects.all()
    category = Category.objects.all()
    context = {"category":category, "catalog":catalog}
    return render(request, 'catalog.html', context)


def product_inner(request):
    product = Product.objects.all()
    context = {"product":product}
    return render(request, 'product-inner.html', context)


def news(requst):
    news = New.objects.filter(is_active=True)[:4]
    context = {"news":news}
    return render(requst, 'news.html', context)


def news_detail(requst, pk):
    # new = New.objects.filter(is_active=True)[:4]
    news_detail = New.objects.get(pk=pk)
    context = {"news_detail":news_detail}
    return render(requst, 'newsdetail.html', context)

