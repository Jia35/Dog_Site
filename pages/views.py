from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone

from stores.models import Alluser, Dogs, GPSs, Message, KeyM, Reservation
from pages.forms import UserForm

from django.core.serializers.json import DjangoJSONEncoder
import json
import datetime
import time


def about(request):
    return render(request, 'pages/about.html', locals())


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_active:
            auth.login(request, user)
            return render(request, 'pages/about.html', locals())
        else:
            error_message = "帳號或密碼錯誤，請確認後重試"
            return render(request, 'pages/login.html', locals())

    return render(request, 'pages/login.html', locals())


def logout(request):
    auth.logout(request)
    return render(request, 'pages/about.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        key = request.POST['key']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if not KeyM.objects.filter(key=key).exists():
            key_is_wrong = "此key碼不存在，請確認後重新輸入"
            return render(request, 'pages/register.html', locals())
        elif KeyM.objects.get(key=key).user:
            key_is_wrong = "此key碼已經註冊過了，請確認後重新輸入"
            return render(request, 'pages/register.html', locals())

        if User.objects.filter(username=username):
            user_is_wrong = "帳號已存在"
            return render(request, 'pages/register.html', locals())
        elif password1 != password2:
            password_is_wrong = "兩次輸入密碼不一致"
            return render(request, 'pages/register.html', locals())

        if form.is_valid():
            user = form.save()
            user = auth.authenticate(username=username, password=password1)
            auth.login(request, user)
            mykey = KeyM.objects.get(key=key)
            mykey.user = username
            mykey.timestamp = timezone.now()
            mykey.save()
            return HttpResponseRedirect('/register_info/')
        else:
            return render(request, 'pages/register.html', {"user_is_wrong":"帳號或密碼有誤"})
    else:
        form = UserCreationForm()
    return render(request, 'pages/register.html', locals())


def register_info(request):
    if 'ok' in request.POST:
        account = request.user.username
        picture = request.FILES.get('picture')
        name = request.POST['name']
        gender = request.POST['gender']
        phone_number = request.POST['phone_number']
        residential_location = request.POST['residential_location']
        housing_condition = request.POST['housing_condition']
        equipment = request.POST['equipment']
        if not picture:
            if gender=='男':
                picture = 'user_pictures/user_m.svg'
            else:
                picture = 'user_pictures/user_f.svg'

        a = Alluser(account=account, picture=picture, name=name, gender=gender,
        phone_number=phone_number,residential_location=residential_location,
        housing_condition=housing_condition, equipment=equipment)
        a.save()
        return render(request, 'stores/home.html', locals())
    f = UserForm()
    return render(request, 'pages/register_info.html', locals())


def register_info_dog(request):
    username = request.user.username
    myuser = Alluser.objects.get(account=username)

    if 'ok' in request.POST:
        name = request.POST['name']
        picture = request.FILES.get('picture')
        gender = request.POST['gender']
        age = request.POST['age']
        breed = request.POST['breed']
        character = request.POST['character']
        
        if not age.isdigit():
            age_is_wrong = "狗齡需為數字格式"
            return render(request, 'pages/register_info_dog.html', locals())

        d = Dogs(name=name, picture=picture, gender=gender, age=age,
                breed=breed, character=character, master=myuser)
        d.save()
        return render(request, 'stores/mine.html', locals())
    return render(request, 'pages/register_info_dog.html', locals())


def reservation(request,id):
    account = request.user.username
    myuser = Alluser.objects.get(account=account)

    mydogs = myuser.dogs_set.all().values()    #_list
    mydogs = json.dumps(list(mydogs), cls=DjangoJSONEncoder)

    whouser = Alluser.objects.get(account=id)

    if request.method == 'POST':
        sel_dog = request.POST['sel_dog']
        date_start = request.POST['date_start']
        time_start = request.POST['time_start']
        date_end = request.POST['date_end']
        time_end = request.POST['time_end']
        note = request.POST['note']

        datetime_start = datetime.datetime.strptime(date_start+time_start,'%Y-%m-%d%H:%M')
        datetime_end = datetime.datetime.strptime(date_end+time_end,'%Y-%m-%d%H:%M')
        
        if myuser.dogs_set.get(name=sel_dog).is_foster:
            dog_is_wrong = "這隻狗還在寄養中呀~"
            return render(request, 'pages/reservation.html', locals())

        elif datetime_start < datetime.datetime.now():
            time_is_wrong = "日期時間要比現在早"
            return render(request, 'pages/reservation.html', locals())
            
        elif datetime_start >= datetime_end:
            time_is_wrong = "結束時間不能早於等於開始時間"
            return render(request, 'pages/reservation.html', locals())
        
        myuser.dogs_set.filter(name=sel_dog).update(is_foster=True)
        
        r = Reservation(employee=myuser,employer=whouser,dog=myuser.dogs_set.get(name=sel_dog),
            datetime_start=datetime_start,datetime_end=datetime_end,note=note)
        r.save()
        return render(request, 'stores/mine.html', locals())

    return render(request, 'pages/reservation.html', locals())
