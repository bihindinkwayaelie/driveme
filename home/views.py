from django.shortcuts import render
from .models import *
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request,'index.html')
def monday(request):
    return render(request,'monday.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name':name,
            'email':email,
            'subject':subject,
            'message':message,
        }
        message = '''
        New message:{}

        From:{}
        '''.format(data['message'],data['email'])
        send_mail(data['subject'],message,'',['drivemerw@gmail.com'])
        return render(request,'contact.html')
    else:
        return render(request,'contact.html',{})
          
    return render(request,'contact.html')
def dashboard(request):
    return render(request,'dashboard.html')
def signin(request):
    return render(request,'signin.html')
def requestdriver(request):
    selectdata= Client.objects.all()
    if request.method=='POST':
        fullname=request.POST['fullname']
        email=request.POST['email']
        phonenumber=request.POST['phonenumber']
        address=request.POST['address']
        currentlocation = request.POST['currentlocation']
        starttime = request.POST['starttime']
        endtime = request.POST['endtime']
        insertdata= Client(fullname=fullname,email=email,phonenumber=phonenumber,address=address,currentlocation=currentlocation,starttime=starttime,endtime=endtime)
        try:
            insertdata.save()
            return render(request, 'requestdriver.html',{'data':selectdata})
        except:
            return render(request, 'requestdriver.html')
    return render(request,'requestdriver.html',{'data':selectdata})
def base(request):
    return render(request,'base.html')
def services(request):
    return render(request,'services.html')
def signup(request):
    selectdata= Driver.objects.all()
    if request.method=='POST':
        fullname=request.POST['fullname']
        email=request.POST['email']
        gender=request.POST['gender']
        dob=request.POST['dob']
        phonenumber=request.POST['phonenumber']
        telephone=request.POST['telephone']
        address=request.POST['address']
        placeofbirth=request.POST['placeofbirth']
        nationality=request.POST['nationality']
        languages=request.POST['languages']
        experienceskills = request.POST['experienceskills']
        workingtime = request.POST['workingtime']
        idcard= request.FILES['idcard']
        licensecard = request.FILES['licensecard']
        insertdata= Driver(fullname=fullname,email=email,gender=gender,dob=dob,phonenumber=phonenumber,telephone=telephone,address=address,placeofbirth=placeofbirth,nationality=nationality,languages=languages,experienceskills=experienceskills,workingtime=workingtime,idcard=idcard,licensecard=licensecard)
        try:
            insertdata.save()
            return render(request, 'signup.html',{'data':selectdata})
        except:
            return render(request, 'signup.html')
    return render(request,'signup.html',{'data':selectdata})
def approveddrivers(request):
    selectdata= Driver.objects.all()
    return render(request,'approveddrivers.html',{'data':selectdata})
def dashboard2(request):
    return render(request,'dashboard2.html')
def more(request,id):
    selectdata= Driver.objects.get(id=id)
    if request.method == 'POST':
        selectdata.fullname=request.POST['fullname']
        selectdata.email=request.POST['email']
        selectdata.gender=request.POST['gender']
        selectdata.dob=request.POST['dob']
        selectdata.phonenumber=request.POST['phonenumber']
        selectdata.telephone=request.POST['telephone']
        selectdata.address=request.POST['address']
        selectdata.placeofbirth=request.POST['placeofbirth']
        selectdata.nationality=request.POST['nationality']
        selectdata.languages=request.POST['languages']
        selectdata.experienceskills = request.POST['experienceskills']
        selectdata.workingtime = request.POST['workingtime']
        selectdata.idcard= request.POST['idcard']
        selectdata.licensecard = request.POST['licensecard']
        msg = selectdata.save()
        if msg == True:
            redirect('adminapproval')
    return render(request,'more.html',{"data":selectdata})