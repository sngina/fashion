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
        form = ImageForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('homepage')
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

# review
def review_image(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            img_id = int(request.POST.get('imageid'))
            image = Image.objects.get(id=img_id)
            new_review = review_form.save(commit = False)
            new_review.name = request.user
            new_review.post = image
            new_review.save()

        return redirect('homepage')
# function for searching for an outfit

            