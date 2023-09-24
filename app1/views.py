from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.cache import cache

# Create your views here.
def WebPage(request):
    return render (request,'website.html')

def SignupPage(request):
    print(f"PANKAJ 0 === {request}")
    if request.method=='POST':
        firstname=request.POST.get('first_name')
        lastname=request.POST.get('last_name')
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        print(f"=========================>>>>>-------------->>>>PANKAJ!|==> uname:{uname} , email:{email}")
        if pass1!=pass2:
            print(f"Your password and confrom password are not Same!!")
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(username=uname, email=email, password=pass1,
                                               first_name=firstname, last_name=lastname)
            my_user.save()
            return redirect('login')
        
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')


#reuqed login urls

@login_required(login_url='login')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def HomePage(request):
    user = request.user
    context = {
        'user_id': user.id,
        'username': user.username,
    }
    print(f"=========================>>>>>-------------->>>>PANKAJ!|==> uname:{context} ")
    if request.method=='POST':
       print("Anonomus --user ----------------------------")
       anonymous_name=request.POST.get('anonymous_name') 
       if anonymous_name != '' and anonymous_name is  not None :
            print(f"Anonomus  ===> {anonymous_name}")  
            cached_dict = cache.get('anonymous_user_details') 
            print(f"Anonomus chache   ===> {cached_dict}") 
            if cached_dict is None:
                context['anonymous_name'] = anonymous_name
                print(f"Anonomus chache  set  ===> {context}")
                cache.set('anonymous_user_details', context)
                return redirect('anonymous_chat')
            elif cached_dict["anonymous_name"] == anonymous_name:
                print("Anonums User alredy Exits")
                return "Anonums User alredy Exits" 
            else:
                context['anonymous_name'] = anonymous_name
                print(f"Anonomus chache  set  ===> {context}")
                cache.set('anonymous_user_details', context)
                return redirect('anonymous_chat')
    return render (request,'homepage.html',context)

def Frinds(request):
    user = request.user
    context = {
        'user_id': user.id,
        'username': user.username,
    }
    return render (request,'friends.html',context)

def Groups(request):
    user = request.user
    context = {
        'user_id': user.id,
        'username': user.username,
    }
    return render (request,'groups.html',context)

def Anonymous(request):
    user = request.user
    context = {
        'user_id': user.id,
        'username': user.username,
    }
    if request.method=='POST':
       print("Anonomus --user ----------------------------")
       anonymous_name=request.POST.get('anonymous_name') 
       if anonymous_name != '' and anonymous_name is  not None :
            print(f"Anonomus  ===> {anonymous_name}")  
            cached_dict = cache.get('anonymous_user_details') 
            print(f"Anonomus chache   ===> {cached_dict}") 
            if cached_dict is None:
                context['anonymous_name'] = anonymous_name
                print(f"Anonomus chache  set  ===> {context}")
                cache.set('anonymous_user_details', context)
                return redirect('anonymous_chat')
            elif cached_dict["anonymous_name"] == anonymous_name:
                return render('template_name', message='Anonums User alredy Exits')
            else:
                context['anonymous_name'] = anonymous_name
                print(f"Anonomus chache  set  ===> {context}")
                cache.set('anonymous_user_details', context)
                return redirect('anonymous_chat')
    return render (request,'anonymous.html',context)

def Ai_Chat(request):
    user = request.user
    context = {
        'user_id': user.id,
        'username': user.username,
    }
    return render (request,'chat_ai.html',context)


def Vedio_Chat(request):
    user = request.user
    context = {
        'user_id': user.id,
        'username': user.username,
    }
    return render (request,'vedio_chat.html',context)


#anonymous_chat view
def Anonymous_Chat(request):
    user = request.user
    # context = {
    #     'user_id': user.id,
    #     'username': user.username,
    # }
    cached_dict = cache.get('anonymous_user_details')
    print(f"anonymous_chat start with {cached_dict}")
    if cached_dict is not None:
        ano_user = cached_dict['anonymous_name']
        print(f"ANO USER ==> {ano_user}")
        return render (request,'anonymous_chat.html',message=ano_user)
    html = "<html><body>Please Go to HomePage and login again </body></html>" 
    return HttpResponse(html)
     