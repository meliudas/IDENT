# from django.core.exceptions import *
#
# from main.models import *
#
#
# def base(request):
#     emails = Email.objects.all()
#     footer = Footer.objects.first()
#     footer_socials = Social.objects.all()
#     phones = PhoneNumber.objects.all()
#     subcategories = SubCategory.objects.all()
#
#     try:
#         places = Address.objects.get(main_place=True)
#     except ObjectDoesNotExist:
#         places = Address.objects.first()
#
#     params = {'emails': emails, 'footer': footer,
#               'footer_socials': footer_socials, 'phones': phones, 'places': places,
#               'subcategories': subcategories}
#
#     return params
