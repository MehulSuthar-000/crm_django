from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


def home(request):
    records = Record.objects.all()

    # Check to see if logging in
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"You have been logged lin")
            return redirect('home')
        else:
            messages.error(request, "There was an error logging in, please try again...")
            return redirect('home')
    else:
        return render(request, 'website/home.html', {'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome")
            return redirect('home')
        
    else:
        form = SignUpForm()
        context = {'form':form}
        return render(request, 'website/register.html', context)
    return render(request, 'website/register.html', {'form':form})


def recordDetail(request, pk):
    if request.user.is_authenticated:
        # Look Up Record
        customer_record = Record.objects.get(id=pk)
        context = {'customer_record': customer_record}
        return render(request, 'website/record.html', context)
    else:
        messages.success(request, "You Must be logged in to view that page...")
        return redirect('home')
    
def deleteRecord(request, pk):
    if request.user.is_authenticated:
        deleted_record = Record.objects.get(id=pk)
        deleted_record.delete()
        messages.success(request, 'Record Deleted Successfully...')
        return redirect('home')
    else:
        messages.success(request, 'You Must Be Logged In to Delete Record...')
        return redirect('home')

def addRecord(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added...")
                return redirect('home')
        context = {'form':form}
        return render(request, 'website/add_record.html', context)
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')