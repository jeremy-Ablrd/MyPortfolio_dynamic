from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # --- send email notification --- #
            # subject = 'Contact form submission'
            # message = 'Name: {}\nEmail: {}\nMessage: {}'.format(
            #     form.cleaned_data['name'],
            #     form.cleaned_data['email'],
            #     form.cleaned_data['message']
            # )
            # send_mail(
            #     subject,
            #     message,
            #     settings.DEFAULT_FROM_EMAIL,
            #     ['j.abelard13@gmail.com'],
            #     fail_silently=False,
            # )

            return redirect('/contact/success')
    
    else:
        form = ContactForm() # mettre text non valid ?
    
    return render(request, 'contact/formulaire.html',{'form': form})

def contact_success(request):
    return render(request, 'contact/formulaire_success.html')
