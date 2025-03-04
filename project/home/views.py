from django.shortcuts import render
from django.http import HttpResponse

# Create your views here:

def index(request):
    # response = HttpResponse()
    # response.writelines("<h1>Home Page</h1>")     # This is a simple way to write HTML code in Django
    # response.write("<p>Welcome to the Home Page of the Django Study Project</p>")
    # response.write("Nguyen Minh Duc")
    # return response
    return render(request, 'pages/home.html')
    # return HttpResponse("<h1>Home Page</h1><p>Welcome to the Home Page of the Django Study Project</p>")
