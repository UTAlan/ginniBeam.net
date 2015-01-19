from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from contact.models import ContactForm
from recaptcha.client import captcha

def index(request):
    msg = ''
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            r = captcha.submit(request.POST['recaptcha_challenge_field'], request.POST['recaptcha_response_field'], settings.RECAPTCHA_PRIVATE_KEY, request.META['REMOTE_ADDR'])
            if not r.is_valid:
                #return redirect('/contact/') # Invalid form entry
                msg = '<p class="error">Invalid Captcha. Please try again.</p>'
            else:
                # Process the data in form.cleaned_data
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                message = form.cleaned_data['message']
                recipients = ['vtbeam@gmail.com', 'alan@alanbeam.net']
                
                send_mail('Contact Message From ' + name + ' (' + email + ') - ginnibeam.net', message, email, recipients)
                
                msg = '<p class="success">Message successfully sent.</p>'
                form = ContactForm()
    else:
        form = ContactForm() # An unbound form
        
    return render_to_response('contact/index.html', { 'form': form, 'msg': msg }, context_instance=RequestContext(request))
