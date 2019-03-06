from django.shortcuts import render
import operator
# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionart = {}

    for word in words:
        if word in word_dictionart:
            word_dictionart[word] += 1
        else:
            word_dictionart[word] = 1
    return render(request, 'result.html', {'full': text, 'total': len(words), 'dictionary': word_dictionart.items()})
