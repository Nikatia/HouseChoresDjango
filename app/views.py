from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import ChoreType, Chore, ChoreDone
from django.contrib.auth.models import User


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


#ChoreTypes
def chore_type_listview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        choretypelist = ChoreType.objects.all()
        context = {'types': choretypelist}
        return render(request, 'choretypes.html', context)

def add_chore_type(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        name = request.POST['name']
        desc = request.POST['description']
        ChoreType(name = name, description = desc).save()
        return redirect(request.META['HTTP_REFERER'])

def confirm_delete_chore_type(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        type = ChoreType.objects.get(id = id)
        chorelist = Chore.objects.all()
        context = {'type': type, 'chores': chorelist}
        return render (request, "confirm_delete_chore_type.html", context)

def delete_chore_type(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        ChoreType.objects.get(id = id).delete()
        return redirect(chore_type_listview)

def edit_chore_type_get(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        type = ChoreType.objects.get(id = id)
        context = {'type': type}
        return render (request, "edit_chore_type.html", context)

def edit_chore_type_post(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        type = ChoreType.objects.get(id = id)
        type.name = request.POST['name']
        type.description = request.POST['description']
        type.save()
        return redirect(chore_type_listview)


#Chores
def chore_listview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        chorelist = Chore.objects.all()
        choretypelist = ChoreType.objects.all()
        context = {'chores': chorelist, 'types': choretypelist}
        return render(request, 'chores.html', context)

def search_chores(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        search = request.POST['search']
        filtered = Chore.objects.filter(name__icontains=search)
        choretypelist = ChoreType.objects.all()
        context = {'chores': filtered, 'types': choretypelist}
        return render (request, "chores.html", context)

def add_chore(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        name = request.POST['name']
        type = request.POST['type']
        Chore(name = name, type = ChoreType.objects.get(id = type)).save()
        return redirect(request.META['HTTP_REFERER'])

def confirm_delete_chore(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        chore = Chore.objects.get(id = id)
        context = {'chore': chore}
        return render (request, "confirm_delete_chore.html", context)

def delete_chore(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        Chore.objects.get(id = id).delete()
        return redirect(chore_listview)
    
def edit_chore_get(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        chore = Chore.objects.get(id = id)
        choretypelist = ChoreType.objects.all()
        context = {'chore': chore, 'types': choretypelist}
        return render (request, "edit_chore.html", context)

def edit_chore_post(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        chore = Chore.objects.get(id = id)
        chore.name = request.POST['name']
        type = request.POST['type']
        chore.type = ChoreType.objects.get(id = int(type))
        chore.save()
        return redirect(chore_listview)

def chores_of_type(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        type = ChoreType.objects.get(id = id)
        chorelist = Chore.objects.all()
        filteredchores = chorelist.filter(type = id)
        context = {'chores': filteredchores, 'type': type}
        return render (request, "categorys_chores.html", context)
    

#Chore Diary
def diary_listview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        choresdone = ChoreDone.objects.all()
        chorelist = Chore.objects.all()
        context = {'diary': choresdone, 'chores': chorelist}
        return render(request, 'diary.html', context)

def add_diary_entry(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        date = request.POST['date']
        duration = request.POST['duration']
        chore = request.POST['chore']
        who = request.user.id

        ChoreDone(date = date, duration = duration, chore = Chore.objects.get(id = chore), person = User.objects.get(id=who)).save()
        return redirect(request.META['HTTP_REFERER'])

def confirm_delete_diary_entry(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        diaryentry = ChoreDone.objects.get(id = id)
        context = {'entry': diaryentry}
        return render (request, "confirm_delete_diary_entry.html", context)

def delete_diary_entry(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        ChoreDone.objects.get(id = id).delete()
        return redirect(diary_listview)
    
def edit_diary_entry_get(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        entry = ChoreDone.objects.get(id = id)
        chorelist = Chore.objects.all()
        users = User.objects.all()
        context = {'entry': entry, 'chores': chorelist, 'users': users}
        return render (request, "edit_diary_entry.html", context)

def edit_diary_entry_post(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        
        entry = ChoreDone.objects.get(id = id)
        entry.date = request.POST['date']
        entry.duration = request.POST['duration']
        chore = request.POST['chore']
        entry.chore = Chore.objects.get(id = int(chore))
        user = request.POST['person']
        entry.person = User.objects.get(id=user)
        entry.save()
        return redirect(diary_listview)

#Users
def user_listview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        users = User.objects.all()
        context = {'users': users}
        return render(request, 'users.html', context)
    
def add_user(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        username = request.POST['username']
        name = request.POST['first_name']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username = username, first_name = name, email=email, password=password)
        user.save()
        return redirect(request.META['HTTP_REFERER'])

def confirm_delete_user(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        user = User.objects.get(id = id)
        context = {'user': user}
        return render (request, "confirm_delete_user.html", context)

def delete_user(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        User.objects.get(id = id).delete()
        return redirect(user_listview)
    
def edit_user_get(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        user = User.objects.get(id = id)
        context = {'user': user}
        return render (request, "edit_user.html", context)

def edit_user_post(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        user = User.objects.get(id = id)
        user.username = request.POST['username']
        user.first_name = request.POST['first_name']
        user.email = request.POST['email']
        password = request.POST['password']
        user.set_password(password)
        user.save()
        return redirect(user_listview)