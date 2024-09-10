from django.shortcuts import render

def show_main(request):
    context = {
        'app_name' : 'Top Up Diamond Mobil Legen Murah',
        'name': 'Flori Andrea Ng',
        'class': 'KKI'
    }

    return render(request, "main.html", context)
