from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.template.context_processors import csrf


# from django.views import generic


# class IndexView(generic.CreateView):
#     template_name = 'main.html'


# def index(request):
#     args = {}
#     args.update(csrf(request))
#     if request.POST:
#         username = request.POST['username']
#         password = request.POST.get('password', '')
#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             args['username1'] = username
#             return render_to_response('main.html', args)
#         else:
#             args['login_error'] = 'no user'
#             return render_to_response('main.html', args)
#     else:
#         return render_to_response('main.html', args)

def index(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        cardnumber = request.POST['cardnumber']
        try:
            card = User.objects.get(username=cardnumber)
        except User.DoesNotExist:
            args['login_error'] = 'no user'
            return render_to_response('main.html', args)
        else:
            if card.is_active == 1:
                #tyt zamenit na zapis v session
                args['username1'] = card.username + ' activ'
                return render_to_response('main.html', args)
            else:
                args['username1'] = card.username + ' passiv'
                return render_to_response('main.html', args)
    else:
        return render_to_response('main.html', args)
