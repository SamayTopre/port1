from django.shortcuts import render
from django.http import HttpResponse
from forminfo.models import forminfo
from django.core.mail import send_mail
from django.conf import settings



def contact(request):
    data={}
    try:
        if request.method=='POST':
            name=request.POST.get('name')
            mail=request.POST.get('mail')
            phone=request.POST.get('phone')
            data={
            'name':name,
            'mail':mail,
            'phone':phone 
             }
            
            
    except:
        pass 
    
    data={}
    try:
        if request.method=='POST':
            name=request.POST.get('name')
            city=request.POST.get('city')
            state=request.POST.get('state')
            address=request.POST.get('address')
            mail=request.POST.get('mail')
            phone=request.POST.get('phone')
            data={
            'name':name,
            'city':city,
            'state':state,
            address:'address',
            'mail':mail,
            'phone':phone 
            }
            
            en=forminfo(name=name,mail=mail,phone=phone)
            en.save()
            message_body = f"Name: {name}\nEmail: {mail}\nPhone: {phone}"
            send_mail(
                subject="Contact Form Submission",
                message=message_body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=["STarchitects2023@gmail.com"], 
            )
            subject = "Thank You for Contacting me"
            message = "Thank you for reaching out to me. I appreciate your interest and will get back to you soon."
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [mail]

           
            send_mail(subject, message, from_email, recipient_list)

    except  Exception as e:
        print("Error sending email:", e) 
    return render(request,'form.html',data)   