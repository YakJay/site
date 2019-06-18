from django.shortcuts import render

# Create your views here.
def index(request):
    template_name = "accounts/index.html"
    args = {}
    return render(request, template_name,args)


# Create your views here.
def services(request):
    template_name = "accounts/services.html"
    args = {}
    return render(request, template_name,args)

    #Views for About Page
def about(request):
    template_name = "accounts/about.html"
    args = {}
    return render(request, template_name,args)

  #Views For Contact Page
def contact(request):
    template_name = "accounts/contact.html"
    args = {}
    return render(request, template_name,args)

      #Views For Tutorials Page
def tutorials(request):
    template_name = "accounts/tutorials.html"
    args = {}
    return render(request, template_name,args)

    #Views For Blog Page
def blog(request):
    template_name = "accounts/blog.html"
    args = {} 
    return render(request,template_name,args)

    #Base Page
#def base(request):
    #template_name = "accounts/base.html"
    #args = {} 
    #return render(request,template_name,args)