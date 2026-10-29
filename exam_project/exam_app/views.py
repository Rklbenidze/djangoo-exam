from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def films(request):
    films_list = [
        {'title': 'Joker', 'imdb': 8.4},
        {'title': 'Shaurma', 'imdb': 9.3},
        {'title': 'Xinkalis da Xawapuris dapirispireba', 'imdb': 9.8},
        {'title': 'Chemi cxovreba', 'imdb': 9.9},
        {'title': 'Zangebis devna', 'imdb': 10.0},
    ]
    context = {'films': films_list}
    return render(request, 'films.html', context)
