from django.http import HttpResponse


def home_page(request):
    print("home pge requested");
    return HttpResponse("<h1>This is home page</h1>")