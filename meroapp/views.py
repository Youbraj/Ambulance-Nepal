from django.shortcuts import render ,redirect
from django.http import HttpResponse
from meroapp.db import data
from .forms import AmbulanceForm
from .forms import UpdateData
from datetime import date

def view_queries(request):
    # # return HttpResponse("ok")
    # name = request.POST.get('name') 
    # contact=request.POST.get('contact')
    # email=request.POST.get('email')
    # subject=request.POST.get('subject')
    # message=request.POST.get('message')
    # date=
    # d=data()
    # d.display_query(name, contact, email,subject,message,date)
    d = data()
    queries = d.display_query()
    my_list = []
    queries_list = {'data':[]}
    for query in queries:
        my_queries = {}
        query_attr = ['id','name','contact', 'email','subject','message','date']
        for index,mydata in enumerate(query_attr):
            my_queries[mydata] = query[index]
        queries_list['data'].append(my_queries)
    context = {
        'queries':queries_list,  
    }
    return render(request,'meroapp/view_queries.html',context)

def send_query(request):
    if request.method == 'POST':
        name = request.POST.get('name') 
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        d=data()
        d.insert_query(name, contact, email,subject,message,date.today())
        return redirect("meroapp:contact")

def ambulances_search(request):
    if (request.GET.get('ambulance-list',None) is not None and request.GET.get('ambulance-list',None) is not '' ) and (request.GET.get('ambulance-list-by-address',None) is not None and request.GET.get('ambulance-list-by-address',None) is not '' ):
        doctor_name = request.GET.get('ambulance-list')
        address = request.GET.get('ambulance-list-by-address')

        print(doctor_name)
        d = data()
        persons = d.search_multi(doctor_name,address)
    elif(request.GET.get('ambulance-list',None) is not None and request.GET.get('ambulance-list',None) is not '' ):
        doctor_name = request.GET.get('ambulance-list')
        d = data()
        persons = d.search(doctor_name)
    
    elif(request.GET.get('ambulance-list-by-address',None) is not None and request.GET.get('ambulance-list-by-address',None) is not ''):
        address = request.GET.get('ambulance-list-by-address')
        d = data()
        persons = d.searchbyaddress(address)

    else:
        d = data()
        persons = d.fetch()
    my_list = []
    person_list = {'data':[]}
    for person in persons:
        my_person = {}
        person_attr = ['id','name','contact', 'address']
        for index,mydata in enumerate(person_attr):
            my_person[mydata] = person[index]
        person_list['data'].append(my_person)
    context = {
        'persons':person_list,  
    }
    return render(request,'meroapp/list_doctor.html',context)


def index(request):
    return render(request,'meroapp/index.html',{})

def about(request):
    return render(request,'meroapp/about.html',{})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name') 
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        d=data()
        d.insert_query(name, contact, email,subject,message,date.today())
        context = {
            'form_success':True
        }
        return render(request,'meroapp/contact.html',context)
    else:
        context = {
            'form_success':False
        }
        return render(request,'meroapp/contact.html',context)

def admin(request):
    return render(request,'meroapp/login.html',{})

def admin_home(request):
    if request.method == 'POST':

        username=request.POST.get('uname')
        pwd=request.POST.get('pwd')
        if (username == 'admin' and pwd == 'admin'):
            return render(request,'meroapp/admin_home.html',{})
        else:
            return redirect('meroapp:login')
    else:
        return render(request,'meroapp/admin_home.html',{})


def view_ambulances(request):
    ambulance_form = AmbulanceForm()
    if (request.GET.get('ambulance-list',None) is not None and request.GET.get('ambulance-list',None) is not '' ) and (request.GET.get('ambulance-list-by-address',None) is not None and request.GET.get('ambulance-list-by-address',None) is not '' ):
        doctor_name = request.GET.get('ambulance-list')
        address = request.GET.get('ambulance-list-by-address')

        print(doctor_name)
        d = data()
        persons = d.search_multi(doctor_name,address)
    elif(request.GET.get('ambulance-list',None) is not None and request.GET.get('ambulance-list',None) is not '' ):
        doctor_name = request.GET.get('ambulance-list')
        d = data()
        persons = d.search(doctor_name)
    
    elif(request.GET.get('ambulance-list-by-address',None) is not None and request.GET.get('ambulance-list-by-address',None) is not ''):
        address = request.GET.get('ambulance-list-by-address')
        d = data()
        persons = d.searchbyaddress(address)

    else:
        d = data()
        persons = d.fetch()
    my_list = []
    person_list = {'data':[]}
    for person in persons:
        my_person = {}
        person_attr = ['id','name','contact', 'address']
        for index,mydata in enumerate(person_attr):
            my_person[mydata] = person[index]
        person_list['data'].append(my_person)
    context = {
        'persons':person_list,  
        'ambulance_form':ambulance_form
    }
    return render(request,'meroapp/view_ambulances.html',context)

def insert_ambulance(request):
    form = AmbulanceForm()
    if request.method == 'POST':
        form = AmbulanceForm(request.POST)
        if form.is_valid():
            
            d = data()
            # id = form.cleaned_data['id']
            name = form.cleaned_data['name']
            contact = form.cleaned_data['contact']
            address = form.cleaned_data['address']
            d.insert(name,contact,address)

            return redirect('meroapp:view-ambulances')
        else:
            return HttpResponse(form.errors)
    else:
        return HttpResponse('NOT ALLOWED')


def update_ambulance(request,id):
    context = {}
    if request.method == "GET":
        d = data()
        my_ambulance = d.getbyid(id)
        for unique_ambulance in my_ambulance:
            form = {
                'id': unique_ambulance[0],
                'name':unique_ambulance[1],
                'contact':unique_ambulance[2],
                'address':unique_ambulance[3]
            }
            # form.id = unique_ambulance[0]
            # form.name = unique_ambulance[1]
            # form.contact = unique_ambulance[2]
            # form.address = unique_ambulance[3]

            true_form = UpdateData(initial= form)
        
        context['form'] = true_form

        return render(request,'meroapp/myform.html',context)

    # if request.method== "POST":
    #     d=data()
    #     name=
    #     d.update(form["name"], form["contact"], form["address"])
    #     return redirect('meroapp:view-ambulances')
    
    elif request.method == 'POST':
        print(request.POST)
        form = UpdateData(request.POST)
        if form.is_valid():
        # if True:
            d = data()
            id = form.cleaned_data['id']
            name = form.cleaned_data['name']
            contact = form.cleaned_data['contact']
            address = form.cleaned_data['address']
            d.update(id,name,contact,address)
        
            return redirect('meroapp:view-ambulances')
        else:
            return HttpResponse(form.errors)
    else:
       return HttpResponse('NOT ALLOWED')    

def delete_ambulance(request,id):
    if request.method == 'GET':
        d =data()
        my_ambulance = d.getbyid(id)
        for unique_ambulance in my_ambulance:
            form = {
                'id': unique_ambulance[0],
                'name':unique_ambulance[1],
                'contact':unique_ambulance[2],
                'address':unique_ambulance[3]
            }
        
        context = {
            'form':form
        }
        return render(request,'meroapp/deleteform.html',context)
    if request.method=="POST":
        d=data()
        d.delete(id)
        return redirect('meroapp:view-ambulances')

