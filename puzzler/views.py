from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomRegisterForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

@login_required
def game(request):
    return render(request, 'game.html')

def signup(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST or None)
        if form.is_valid():
           
            form.save()
           #  username=form.cleaned_data.get('username')
            messages.success(
                request, f"Your account has been created! You are now able to log in")
            return redirect('login')
    else:
        form = CustomRegisterForm()
    return render(request, 'signup.html', {'form': form})    