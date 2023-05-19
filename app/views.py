from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Main page
def landingview(request):
    return render(request, 'landingpage.html')

#Login
def loginview(request):
    return render (request, "loginpage.html")

def login_action(request):
    user = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username = user, password = password)
    if user is not None:
        login(request, user)
        context = {'name': user}
        return render(request, 'landingpage.html', context)
    else:
        return render(request, 'loginerror.html')
    
def logout_action(request):
    logout(request)
    return render(request, 'leavingpage.html')
