from django.shortcuts import render
from fun7app.models import Father,Student,User
from fun7app.forms import StudentProfileInfoForm, UserForm

from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    return render (request,'fun7app/index.html')
def home(request):
    return render(request,'fun7app/home.html')
def mtv(request):
    student_list=Student.objects.order_by('NameStudent')
    listy={'stu_key':student_list}
    return render(request,'fun7app/mtv.html',context=listy)

def register(request):

    registered=False
    if request.method=='POST':
        user_form=UserForm(request.POST)
        student_form=StudentProfileInfoForm(request.POST)

        if user_form.is_valid() and student_form.is_valid():
            allfields=user_form.save()
            allfields.set_password(allfields.password)
            allfields.save()

            profile=student_form.save(commit=False)
            profile.allfields=allfields

            if 'profile_pic_blnk' in request.FILES:
                print('found the image')
                profile.profile_pic_blnk=request.FILES['profile_pic_blnk']

            profile.save()

            registered=True
        else:
            print(user_form.errors,student_form.errors)
    else:
        print("form is not POSTED AS OF NOW/OR METHOD != POST")
        user_form=UserForm()
        student_form=StudentProfileInfoForm()

    dict={'user_form':user_form, 'student_form':student_form , 'registered':registered}
    return render(request,'fun7app/registration.html',context=dict)


# say i have any page xyz that requires a login then i will do as below:
def page2(request):
    return render(request,'profiles/page2.html',{})

@login_required
def special(request):
    """
i think without login if you click this link it will take
you to login page...as login_required funcn is must for special to work

    """
    # return HttpResponse ("you are logged in  nice!!")
    return page2(request)

@login_required
def user_logout(request):
    logout(request)
    # return HttpResponseRedirect(reverse('home'))
    return home(request)


def login_for_user(request):

    if request.method=='POST':
        # username=Formclass(reques.POST) AS NO FORMS.PY SO
        logger_username=request.POST.get('user_name')
        #get(name)just as in {%url 'here we write name provided in urls.py'%}
        logger_password=request.POST.get('pass_word')

        user=authenticate(username=logger_username,password=logger_password)
        # username is field inside inbuit User model in django
        if user:
            if user.is_active:
                login(request,user)    #inbuit func ka use kia,,user ko send kr dia which contain
                # that username and password which any client can enter
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE BRO")
        else:
            print("someone tried to login but failed")

            print("one who tried is ,username:{} and password:{}".format(logger_username,logger_password))
            return HttpResponse("invalid login details")
    else:
        print(" control did not reached login template as of now...after this line will reach for sure")
        return render(request,'fun7app/login.html')   #you can write it outside else too



def login_for_user2(request):
    #defining other func inside so that i can use local variable username12
    def profile_page(request):
        dict={'username_tag':username12}
        return render(request,'profiles/page1.html',context=dict)
    if request.method=='POST':
        username12=request.POST.get('user_name')
        password12=request.POST.get('pass_word')

        user=authenticate(username=username12,password=password12)

        if user:
            if user.is_active:
                login(request,user)
                # return HttpResponseRedirect(reverse('index'))
                # both line does same thing
                return profile_page(request)  #manish:local function defined by me
            else:
                return HttpResponse("invalid login credential passed by user variable")
        else:
            print("someone tried to login")
            print(f"username was: {username12}and password was{password12}")

    else:
            # return HttpResponseRedirect(reverse(home))
               # even this works
        #Nothing has been provided for username or password.
        return render(request,'fun7app/login.html', {})
