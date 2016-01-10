from django.shortcuts import redirect, render
from django.contrib import auth
from django.template.context_processors import csrf
from ATM.models import CustomUser


def index(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        card_number = request.POST['card_number']
        try:
            card = CustomUser.objects.get(username=card_number)
        except CustomUser.DoesNotExist:
            args['login_error'] = 'no user in db'
            return render(request, 'main.html', args)
        else:
            if card.is_active:
                resp = redirect('auth/')
                request.session.set_expiry(900)
                request.session['card_number'] = card.username
                # resp.set_cookie('card_number', card.username, max_age=30000)
                return resp
            else:
                args['card_number'] = card.username
                return render(request, 'error.html', args)
    else:
        return render(request, 'main.html', args)


def login(request):
    args = {}
    args.update(csrf(request))
    if request.session.get('card_number') is None:
        resp = redirect('/')
        return resp
    if request.POST:
        # username = request.COOKIES.get('card_number')
        username = request.session.get('card_number')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        card = CustomUser.objects.get(username=request.session.get('card_number'))
        if user is not None:
            auth.login(request, user)
            args['username'] = username + 'logged in'
            card.quantity_login = 0
            card.save()
            # del request.session['card_number']
            return render(request, 'operations.html', args)
        else:
            if card.quantity_login <= 2:
                card.quantity_login += 1
                card.save()
                args['login_error'] = 'Incorrect password. Try again. You have ' + str(
                        3 - card.quantity_login) + ' attempts'
                return render(request, 'login.html', args)
            else:
                card.is_active = False
                card.save()
                del request.session['card_number']
                args['card_number'] = card.username
                return render(request, 'error.html', args)
    else:
        return render(request, 'login.html')
