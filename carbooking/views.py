from django.http import HttpResponse
from django.shortcuts import render,redirect
from car_admin.models import Service,Cat,Centalprocess,Blog,Numbering,Reviews,Centalfeatures,HeroForm,contactsform

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
    if request.method =="POST":
        HeroForm.objects.create(
            car_type=request.POST.get('car_type'),
            pickup_location=request.POST.get('pickup_location'),
            drop_location=request.POST.get('drop_location'),
            pickup_date=request.POST.get('pickup_date'),
            pickup_time=request.POST.get('pickup_time'),
            drop_date=request.POST.get('drop_date'),
            drop_time=request.POST.get('drop_time'),
        )
        return redirect('success')
    

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
    if request.method =="POST":
        contactsform.objects.create(
            your_name=request.POST.get('your_name'),
            email=request.POST.get('email'),
            your_phone=request.POST.get('your_phone'),
            your_projects=request.POST.get('your_projects'),
            subjects=request.POST.get('subjects'),
            msg=request.POST.get('msg')
        )
        return redirect('contact')
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

def successpage(request):
    return render(request,"success.html")







