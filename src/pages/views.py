from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact Page</h1>")
    return render(request, 'contact.html', {})


def about_view(request, *args, **kwargs):
    my_context = {
        "title": "This is about us",
        "my_number": 123,
        "my_list": [32423, 23423, 312, 'abc'],
        "my_html": "<h1>Hello World!</h1>"
    }
    return render(request, 'about.html', my_context)
