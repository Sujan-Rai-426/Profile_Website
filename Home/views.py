


from django.shortcuts import redirect, render

# Create your views here.
from django.contrib import messages
from Home.forms import Contact_Form
from django.core.mail import send_mail
from django.template.loader import render_to_string

from Home.models import Back_End_Skill, CurrentAddress, Download, Front_End_Skill, Project



# Home page logic
def Index_View(request):
    
    projects = Project.objects.all() #for project model class
    FrontEnd_skills = Front_End_Skill.objects.all() #for front end skill model class
    BackEnd_skills = Back_End_Skill.objects.all() #for back end skill model class
    download_files = Download.objects.all() # for Downlaod models to downlaod resume images 
    current_address = CurrentAddress.objects.all() # for Downlaod models to downlaod resume images 
    
    # For contact from model
    if request.method == 'POST':
        form = Contact_Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            #  Get message in our email form sender using below html template Home/email/contactform.html
            html = render_to_string('email/contactform.html', {'name':name, 'email':email, 'subject':subject, 'message':message})
            send_mail('The contact form subject', 'This is the message', 'rsujan140.in@gmail.com', ['rsujan140.in@gmail.com'], html_message=html)
            messages.success(request, " Your message has been delivered successfully... ")
            return redirect("index")
        else:
            messages.error(request, " Something is wrong. Please try again... ")
            return redirect("index")
    else:
        form = Contact_Form()
    
    return render(request, 'Home/index.html', {'form': form, 'projects': projects, 'FrontEnd_skills': FrontEnd_skills, 'BackEnd_skills': BackEnd_skills, 'download_files': download_files, 'current_address': current_address})


# Logic For incomplete projects
def ComingSoon_View(request):
    return render(request, 'Home/ComingSoon.html')


