from django.shortcuts import render, HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def analyzer1(request):
    text = request.GET.get('text', 'default')

    # variable declaritions
    removepunc = request.GET.get('removepunc', 'off')
    uppercase = request.GET.get('upper', 'off')
    lineremove = request.GET.get('lineremove', 'off')
    spaceremove = request.GET.get('spaceremove', 'off')

    # function for remove extra punctuation
    if removepunc == "on":
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_`'''
        analyzed = ""
        for char in text:
            if char not in punc:
                analyzed = analyzed+char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        # return render(request, 'analyzer1.html', params)
        text = analyzed

    # function for Upper case conversion
    if(uppercase == "on"):
        analyzed = ""
        for char in text:
            analyzed = analyzed+char.upper()

            params = {'purpose': 'Changement of letters in CapitalLetter',
                      'analyzed_text': analyzed}
        # return render(request, 'analyzer1.html', params)
        text = analyzed

    # function for remove extra lines
    if(lineremove == "on"):
        analyzed = ""
        for char in text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

                params = {'purpose': 'Extra line has been removed',
                          'analyzed_text': analyzed}
            # return render(request, 'analyzer1.html', params)
        text = analyzed

    # function for remove extraa spaces
    if(spaceremove == "on"):
        analyzed = ""
        for index, char in enumerate(text):
            if text[index] == " " and text[index+1] == " ":
                pass
            else:
                analyzed = analyzed+char
        params = {'purpose': 'Extra Spaces has been removed',
                  'analyzed_text': analyzed}

    # if none of the button are onn
    if removepunc != "on" and uppercase != "on" and lineremove != "on" and spaceremove != "on":
        text = request.GET.get('text', 'default')

        params = {'purpose': 'None of the operation are done',
                  'analyzed_text': text}
        return render(request, 'analyzer1.html', params)

    return render(request, 'analyzer1.html', params)
