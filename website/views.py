from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# 主頁
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # 驗證
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "登入成功！")
            return redirect('home')
        else:
            messages.success(request, "登入失敗，請再重新輸入一次！")
            return redirect('home')

    return render(request, 'home.html')

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "您已登出成功！")

    return redirect('home')


def register(request):
    return render(request, 'register.html')