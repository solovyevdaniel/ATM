from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.template.context_processors import csrf


def index(request):
    args = {}
    args.update(csrf(request))
    if request.GET:
        cardnumber = request.GET['cardnumber']
        try:
            card = User.objects.get(username=cardnumber)
        except User.DoesNotExist:
            args['login_error'] = 'no user in db'
            return render_to_response('main.html', args)
        else:
            if card.is_active:
                # session or arg?
                request.session.set_expiry(30)
                request.session['card_number'] = card.username
                return redirect('auth/')
            else:
                args['username'] = card.username + ' deactivated'
                return render_to_response('main.html', args)
    else:
        return render_to_response('main.html', args)


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.session.get('card_number')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            args['username'] = username + 'logged in'
            return render_to_response('login.html', args)
        else:
            args['login_error'] = 'no user'
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html')
