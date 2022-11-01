from django.shortcuts import redirect, get_object_or_404, render
from .models import Location, HotPlace, ImageHotPlace, Reviews, ImageReviews
from .forms import ReviewForm, HotPlaceForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.

def main(request):
    locations = Location.objects.all()
    context = {
        'locations' : locations
    }
    return render(request, 'reviews/index.html', context)

def hotlist(request):
    hotplace = HotPlace.objects.all()
    image = ImageHotPlace.objects.all()
    context = {
        'hotplace' : hotplace,
        'image' : image
    }
    return render(request, 'reivews/hotlist.html', context)

def hotdetail(request, pk):
    hotplace = get_object_or_404(HotPlace, pk=pk)
    review = Reviews.objects.filter(hotplace=hotplace)
    image = ImageHotPlace.objects.filter(hotplace=hotplace)
    context = {
        'hotplace' : hotplace,
        'review' : review,
        'image' : image,
    }
    return render(request, 'reviews/detail.html', context)

@login_required
def hotcreate(request):
    if request.method == 'POST':
        hotplace_form = HotPlaceForm(request.POST, request.FILES)
        if hotplace_form.is_valid():
            hotplace = hotplace_form.save(commit=False)
            hotplace.user = request.user
            hotplace.save()
            messages.success(request, '관광지 추가 완료')
    else:
        hotplace_form = HotPlaceForm()
    context = {
        'hotplace_form' : hotplace_form
    }
    return render(request, 'reviews/hotcreate.html', context)

@login_required
def reviewcreate(request, pk):
    hotplace = get_object_or_404(HotPlace, pk=pk)
    review_form = ReviewForm(request.POST)
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.hotplace = hotplace
        review.user = request.user
        review.save()
        context = {
            'title' : review.title,
            'content' : review.content,
            'image' : review.image,
            'grade' : review.grade,
            'username' : review.user.username
        }
        return JsonResponse(context)

@login_required
def delete(request, pk):
    review = get_object_or_404(Reviews, pk=pk)
    if request.user == review.user:
        review.delete()
        return redirect('reviews:index')
    else:
        messages.warning(request, '본인의 리뷰만 삭제할 수 있습니다.')
        return redirect('reviews:detail', pk)