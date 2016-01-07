from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.core.context_processors import csrf
# from django.views import generic


# class IndexView(generic.CreateView):
#     template_name = 'main.html'


def index(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        # password = request.POST.get('password', '')
        # user = auth.authenticate(username=username, password=password)
        user = auth.authenticate(username=username)
        if user is not None:
            auth.login(request, user)
            args['username1'] = username
            return render_to_response('main.html', args)
        else:
            args['login_error'] = 'no user'
            return render_to_response('main.html', args)
    else:
        return render_to_response('main.html', args)
