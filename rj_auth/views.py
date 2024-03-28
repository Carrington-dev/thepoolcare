from django import forms
from django.shortcuts import render, redirect
from contact.forms import ContactForm
from django.contrib import messages

# Create your views here.
def home(request):
    context = {
        'title' : "Pool Masters"
    }
    form = ContactForm()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # subject = form.cleaned_data['subject']
            # email = form.cleaned_data['email']
            # name = form.cleaned_data['name']
            # message = form.cleaned_data['message']
            form.save()

            

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            messages.success(request,f"Your message has been sent. Thank you!")
            return redirect('home')

    # if a GET (or any other method) we'll create a blank form
    else:
        # form = ContactForm()
        context['form'] = ContactForm()

    # return render(request, 'name.html', {'form': form})
    
    return render(request, "index.html") 