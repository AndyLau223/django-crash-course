from django.shortcuts import render
from googletrans import Translator
# Create your views here.

translator = Translator()

def translator_view(request):
    if request.method == 'POST':
        original_text = request.POST['my_textarea']
        output = translator.translate(text=original_text, dest="zh-cn").text
        return render(request, 'translator.html',
                      {'output_text': output, 'original_text': original_text})
    else:
        return render(request, 'translator.html')
