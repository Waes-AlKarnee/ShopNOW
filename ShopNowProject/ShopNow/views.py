from django.shortcuts import render,redirect
from .forms import SignUpForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import shopCard

# Create your views here.
def homepage(request):
    return render(request, 'ShopNowApp/home.html')

def blogpage(request):
    allpost = shopCard.objects.all()
    return render(request, 'ShopNowApp/blog.html',{'allpose':allpost})
# -------------------Login------------

def loginpage(request):
    if(request.user.is_authenticated):
        return redirect('/dashboard')
    if request.method == "POST":
        forms = LoginForm(request = request, data = request.POST)
        print(forms)

        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/dashboard')
                
        else:
            return render(request, 'ShopNowApp/login.html', {'forms': forms})
        
    forms = LoginForm()
    return render(request, 'ShopNowApp/login.html', {'forms': forms})

# -------------LogOut-----------------

def logOutUser(request):
    logout(request)
    return redirect('/')

# ----------Sign Up-----------------

def signuppage(request):
    if request.method == 'POST':
        forms = SignUpForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, "Your SignUp Successful")
            return redirect('/signup')
    else:
        forms = SignUpForm()

    return render(request, 'ShopNowApp/signup.html', {'forms': forms})

# -----------Dashboard------------------

def dashboardpage(request):
    return render(request, 'ShopNowApp/dashboard.html')