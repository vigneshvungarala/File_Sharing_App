from django.shortcuts import render, get_object_or_404, redirect
from .models import File
from .forms import FileUploadForm

def home(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FileUploadForm()
    files = File.objects.all()
    return render(request, 'files/home.html', {'form': form, 'files': files})

def file_share(request, unique_id):
    file = get_object_or_404(File, unique_id=unique_id)
    return render(request, 'files/file_share.html', {'file': file})
