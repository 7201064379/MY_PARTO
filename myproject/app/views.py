from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import*

# Create your views here.
def index(request):
    if request.method == 'POST':
        tn = request.POST['team_name']
        pn = request.POST['project_name']
        lc = request.POST['lead_contact']
        m1 = request.POST['member1']
        m2 = request.POST['member2']
        m3 = request.POST['member3']
        m4 = request.POST['member4']

        uid = Registration.objects.create(
            team_name=tn,
            project_name=pn,
            lead_contact=lc,
            member1=m1,
            member2=m2,
            member3=m3,
            member4=m4,
        )
        return redirect('response')
    return render(request,"index.html")

def response(request):
    return  render(request,'response.html')
def register(request):
    if request.method == "POST":
        team = request.POST.get('team_name')
        project = request.POST.get('project_name')
        email = request.POST.get('lead_contact')
        member1 = request.POST.get('member1')
        member2 = request.POST.get('member2')
        member3 = request.POST.get('member3')
        member4 = request.POST.get('member4')

        Registration.objects.create(
            team_name = team,
            project_name = project,
            lead_contact = email,
            member1 = member1,
            member2 = member2,
            member3 = member3,
            member4 = member4,
        )
        send_mail(
            subject="Registration Successful - CodeFest 2K25",
            message=f"Hello {team},\n"
                    "\nYour registration is successful!\nBest of luck to you guys  ",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=True,
        )


        return render(request, "response.html")

    return redirect('index')