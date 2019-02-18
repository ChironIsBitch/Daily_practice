from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile

# Create your views here.
def index(request):
    return render(request, 'index.html')

def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('acount', None)
        pass_word = request.POST.get('password', None)
        print(user_name, pass_word)
        user_data = UserProfile.objects.get()
        user = authenticate(username=user_name, password=pass_word)
        # 如果不是null说明验证成功
        if user is not None:
            # 登录
            login(request, user)
            return render(request, 'index.html', {'user': user_data})
        else:
            return render(request, 'index.html', {'msg': '用户名或密码错误'})

    elif request.method == 'GET':
        return render(request, 'index.html')

def user_logout(request):
    logout(request)
    return render(request, 'index.html')