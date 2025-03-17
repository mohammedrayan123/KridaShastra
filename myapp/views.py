from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def products(request):
    return render(request, 'main/products.html')

def partnership(request):
    return render(request, 'main/partnership.html')

def resources(request):
    return render(request, 'main/resources.html')

def testimonials(request):
    return render(request, 'main/testimonials.html')

def contact(request):
    return render(request, 'main/contact.html')
