from django.http import HttpResponse
from django.shortcuts import render
from car_admin.models import Service,Cat,Centalprocess,Blog,Numbering,Reviews,Centalfeatures

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
    serviceData=Service.objects.all()
    CatData=Cat.objects.all()
    CentalprocessData=Centalprocess.objects.all()
    BlogData=Blog.objects.all()
    NumberingData=Numbering.objects.all()
    ReviewsData=Reviews.objects.all()
    CentalfeaturesData=Centalfeatures.objects.all()
    data={
        'service_show':serviceData,
        'cat_show':CatData,
        'pro_show':CentalprocessData,
        'blog_show':BlogData,
        'num_show': NumberingData,
        'review_show':ReviewsData,
        'feat_show':CentalfeaturesData,
    }
    return render(request,"index.html",data)

def Aboutpage(request):
    NumberingData=Numbering.objects.all()
    CentalprocessData=Centalprocess.objects.all()
    data={
        'num_show': NumberingData,
        'pro_show':CentalprocessData,
    }
    return render(request,"about.html",data)

def Blogpage(request):
    BlogData=Blog.objects.all()
    NumberingData=Numbering.objects.all()
    data={
        'blog_show':BlogData,
        'num_show': NumberingData, 
     }
    return render(request,"blog.html",data)

def Servicepage(request):
    serviceData=Service.objects.all()
    NumberingData=Numbering.objects.all()
    ReviewsData=Reviews.objects.all()
    data={
        'service_show':serviceData,
        'num_show': NumberingData,
        'review_show':ReviewsData,
    }
    return render(request,"service.html",data)

def Contactpage(request):
    return render(request,"contact.html")

def Featurepage(request):
    NumberingData=Numbering.objects.all()
    data={
        'num_show': NumberingData,
    }
    return render(request,"feature.html",data)

def Carspage(request):
    CatData=Cat.objects.all()
    CentalprocessData=Centalprocess.objects.all()
    data={
        'cat_show':CatData,
        'pro_show':CentalprocessData,
    }
    return render(request,"cars.html",data)

def Teampage(request):
    return render(request,"team.html")

def Testimonialpage(request):
    ReviewsData=Reviews.objects.all()
    data={
        'review_show':ReviewsData,
    }
    return render(request,"testimonial.html",data)

def page404page(request):
    return render(request,"page404.html")




