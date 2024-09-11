from django.shortcuts import render

def show_main(request):
    context = {
        'app_name' : 'Upcycle Shop',
        'name': 'Flori Andrea Ng',
        'class': 'KKI'
    }

    return render(request, "main.html", context)
