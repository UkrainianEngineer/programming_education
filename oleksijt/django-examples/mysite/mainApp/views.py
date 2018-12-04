from django.shortcuts import render


def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    return render(request, 'mainApp/basic.html', {'values': [
        'Якщо у вас виникли питання, звертайтесь за телефоном:',
        '+380(50)123 45 67',
        '123@123.com'
        ]})
