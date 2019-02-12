from django.shortcuts               import render
from django.contrib.auth.decorators import login_required
from upload.models                  import Shared_Photos
from django.http                    import HttpResponseRedirect

def homepage(request):
    return render(request , 'homepage.html')

def delete(request , id):
    photo = Shared_Photos.objects.get(id = id)
    photo.others = False
    photo.save()
    return HttpResponseRedirect('/admin_photos/')

@login_required(login_url = '/accounts/login/')
def admin_photos(request):
    photos = Shared_Photos.objects.all()
    all = {}
    for photo in photos:
        if photo.session_key in all.keys():
            all[photo.session_key].append(photo)
        else:
            all[photo.session_key] = [photo]
    return render(request , 'admin_photos.html', {'all' : all })
