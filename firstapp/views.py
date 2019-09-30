from django.shortcuts import render,HttpResponse,redirect
from firstapp.forms import SiteUserForm,UserRoleForm,ImagesForm
from firstapp.models import SiteUser,UserRole,Images
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to the first response</h1>")
#we can also add anythin html code in the commas..


def home(request):
    return render(request,"home.html")


def about(request):

    name="vishul"
    names=["vishul","vikas","beenu"]
    return render(request,"about.html",{'n':name,'l':names})

def testhome(request):
    return render(request,"home_master.html")


def signup(request):
    if request.method=="POST":
        form=SiteUserForm(request.POST)
        f=form.save(commit=False)
        f.userFullName=request.POST["username"]
        f.userEmail = request.POST["useremail"]
        f.userPassword =make_password(request.POST["userpassword"])
        f.userMobile = request.POST["usermobile"]
        f.isActive=True
        f.roleId_id=2
        f.save()
        return render(request, "signup.html",{'success':True})
    return render(request,"signup.html")


def formname(request):
    if request.method=="POST":
        form=UserRoleForm(request.POST)
        f=form.save(commit=False)
        f.roleName=request.POST["rolename"]
        f.isActive=True
        f.save()
        return render(request, "formname.html", {'success1': True})
    return render(request, "formname.html")

def datafetch(request):
    data=SiteUser.objects.filter(isActive=1)
    #data = SiteUser.objects.all()
    #data = SiteUser.objects.get(userEmail="vishul@gmail")

    return render(request,"viewdata.html",{'d':data})

def viewall(request):
    data = SiteUser.objects.all()

    return render(request, "viewall.html", {'d': data})

def viewone(request):
    data = SiteUser.objects.get(userEmail="vishul@gmail")

    return render (request,"viewone.html",{'d':data})


def image(request):
    if request.method=="POST":
        form= ImagesForm(request.POST)
        img1=None
        try:
            if request.FILES["userimage"]:
                my_file = request.FILES["userimage"]
                fs=FileSystemStorage()
                file_name =fs.save(my_file.name,my_file)
                img1= fs.url(file_name)
                img1= my_file
        except:
            pass
        f=form.save(commit=False)
        f.userFullName=request.POST["username"]
        f.userEmail = request.POST["useremail"]
        f.userImage = img1
        f.userPassword = request.POST["userpassword"]
        f.userMobile = request.POST["usermobile"]
        f.isActive=True
        f.roleId_id=2
        f.save()
        return render(request, "image.html",{'success':True})
    return render(request,"image.html")

def update(request):
    if request.method=="POST":
        emailid=request.POST["useremail"]
        u_name=request.POST["username"]
        u_password=request.POST["userpassword"]
        u_contact = request.POST["usermobile"]
        updatedata=SiteUser(userEmail=emailid,userFullName=u_name,userPassword=u_password,userMobile=u_contact)
        updatedata.save(update_fields=["userFullName","userPassword","userMobile"])
        return render(request,"update.html")

    return render(request,"update.html")

def deletedata(request):
    emailid= request.GET["id"]
    data=SiteUser.objects.get(userEmail=emailid)
    data.delete()
    return redirect("/viewdata/")


def editdata(request):
    emailid = request.GET["id"]
    data = SiteUser.objects.get(userEmail=emailid)
    if request.method=="POST":

        u_name = request.POST["username"]
        u_password = request.POST["userpassword"]
        u_contact = request.POST["usermobile"]
        updatedata = SiteUser(userEmail=emailid, userFullName=u_name, userPassword=u_password, userMobile=u_contact)
        updatedata.save(update_fields=["userFullName", "userPassword", "userMobile"])

        return redirect("/viewdata/")

    return render(request, "update2.html", {'r': data})



def imagefetch(request):
    emailid = request.GET["id1"]
    data = Images.objects.get(userEmail=emailid)

    if request.method == "POST":
        form = ImagesForm(request.POST)
        img1 = None
        try:
            if request.FILES["userimage"]:
                my_file = request.FILES["userimage"]
                fs = FileSystemStorage()
                file_name = fs.save(my_file.name, my_file)
                img1 = fs.url(file_name)
                img1 = my_file
        except:
            pass
        userimage=img1
        u_name = request.POST["username"]
        u_password = request.POST["userpassword"]
        u_contact = request.POST["usermobile"]

        updatedata = Images(userEmail=emailid, userFullName=u_name, userPassword=u_password, userMobile=u_contact,userImage=img1)

        updatedata.save(update_fields=["userFullName", "userPassword", "userMobile", "userImage"])

        return redirect("/viewdata/")

    return render(request, "imagefetch.html", {'v': data})





def viewimage(request):
    data=Images.objects.filter(isActive=1)
    #data = SiteUser.objects.all()
    #data = SiteUser.objects.get(userEmail="vishul@gmail")

    return render(request,"viewimage.html",{'d':data})



def viewimage2(request):
    emailid = request.GET["id1"]
    data = Images.objects.get(userEmail=emailid)

    if request.method == "POST":
        form = ImagesForm(request.POST)
        img1 = None
        try:
            if request.FILES["userimage"]:
                my_file = request.FILES["userimage"]
                fs = FileSystemStorage()
                file_name = fs.save(my_file.name, my_file)
                img1 = fs.url(file_name)
                img1 = my_file
        except:
            pass
        userimage = img1
        u_name = request.POST["username"]
        u_password = request.POST["userpassword"]
        u_contact = request.POST["usermobile"]

        updatedata = Images(userEmail=emailid, userFullName=u_name, userPassword=u_password, userMobile=u_contact,userImage=img1)

        updatedata.save(update_fields=["userFullName", "userPassword", "userMobile", "userImage",])

        return redirect("/viewimage/")

    return render(request, "viewimage2.html", {'k': data})



def deleteimage(request):
    mail= request.GET["id"]
    data = Images.objects.get(userEmail=mail)
    data.delete()
    return redirect("/viewimage/")
