from django.core.mail import send_mail
from django.shortcuts import redirect
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    card_data = [
        {"slno":"1","title": "Athlete Success", "description": "Athletes benefiting from Krida Shastra's solutions.", "offset": -2 * 80},
        {"slno":"2","title": "Data-Driven", "description": "Quantitative data showcasing performance improvements.", "offset": -1 * 80},
        {"slno":"3","title": "Endorsements", "description": "Testimonials from coaches and organizations.", "offset": 0},
        {"slno":"4","title": "Indian Hockey Team", "description": "12% improvement in endurance (2024).", "offset": 1 * 80},
    ]
    return render(request, "main/index.html", {"card_data": card_data})


def school(request):
    return render(request, 'main/school.html')

def services(request):
    return render(request, 'main/services.html')

def products(request):
    return render(request, 'main/products.html')

def partnership(request):
    return render(request, 'main/partnership.html')

def resources(request):
    return render(request, 'main/resources.html')

def request_info(request):
    if request.method == 'POST':
        product = request.POST.get('product')
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"""
        Product: {product}
        Name: {name}
        Email: {email}
        Message: {message}
        """

        send_mail(
            subject=f"Info Request: {product}",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['irfan@kridasashtra.com'],  # Replace with your email
            fail_silently=False,
        )

        return HttpResponse("<h2>Thanks! Your request has been submitted.</h2><a href='/'>Back</a>")

def contact(request):
    return render(request, 'main/contact.html')


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        company = request.POST.get('company')
        business_type = request.POST.get('business_type')
        message = request.POST.get('message')

        full_message = f"""
        New Business Inquiry:

        Name: {name}
        Email: {email}
        Phone: {phone}
        Company: {company}
        Business Type: {business_type}
        Message: {message}
        """

        send_mail(
            subject="New Business Inquiry",
            message=full_message,
            from_email="irfan@kridasashtra.com",
            recipient_list=["irfan@kridasashtra.com"],
            fail_silently=False,
        )

        messages.success(request, "Thank you! Your inquiry has been submitted.")
        return redirect(request.path)

    return render(request, 'contact.html')


def submit_contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']

        # Compose email message
        message = f"""
        New Contact Submission:

        Name: {name}
        Email: {email}
        Phone: {phone}
        """

        send_mail(
            subject="New Contact Form Submission",
            message=message,
            from_email="irfan@kridasashtra.com",
            recipient_list=["irfan@kridasashtra.com"],
            fail_silently=False,
        )

        return redirect('thank_you')

    return redirect('/')  # fallback

def thank_you(request):
    return render(request, 'main/thank_you.html')