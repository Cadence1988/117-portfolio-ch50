from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def test_view(request):
    return render(request, "pages/test.html")

def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    if request.method == "POST":
        # Send the message
        form = ContactForm(request.POST)

        if form.is_valid():
            print('sending email')

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            full_message = f"This is an email from your portfolio page\nName:{name}\nEmail:{email}\nmessage{message}"

            send_mail(
            "email from" + name,
            full_message,
            email,
            ['sinzunza@sdgku.edu']
            )

            print('Email sent')

            # send the user to thank you page

        else:
            print('Invalid data on the form')

    else:
        # display page
        form = ContactForm()
    
    return render(request, "pages/contact.html", {'form': form})