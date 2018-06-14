from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from stores.models import Alluser, Dogs, GPSs, Message, Reservation
from django.forms.models import model_to_dict

from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
import json
import time
import datetime
import math

import sys, os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))    #__file__獲取執行文檔相對路徑，整行為取上一級的上一級目錄
sys.path.append(BASE_DIR)   #添加路徑
import cal_datetime


@login_required
def home(request):
    if 'gpsdate' in request.POST:
        gpsdate = request.POST['gpsdate']
    else:
        gpsdate = time.strftime("%Y-%m-%d", time.localtime())

    username = request.user.username
    
    myuser = Alluser.objects.get(account=username)
    mydog = Dogs.objects.get(master=myuser)

    gpshtml = GPSs.objects.filter(dog=mydog, date=gpsdate).order_by('date','time')

    gpss = GPSs.objects.filter(dog=mydog, date=gpsdate).order_by('date','time').values()    #_list
    gpss = json.dumps(list(gpss), cls=DjangoJSONEncoder)

    return render(request, 'stores/home.html', locals())


@login_required
def foster(request):
    username = request.user.username
    myuser = Alluser.objects.get(account=username)
    collection_users = myuser.collection_user.split(',');
    
    if 'searchUser' in request.POST:
        searchUser = request.POST['searchUser']
        alluser = Alluser.objects.filter(name__icontains=searchUser)
    else:
        alluser = Alluser.objects.all()
        alldog = Dogs.objects.all()

    if 'collection' in request.POST:
        collection_name = request.POST['collection']
        if collection_name in collection_users:
            collection_users.remove(collection_name)
            myuser.collection_user = ",".join(collection_users)
        else:
            myuser.collection_user = myuser.collection_user + "," + collection_name
        myuser.save()

    allusers = alluser.values()    #_list
    allusers = json.dumps(list(allusers), cls=DjangoJSONEncoder)
    alldogs = alldog.values()    #_list
    alldogs = json.dumps(list(alldogs), cls=DjangoJSONEncoder)

    return render(request, 'stores/foster.html', locals())


