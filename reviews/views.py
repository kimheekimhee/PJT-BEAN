from django.shortcuts import redirect, get_object_or_404, render
from .models import Location, HotPlace, ImageHotPlace, Reviews, ImageReviews, Location
from .forms import ReviewForm, HotPlaceForm, HotPlaceImageForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.

def hotcreate(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        image_form = HotPlaceImageForm(request.POST, request.FILES)
        form = HotPlaceForm(request.POST, request.FILES)
        images = request.FILES.getlist("image")
        if form.is_valid() and image_form.is_valid():
            hotplace = form.save(commit=False)
            hotplace.location = location
            if len(images):
                for image in images:
                    image_instance = ImageHotPlace(hotplace=hotplace, image=image)
                    hotplace.save()
                    image_instance.save()
            else:
                hotplace.save()
            return redirect('reviews:hotlist', pk)
    else:
        form = HotPlaceForm()
        image_form = HotPlaceImageForm()
    context = {
        'image_form': image_form,
        'form': form,
        'location': location
    }
    return render(request, 'reviews/hotcreate.html', context)

def main(request):
    locations = Location.objects.all()
    context = {
        'locations' : locations
    }
    return render(request, 'reviews/index.html', context)

def hotlist(request, pk):
    location = get_object_or_404(Location, pk=pk)
    hotplaces = HotPlace.objects.filter(location_id=pk)
    images = ImageHotPlace.objects.all()
    context = {
        'location': location,
        'hotplaces' : hotplaces,
        'images' : images
    }
    return render(request, 'reviews/hotlist.html', context)

def hotdetail(request, pk):
    hotplace = get_object_or_404(HotPlace, pk=pk)
    reviews = Reviews.objects.filter(hotplace=hotplace)
    images = ImageHotPlace.objects.filter(hotplace=hotplace)
    context = {
        'hotplace' : hotplace,
        'reviews' : reviews,
        'images' : images,
    }
    return render(request, 'reviews/detail.html', context)

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