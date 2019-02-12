from django.shortcuts import render
from upload.models    import Shared_Photos


def show(request):
    photos = Shared_Photos.objects.all()
    if photos == '':
        return render(request , 'shared_photos/nothing.html')
    else:
        return render(request , 'shared_photos/show.html' , {'photos' : photos})
