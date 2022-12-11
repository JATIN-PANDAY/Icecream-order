from django.shortcuts import render,redirect
from ice.models import Contact
from ice.models import Order
from ice.models import Account
from django.contrib import messages


def index (request):
    return render(request,'ice.html')
def contact (request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        textarea=request.POST['desc']
        # print(name,email,textarea)
        var = Contact(Name=name,Email=email,Textarea=textarea)
        var.save()
        messages.success(request, 'Message has been sent')

    return render(request,'cont.html')

def services (request):
    return render(request,'services.html')
def about (request):
    return render(request,'about.html')
def order (request):
        if request.method=="POST":
            name=request.POST['name']
            address=request.POST['address']
            phone=request.POST['phone.no']
            select=request.POST['select']
            # print(name,address,phone,select)
            var=Order(Name=name,Mobileno=phone,Address=address,Icecream=select)
            var.save()
            messages.info(request, 'your order has been sent')

        return render(request,'order.html')


def showpage(request):
    all_data=Order.objects.all()
    return render(request,'show.html',{'key1':all_data})

# fetch data
def Editpage(request,pk):
    edit=Order.objects.get(id=pk)
    return render(request,'edit.html',{'key2':edit})
def update(request,pk):
    udata=Order.objects.get(id=pk)
    udata.Name=request.POST['name']
    udata.Mobileno=request.POST['phone.no']
    udata.Address=request.POST['address']
    udata.save()
    return redirect('show')

def delete(request,pk):
    ddata=Order.objects.get(id=pk)
    ddata.delete()
    return redirect('show')
# user regestartion 
def userregister(request):
    return render(request,'register.html')

def register(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        contact=request.POST['contact'] 
        passw=request.POST['password']
        cpassw=request.POST['cpassword']
        account=Account.objects.filter(Email=email)
        if account:
            message='User already register'
            return render(request,'register.html',{'msg':message})
        else:
            if  passw==cpassw:
                new=Account.objects.create(Username=name,Email=email,Contact=contact,Password=passw)
                message="Your account created please login to continue"
                return render(request,'log.html',{'msg':message})
            else:
                message="Password and confirm does'nt match"
                return render(request,'register.html',{'msg':message})
def login(request):
    return render(request,'log.html')
def loginuser(request):
    if request.method=="POST":
        Email=request.POST['email']
        password=request.POST['password']

        user=Account.objects.get(Email=Email)
        
        if user:
            if user.Password==password:
                request.session['Name']=user.Username
                request.session['Email']=user.Email
                request.session['Contact']=user.Contact
                message='register successfully'
                return render(request,'home.html',{'msg':message})
            else:
                message='Please enter correct Password' 
                return render(request,'log.html',{'msg':message})
        else:
            message='User does not exist'
            return render(request,'register.html',{'msg':message})   






        



        
    # if request.method=='POST':
    #     name=request.POST['name']
    #     email=request.POST['email']
    #     contact=request.POST['contact']
    #     password= request.POST['password']
    #     cpassword= request.POST['cpassword']
    #     user=Account.objects.filter(Email=email)
    #     return render(request,'account.html',{'msg':message})
        # else:
        #     if password==cpassword:
        #         newuser=Account.objects.create(Username=name,Email=email,Contact=contact,Password=password)
        #         return render(request,'log.html')
        #     else:
        #          return render(request,'about.html')





# our css
# def style (request):
#     return render(request,'style.html')
