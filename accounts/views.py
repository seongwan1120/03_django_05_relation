from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from .forms import CustomUserCreationForm
# Create your views here.

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('blog:posting_index')
    # Create_user
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:posting_index')
    
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })

@require_http_methods(['GET', 'POST'])
def signin(request):
    # login이 되어 있으면 페이지를 보여주지 않는다.
    if request.user.is_authenticated:
        # index 페이지로 튕겨낸다.
        return redirect('blog:posting_index')
    if request.method == 'POST':
        # ID/PW
        form = AuthenticationForm(request, request.POST)
        # ID/PW가 맞다면
        if form.is_valid():
            # AuthenticationForm은 용도가 다르기 때문에 .get_user() method가 존재.
            # 인증을 해줘야 한다. 인증 => 쿠키에 정보 저장.
            user = form.get_user()  # id/pw로 찾은 기존 사용자.
            login(request, user)  # 기존 사용자로 로그인(set cookie)

            # http://127.0.0.1:8000/accounts/signin/
            # ?
            # next=/blog/create/

            # 0. URL 에 ?와 &로 넘어오는 값들은 모두 request.GET 꾸러미에 담긴다.
            # 1. request.GET 은 dict
            # 2. dict의 get 메서드 떠올리기
            # 3. or 은 1 or 2 or 3 / 0 or 1 or 2
            
            return redirect(request.GET.get('next') or 'blog:posting_index')
    
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/signin.html', {
        'form': form,
    })

def signout(request):
    logout(request)
    return redirect('blog:posting_index')