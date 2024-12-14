from django.shortcuts import render

import qrcode
import os

# Create your views here.
def render_gen_qr(request):
    if request.method == "POST":
        url = request.POST.get("url")
        if url:
            os.makedirs('qrcodes', exist_ok=True)

            existing_files = os.listdir('qrcodes')
            next_number = len(existing_files) + 1

            path = os.path.join('qrcodes', f"qr_code_{next_number}.png")

            qr = qrcode.make(url)
            qr.save(path)

    return render(request, 'gen.html')