from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import auth
from .models import CustomUser as User




def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return  redirect('/')
        

    else:
        return render(request, 'index.html',{})

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(
            
            username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            auth.login(request, user)
            return  redirect('/')
         
            # recaptcha_response = request.POST.get('g-recaptcha-response')
            # url = 'https://www.google.com/recaptcha/api/siteverify'
            # values = {
            #     'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            #     'response': recaptcha_response
            # }
            # data = urllib.parse.urlencode(values).encode()
            # req = urllib.request.Request(url, data=data)
            # response = urllib.request.urlopen(req)
            # result = json.loads(response.read().decode())
            # if result['success']:
            #     auth.login(request, user)
            #     return redirect('/')
            # else:
            #     return render(request, 'login.html', {'error': 'Invalid reCAPTCHA. Please try again'})
        else:
            return JsonResponse({'message': 'error invalid'}, status=401)
    else:
        return JsonResponse({'message': 'error server'}, status=500)


def signup(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(
                username=request.POST.get('username'))

            return JsonResponse({'message': 'چنین نام کاربری در حال حاضر وجود دارد ، نام کاربری دیگری انتخاب کنید'}, status=401)
        except :
            if request.POST.get('password') == request.POST.get('confirm'):
                    
                user = User.objects.create_user(
                    request.POST.get('username'),  email=request.POST.get('email'), password=request.POST.get('password'))
                auth.login(request, user)
                return redirect('/')


            else:
                return JsonResponse({'message': 'رمز و تکرار رمز مشابه نیستند'}, status=401)



    else:

        return JsonResponse({'message': ' نام کاربری دیگری انتخاب کنید'}, status=500)
