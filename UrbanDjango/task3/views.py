from django.shortcuts import render

# Create your views here.
def platform(request):
    return render(request, 'third_task/platform.html')

def book(request):
    title = "Магазин"
    text = "Каталог книг"
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'third_task/book.html', context)

def cart(request):
    return render(request, 'third_task/cart.html')