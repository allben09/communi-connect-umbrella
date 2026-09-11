from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Organization, Donation, ContactMessage


def home(request):
    orgs = Organization.objects.filter(is_active=True)[:6]
    context = {
        'orgs': orgs,
        'total_orgs': Organization.objects.filter(is_active=True).count(),
        'total_donations': Donation.objects.count(),
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def programmes(request):
    return render(request, 'programmes.html')


def members(request):
    orgs = Organization.objects.filter(is_active=True)
    return render(request, 'members.html', {'orgs': orgs})


def donate(request):
    if request.method == 'POST':
        try:
            Donation.objects.create(
                donor_name=request.POST.get('name'),
                donor_email=request.POST.get('email'),
                amount=request.POST.get('amount'),
                message=request.POST.get('message', ''),
                is_anonymous=request.POST.get('anonymous') == 'on',
            )
            messages.success(request, 'Thank you for your generous donation! 💚')
            return redirect('donate')
        except Exception as e:
            messages.error(request, f'Error: {e}')
    return render(request, 'donate.html')


def contact(request):
    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
        )
        messages.success(request, 'Message sent! We will respond soon. 🙏')
        return redirect('contact')
    return render(request, 'contact.html')
