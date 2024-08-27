from django.shortcuts import render
from .models import Tweet , TweetInfo as TweetInfoModel
from .forms import TweetForm , UserRegistrationForm , TweetInfo
from django.shortcuts import get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.

def index(request):
    return render(request,'index.html')


def tweet_list(request):
    tweets = Tweet.objects.all().order_by("-created_at")
    return render(request,'tweet_list.html' ,{'tweets':tweets , 'ExtraKnowledge' : 'I am Passing Extra thing to frontend to get the data'})

@login_required
def tweet_create(request):
    if request.method == "POST":
        tweet_form = TweetForm(request.POST , request.FILES)
        tweet_info_form = TweetInfo(request.POST)
        if tweet_form.is_valid() and tweet_info_form.is_valid():
            tweet = tweet_form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            
            tweet_info = tweet_info_form.save(commit=False)
            tweet_info.user = request.user
            tweet_info.tweetId = tweet
            tweet_info_data_manuplated = tweet_info_form.cleaned_data["tweetTags"].split()
            tweet_info.tweetTagsSplitForm = tweet_info_data_manuplated
            tweet_info.save()
            return redirect('tweet_list')
    else:
        tweet_form =  TweetForm()
        tweet_info_form = TweetInfo()
        return render(request ,'tweet_form.html',{'tweet_form':tweet_form , 'tweet_info_form':tweet_info_form})
    
@login_required   
def tweet_edit(request,tweet_id):
    tweet = get_object_or_404(Tweet , pk=tweet_id, user = request.user)
    tweet_info = get_object_or_404(TweetInfoModel,tweetId=tweet_id,user=request.user)
    if request.method == "POST": 
        form = TweetForm(request.POST , request.FILES , instance = tweet)
        form_info = TweetInfo(request.POST,instance=tweet_info)
        if form.is_valid() and form_info.is_valid():
            tweet = form.save(commit=False)
            tweet.user = tweet.user
            tweet.save()
            tweet_info = form_info.save(commit=False)
            tweet_info.user = tweet_info.user
            tweet_info.tweetId = tweet_info.tweetId
            print(form_info.cleaned_data["tweetTags"])
            tweet_info_data_manuplated = form_info.cleaned_data["tweetInfo"].split()
            print(tweet_info_data_manuplated)
            tweet_info.tweetTagsSplitForm = tweet_info_data_manuplated
            tweet_info.save()
            return redirect('tweet_list')
    else:
        tweet_form = TweetForm(instance=tweet)
        tweet_info_form = TweetInfo(instance=tweet_info)
        # we have given instance because we are editing old tweet and there was some previous data
        return render(request,'tweet_form.html',{'tweet_form':tweet_form , 'tweet_info_form':tweet_info_form})

def tweet_detail(request,tweet_id):
    tweet = get_object_or_404(Tweet,pk=tweet_id)
    return render(request,'tweet_detail.html',{'tweet':tweet})

@login_required
def tweet_delete(request,tweet_id):
    tweet = get_object_or_404(Tweet , pk=tweet_id , user =request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect('tweet_list')
    else:
        return render(request,'tweet_confirm_delete.html',{'tweet':tweet})
    
    
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        print("value")
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')  # **Key Change: Ensure redirection after successful registration**
    else:
        print(request.method , "request")
        form = UserRegistrationForm()

    # **Key Change: Always render the form, even if POST data is invalid**
    return render(request, 'registration/register.html', {'form': form})


def search(request):
    if request.method == 'POST':
        tweets = Tweet.objects.all()
        searched_value = request.POST.get('search','')
        return render(request , 'result.html' , {'tweets' : tweets , 'searched_value':searched_value})
    else :
        print(request,"request")
        return redirect('tweet_list')