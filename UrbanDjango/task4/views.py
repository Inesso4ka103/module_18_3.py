from django.shortcuts import render


# Create your views here.
def platform(request):
    return render(request, 'fourth_task/platform.html')


def book(request):
    books = [
        "М.А. Булгаков Мастер и Маргарита",
        "М.Ф. Достоевский Преступление и наказание",
        "Л.Н.Толстой Война и мир"
    ]
    context = {
        'books': books
    }
    return render(request, 'fourth_task/book.html', context)


def cart(request):
    return render(request, 'fourth_task/cart.html')

def menu(request):
    return render(request, 'fourth_task/menu.html')
