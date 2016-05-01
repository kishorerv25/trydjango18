from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import SignUpForm, ContactForm
# Create your views here.

def home(request):
	title = "Welcome , Please login to admin page"

	form = SignUpForm(request.POST or None)
	context = {
		"title": title,
		"form":form,
		}

	if form.is_valid():
		instance = form.save(commit = False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full_name"
			instance.full_name = full_name
			instance.save()
			context = {
				"title": "Thank you"
				
				}

	return render(request, 'home.html', context)


def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
	# 	for key, value in form.cleaned_data.iteritems():
	# 		print key, value
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		print form_email,form_message,form_full_name
		
		#import pdb;pdb.set_trace()
		
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'kishorebanrv25@gmail.com']
		contact_message = "%s: %s via %s"%(
			form_full_name,
			form_message,
			form_email)

		some_html_message = """
		<h1>hello</h1>

		<img src="/static/img/images1.jpg" height="42" width="42"/>
		"""
		
		send_mail(subject,
			contact_message,
			from_email,
			to_email,
			html_message = some_html_message,
			fail_silently = True)
	
	context = {
		"form":form,
	}
	return render(request, "forms.html", context)
