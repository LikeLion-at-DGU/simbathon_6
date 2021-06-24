from django.shortcuts import render
from review.models import Review
from django.contrib.auth.models import User

# Create your views here.
def mypage(request):
    user=request.user
    reviews=Review.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'reviews':reviews})
