from django.shortcuts import render_to_response, redirect, render, HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.template.context_processors import csrf

def index(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        cardnumber = request.POST['cardnumber']
        try:
            card = User.objects.get(username=cardnumber)
        except User.DoesNotExist:
            args['login_error'] = 'no user in db'
            return render(request, 'main.html', args)
        else:
            if card.is_active:
                # session or arg?
                resp = redirect('auth/')
                resp.set_cookie('card_number', card.username, max_age=30000)
                return resp
            else:
                args['username'] = card.username + ' deactivated'
                return render(request, 'main.html', args)
    else:
        return render(request, 'main.html', args)


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.COOKIES.get('card_number')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            args['username'] = username + 'logged in'
            return render(request,'login.html', args)
        else:
            args['login_error'] = 'no user'
            return render(request, 'login.html', args)
    else:
        return render(request, 'login.html')
