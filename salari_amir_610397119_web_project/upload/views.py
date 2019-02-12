from django.shortcuts import render
from django.http      import HttpResponse , Http404
from django.http      import HttpResponseRedirect
from .forms           import UploadFileForm
from .models          import Photo , Shared_Photos
from PIL              import Image
from django.conf      import settings


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST , request.FILES)
        if form.is_valid():
            instance = Photo(File = request.FILES['your_photo'])
            instance.save()
            return HttpResponseRedirect('/upload/edit/' +  str(instance.id) + '/')
        else:
            return HttpResponse(form.errors)
    else:
        return render(request , 'upload/upload.html' )

def edit(request , id):
    photo    = Photo.objects.get(id = id)
    mediaIns = photo.edit()
    width    = mediaIns.width
    height   = mediaIns.height
    
    return render(request , 'upload/edit.html' , {'url' : photo.File.url , 'id' : id , 'max_width' : width ,  'max_height' : height})

def resize(request , id):
    width    = int(request.POST.get("width"))
    height   = int(request.POST.get("height"))
    mediaIns = Photo.objects.get(id = id)
    photo    = mediaIns.edit()
    photo    = photo.resize((width , height)) 
    photo.save(str(settings.MEDIA_ROOT) + "/" + str(mediaIns.File))
    
    return HttpResponseRedirect('/upload/edit/' +  str(mediaIns.id) + '/')

def black_and_white(request , id):
    mediaIns = Photo.objects.get(id = id)
    photo    = mediaIns.edit()
    photo    = photo.convert("L")
    photo.save(str(settings.MEDIA_ROOT) + "/" + str(mediaIns.File))
    
    return HttpResponseRedirect('/upload/edit/' +  str(mediaIns.id) + '/')

def rotate(request , id):
    degree   = int(request.POST.get('degree'))
    mediaIns = Photo.objects.get(id = id)
    photo    = mediaIns.edit()
    photo    = photo.rotate(degree)
    print(str(settings.MEDIA_ROOT) + "/" + str(mediaIns.File))
    photo.save(str(settings.MEDIA_ROOT) + "/" + str(mediaIns.File))
    
    return HttpResponseRedirect('/upload/edit/' +  str(mediaIns.id) + '/')

def crop(request , id):
    Left  = int(request.POST.get("Left"))
    Right = int(request.POST.get("Right"))
    Upper = int(request.POST.get("Upper"))
    Lower = int(request.POST.get("Lower"))
    if not(Left < Right) or not(Lower > Upper):
        
        return render(request , 'upload/crop.html')

    mediaIns = Photo.objects.get(id = id)
    photo    = mediaIns.edit()
    photo    = photo.crop((Left , Upper , Right , Lower))
    photo.save(str(settings.MEDIA_ROOT) + "/" + str(mediaIns.File))

    return HttpResponseRedirect('/upload/edit/' +  str(mediaIns.id) + '/')

def share(request , id):
    if request.session.session_key == None:
        request.session.create()
    photo = Photo.objects.get(id = id)
    instance = Shared_Photos(
        shared_photos = photo.File ,
        session_key = request.session.session_key
        )
    instance.save()

    return render(request , 'upload/shared.html' ,  {'url' : photo.File.url })