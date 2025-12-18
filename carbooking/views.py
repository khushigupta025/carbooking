from django.http import HttpResponse
from django.shortcuts import render

# def Homepage(request):
#     return HttpResponse("Hello Welcome to home page")

# def AboutPage(request):
#     return HttpResponse("Hello Welcome to about page")

# def BlogPage(request):
#     return HttpResponse("Hello Welcome to blog page")

# def ServicesPage(request):
#     return HttpResponse("Hello Welcome to services page")

# def ContactPage(request):
#     return HttpResponse("Hello Welcome to contact page")

# def PagesPage(request):
#     return HttpResponse("Hello Welcome to Pages page")

def Homepage(request):
    return render(request,"index.html")

def Aboutpage(request):
    return render(request,"about.html")

def Blogpage(request):
    return render(request,"blog.html")

def Servicepage(request):
    return render(request,"service.html")

def Contactpage(request):
    return render(request,"contact.html")

def Featurepage(request):
    return render(request,"feature.html")

def Carspage(request):
    return render(request,"cars.html")

def Teampage(request):
    return render(request,"team.html")

def Testimonialpage(request):
    return render(request,"testimonial.html")

def page404page(request):
    return render(request,"page404.html")




