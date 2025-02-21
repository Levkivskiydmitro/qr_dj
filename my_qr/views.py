from django.shortcuts import render, redirect
from django.http import FileResponse, Http404
import os
from django.conf import settings
from gen_qr.models import QR 

def render_my_qr(request):
    qrcodes = QR.objects.all()
    
    if request.method == "POST":
        for key in request.POST:
            if key.startswith("del-"):
                qr_id = key.split("-")[1]
                QR.objects.filter(pk=qr_id).delete()
                return redirect('my_qr')
            
    if "download_local" in request.GET:
        qr_id = request.GET.get("download_local")
        qr = QR.objects.filter(pk=qr_id).first()
        if qr and qr.image:
            file_path = os.path.join(settings.MEDIA_ROOT, str(qr.image))
            if os.path.exists(file_path):
                return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))
            else:
                raise Http404("Файл не найден")
    
    return render(request, 'qr.html', context={'qrs': qrcodes})


