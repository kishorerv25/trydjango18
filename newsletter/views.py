from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.


def home(request):
    title = "Welcome , Please login to admin page"
    # if request.user.is_authenticated():
    #     title = "My title %s" % (request.user)

    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form" : form
    }

    if form.is_valid():
    	#print request.POST('email')
    	instance = form.save(commit = False)

    	full_name = form.cleaned_data.get("full_name")
    	if not full_name:
    		full_name = "New full_name"
    	instance.full_name = full_name
    	instance.save()
    	context = {
    		"title" : "Thank You"

    	}


    return render(request, 'home.html', context)
