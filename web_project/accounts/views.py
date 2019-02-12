from django.shortcuts          import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth       import login , logout
from django.http               import HttpResponseRedirect , HttpResponse


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request , user)
            return HttpResponseRedirect('/admin_photos/')
    else:
        form = AuthenticationForm()
    return render(request , 'accounts/login.html' , {'form' : form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return render(request , 'homepage.html')


