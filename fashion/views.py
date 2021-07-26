from fashion.form import ImageForm, ReviewForm
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
    c_form = ReviewForm()
    form = ImageForm()
    return render(request , 'profile/index.html', {"all_images":all_images, "imageform":form , "c_form" :c_form, "review":review})