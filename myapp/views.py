from django.shortcuts import render
def index(request):
    card_data = [
        {"slno":"1","title": "Athlete Success", "description": "Athletes benefiting from Krida Shastra's solutions.", "offset": -2 * 80},
        {"slno":"2","title": "Data-Driven", "description": "Quantitative data showcasing performance improvements.", "offset": -1 * 80},
        {"slno":"3","title": "Endorsements", "description": "Testimonials from coaches and organizations.", "offset": 0},
        {"slno":"4","title": "Indian Hockey Team", "description": "12% improvement in endurance (2024).", "offset": 1 * 80},
    ]
    return render(request, "main/index.html", {"card_data": card_data})


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
