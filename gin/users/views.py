from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from users.forms import ProfileForm

@login_required
def editUser(request):
    msg = ''
    if request.method == 'POST':
      form = ProfileForm(request.POST)
      if form.is_valid():
        email = form.cleaned_data['email']
        request.user.email = email
        request.user.save()
        msg = '<p class="success">Profile Successfully Updated.</p>'
      else:
        msg = '<p class="error">Error occurred while updating profile. Please try again.</p>'
    
    form = ProfileForm()
    
    return render_to_response('users/edit.html', { 'form': form, 'msg': msg }, context_instance=RequestContext(request))

def registerUser(request):
    if request.user.is_authenticated():
        return redirect('/')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            if user is not None:
              # Add user to REGISTERED_USERS group
              default_group = Group.objects.get(pk=1)
              user.groups.add(default_group)
              user.save()
              # Log User In
              login(request, user)
              # Redirect to home page
              return redirect('/')
    else:
        form = UserCreationForm()
    
    return render_to_response('users/register.html', { 'form': form }, context_instance=RequestContext(request))
