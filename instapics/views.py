import datetime as dt
from django.http  import HttpResponse,Http404
# from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import Image,Profile,Comment
from .forms import NewPostForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def instaImages(request):

    current_user = request.user
    profile = Profile.get_profile()
    image = Image.get_images()
    
    comments = Comment.get_comment()
    return render(request,'welcome.html',{"profile":profile,"comments":comments,"current_user":current_user,"images":image,})


@login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user = request.user
    profile = Profile.get_profile()
    image = Image.get_images()
    comments = Comment.get_comment()

    return render(request,'profile/profile.html',{"title":title,"comments":comments,"image":image,"user":current_user,"profile":profile,})


@login_required(login_url="/accounts/login/")
def new_post(request):
    title = 'Insta-Gram'
    current_user = request.user
    profiles = Profile.get_profile()
    for profile in profiles:
        if profile.user.id == current_user.id:
            if request.method == 'POST':
                form = UploadForm(request.POST,request.FILES)
                if form.is_valid():
                    upload = form.save(commit=False)
                    upload.user = current_user
                    upload.profile = profile
                    upload.save()
                    return redirect('home')
            else:
                form = UploadForm()
            return render(request,'upload/new.html',{"title":title,
                                                    "user":current_user,
                                                    "form":form})


@login_required(login_url="/accounts/login/")
def search_results(request):
    current_user = request.user
    profile = Profile.get_profile()
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_name = Profile.find_profile(search_term)
        message = search_term

        return render(request,'search.html',{"message":message,
                                             "profiles":profile,
                                             "user":current_user,
                                             "username":searched_name})
    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def new_comment(request,pk):
    image = get_object_or_404(Image, pk=pk)
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.user = current_user
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'comment.html', {"user":current_user,
                                            "comment_form":form})



@login_required(login_url="/accounts/login/")
def view_your_profile(request,pk):
    title =  "Insta-gram"
    current_user = request.user
    image = Image.get_images()
    profile = Profile.get_profile()
    comment = Comment.get_comment()
    user = get_object_or_404(User, pk=pk)
    return render(request,'profile/view.html',{"user":current_user,
                                               "images":image,
                                               "my_user":user,
                                               "comments":comment,
                                               "profile":profile})

@login_required(login_url="/accounts/login/")
def like(request,operation,pk):
    image = get_object_or_404(Image,pk=pk)
    if operation == 'like':
        image.likes += 1
        image.save()
    elif operation =='unlike':
        image.likes -= 1
        image.save()
    return redirect('home')


def new_post(request):
    current_user = request.user
    if request.method == 'POST':

        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():

            post = form.save(commit=False)
            post.user = current_user

            post.save()
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form })



@login_required(login_url='/accounts/login/')
def edit_profile(request):
  
    current_user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST,request.FILES)
        if form.is_valid():
            update = form.save(commit=False)
            update.user = current_user
            update.save()
            return redirect('profile')
    else:
        form = EditProfileForm()
    return render(request,'profile/edit.html',{"title":title,"form":form})