@login_required
def message(request):
    username = request.user.username
    myuser = Alluser.objects.get(account=username)
    
    message = Message.objects.order_by('-timestamp')[0]
    m_time = datetime.datetime.strptime(str(message.timestamp)[:19], '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=8)
    now = datetime.datetime.now()

    diff_t = cal_datetime.DiffDatetime(now, m_time)

    t1 = str(now)
    t2 = str(m_time)
    td = str(diff_t.to_str_simplify())
    t1 = json.dumps(t1, cls=DjangoJSONEncoder)
    t2 = json.dumps(t2, cls=DjangoJSONEncoder)
    td = json.dumps(td, cls=DjangoJSONEncoder)


    chat_userss = myuser.chat_user.split(',');
    chat_users = []
    for account in chat_userss:
        oneuser = Alluser.objects.get(account=account)
        chat_users.append(oneuser)

    alluser = Alluser.objects.all()


    the_reservation = Reservation.objects.filter(employee=myuser)
    #the_reservation.dog
    print(the_reservation[0].dog.breed)
    return render(request, 'stores/message.html', locals())


@login_required
def message_user(request,id):
    account = request.user.username
    myuser = Alluser.objects.get(account=account)
    whouser = Alluser.objects.get(account=id)
    messages = Message.objects.order_by('timestamp')
    who = id

    messages_val = messages.values()    #_list
    
    messages_time=[]
    for message in messages:
        m_time = datetime.datetime.strptime(str(message.timestamp)[:19], '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=8)
        now = datetime.datetime.now()
        
        diff_t = cal_datetime.DiffDatetime(now, m_time)
        messages_time.append( diff_t.to_str_simplify() )

    for index, message in enumerate(messages_val):
        message["messages_time"] = messages_time[index]
        message["picture"] = str(whouser.picture)

    messages_js = json.dumps(list(messages_val), cls=DjangoJSONEncoder)
    

    if 'message_text' in request.POST:
        message = Message(account=account, name=myuser.name, text=request.POST.get('message_text'))
        message.save()
        return HttpResponseRedirect(request.path)

    return render(request, 'stores/message_user.html', locals())


@login_required
def mine(request):
    account = request.user.username
    myuser = Alluser.objects.get(account=account)
    mydog = myuser.dogs_set.all()
    if 'edit' in request.POST:
        isEdit = True
    elif 'ok' in request.POST:
        isEdit = False
        #picture = request.FILES.get('picture')
        name = request.POST['name']
        gender = request.POST['gender']
        phone_number = request.POST['phone_number']
        residential_location = request.POST['residential_location']
        housing_condition = request.POST['housing_condition']
        equipment = request.POST['equipment']
        
        myuser.name = name
        myuser.gender = gender
        myuser.phone_number = phone_number
        myuser.residential_location = residential_location
        myuser.housing_condition = housing_condition
        myuser.equipment = equipment
        
        myuser.save()
    
    dname = request.POST.getlist('dname[]')
    dgender = request.POST.getlist('dgender[]')
    dage = request.POST.getlist('dage[]')
    dbreed = request.POST.getlist('dbreed[]')
    dcharacter = request.POST.getlist('dcharacter[]')
    for i in range(len(mydog)):
        if 'dedit' in request.POST:
            isdEdit = True
        elif 'dok' in request.POST:
            isdEdit = False
            
            mydog[i].name = dname[i]
            mydog[i].gender = dgender[i]
            mydog[i].age = dage[i]
            mydog[i].breed = dbreed[i]
            mydog[i].character = dcharacter[i]
            
            mydog[i].save()
    return render(request, 'stores/mine.html', locals())


@login_required
def collection(request):
    account = request.user.username
    myuser = Alluser.objects.get(account=account)
    
    collection_users = myuser.collection_user.split(',');

    if 'collection' in request.POST:
        collection_name = request.POST['collection']
        if collection_name in collection_users:
            collection_users.remove(collection_name)
            myuser.collection_user = ",".join(collection_users)
        else:
            myuser.collection_user = myuser.collection_user + "," + collection_name
        myuser.save()
    
    allusers = []
    for account in collection_users:
        oneuser = Alluser.objects.get(account=account)
        allusers.append(oneuser)

    alluser2 = Alluser.objects.all()
    alldog2 = Dogs.objects.all()

    allusers2 = alluser2.values()    #_list
    allusers2 = json.dumps(list(allusers2), cls=DjangoJSONEncoder)
    alldogs2 = alldog2.values()    #_list
    alldogs2 = json.dumps(list(alldogs2), cls=DjangoJSONEncoder)

    return render(request, 'stores/collection.html', locals())


@login_required
def user_info(request,id):
    thisuser = Alluser.objects.get(account=id)
    #thisdog = thisuser.dogs_set.all()

    return render(request, 'stores/user_info.html', locals())


@login_required
def setting(request):
    account = request.user.username
    myuser = Alluser.objects.get(account=account)
    # alluser = Alluser.objects.all()
    # alldog = Dogs.objects.all()

    # allusers = alluser.values()    #_list
    # allusers = json.dumps(list(allusers), cls=DjangoJSONEncoder)
    # alldogs = alldog.values()    #_list
    # alldogs = json.dumps(list(alldogs), cls=DjangoJSONEncoder)

    return render(request, 'stores/setting.html', locals())


def getGPS(request):
    if 'ok' in request.GET:
        dog_name = request.GET['dog_name']
        latitude = request.GET['latitude']
        longitude = request.GET['longitude']
        dog = Dogs.objects.get(name=dog_name)

        gps = GPSs(latitude=latitude, longitude=longitude, dog=dog)
        gps.save()
        return render(request, 'stores/home.html', locals())
    return render(request, 'stores/getGPS.html', locals())

