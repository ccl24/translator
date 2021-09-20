from django.shortcuts import render
from . import translate

# Create your views here.

def translator_view(request):
    if request.method == 'POST':
        original_text = request.POST['my_textarea']
        language = translate.detect(original_text)
        output = translate.translate(original_text)
        return render(request, 'translator.html', {'output_text':output, 'original_text':original_text, 'language_type':language})
    else:
        return render(request, 'translator.html')