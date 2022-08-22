from django.shortcuts import HttpResponse, HttpResponseRedirect, render ,redirect

from KwaDuka.forms import CustomerUserForm, LoginUserForm
from . import models


def home_view(request):
    products=models.Product.objects.all()
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'index.html',{'products':products,'product_count_in_cart':product_count_in_cart})


def signup(request):
    form = CustomerUserForm()
    if request.method == 'POST':
        form = CustomerUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
def loginPage(request):
    form = LoginUserForm()
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        email1 = request.POST.get('email1')
        password1 = request.POST.get('password1')
        user = None
        next = request.POST.get('next')
        
        if password != None and email != None:
            user_from_email = User.objects.filter(email = email)
            if user_email.exist():
                user_from_obj = list(user_from_email)[0]
                user_email = user_from_obj.email
                print(user_email)
                user = authenticate(request,username = user_from_obj.username,password = password)
        else :
            user_from_email = User.objects.filter(email=email1)
            if user_from_email.exist():
                user_from_obj = list(user_fromm_email)[0]
                user_email = user_from_obj.email
                print(user_email)
                user = authenicate(request,username = user_from_obj.username,password=password1)
        if user:
            login(request, user_from_obj)
            print('Login Success')

        
            print('Next is')
            print(next)
            if next:
                return redirect(next)
            else:
                return HttpResponseRedirect('/')
        else:
            return render(request, 'accounts/login.html', {'login_form': form, 'error': 'Error! Username or password is incorrect'})

        
        return redirect('/')


    return render(request, 'accounts/login.html', {'login_form': form}) 
            
                

    
   