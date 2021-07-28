from django.contrib.auth.models import User
from fashion.form import ImageForm, ProfileForm, ReviewForm, UserForm
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render , redirect
from django.http import HttpResponse ,Http404 
from .models import Image ,Profile ,Review
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
#returning images
@login_required(login_url='/accounts/login')
def get_images(request):
    all_images = Image.objects.all()
    review = Review.objects.all()
    if request.method == 'POST':
        c_form = ReviewForm(request.POST)
        form = ImageForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('homepage')
        if c_form.is_valid():
            c_form.save()
            return redirect('homepage')
    else:
        c_form = ReviewForm()
        form = ImageForm()
    return render(request , 'profile/index.html', {"all_images":all_images, "imageform":form , "c_form" :c_form, "review":review})

def userpage(request):
	user_form = UserForm(instance=request.user)
	profile_form = ProfileForm(instance=request.user.profile)
	return render(request,"registration/profile.html", context={"user":request.user, "user_form":user_form, "profile_form":profile_form })

# function for clicking on one image
def image_details(request , id):
    one_image = Image.objects.get(id = id)
    return render(request , 'profile/image.html' , {"one_image": one_image})

# search function

def search(request) :
        if 'profile' in request.GET and request.GET["profile"]:
            search_term = request.GET.get("profile")
            search_profile = Profile.search_profile(search_term)
            message = f"{search_term}"

            return render(request , 'profile/search.html' ,{"message" : message , "search_profile":search_profile} ) 

        else:
            message = "You haven't searched for any profile"
            return render(request , 'profile/search.html') 