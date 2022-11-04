from django.shortcuts import redirect, get_object_or_404, render
from .models import Location, HotPlace, ImageHotPlace, Reviews, ImageReviews, Location
from .forms import (
    ReviewForm,
    HotPlaceForm,
    HotPlaceImageForm,
    ReviewImageForm,
    HotUpdateForm,
    ReviewUpdateForm,
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponseForbidden
from django.views.decorators.http import require_POST

# Create your views here.


@login_required
def hotcreate(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == "POST":
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
            return redirect("reviews:hotlist", pk)
        else:
            messages.warning(request, "모든 항목을 입력해 주세요.")
    else:
        form = HotPlaceForm()
        image_form = HotPlaceImageForm()
    context = {"image_form": image_form, "form": form, "location": location}
    return render(request, "reviews/hotcreate.html", context)


def main(request):
    domestics = Location.objects.filter(country=True)
    overseas = Location.objects.filter(country=False)
    themes = HotPlace.objects.values("theme").distinct()
    context = {
        "domestics": domestics,
        "overseas": overseas,
        "themes": themes,
    }
    return render(request, "reviews/index.html", context)


def hotlist(request, pk):
    location = get_object_or_404(Location, pk=pk)
    hotplaces = HotPlace.objects.filter(location_id=pk)
    context = {
        "location": location,
        "hotplaces": hotplaces,
    }
    return render(request, "reviews/hotlist.html", context)


def hotdetail(request, pk):
    hotplace = get_object_or_404(HotPlace, pk=pk)
    reviews = Reviews.objects.filter(hotplace=hotplace)
    images = ImageHotPlace.objects.filter(hotplace=hotplace)
    context = {
        "hotplace": hotplace,
        "reviews": reviews,
        "images": images,
    }
    return render(request, "reviews/detail.html", context)


@login_required
def reviewcreate(request, pk):
    hotplace = get_object_or_404(HotPlace, pk=pk)
    review_form = ReviewForm(request.POST, request.FILES)
    image_form = ReviewImageForm(request.POST, request.FILES)
    images = request.FILES.getlist("image")
    if review_form.is_valid() and image_form.is_valid():
        review = review_form.save(commit=False)
        review.hotplace = hotplace
        review.user = request.user
        if len(images):
            for image in images:
                image_instance = ImageReviews(reviews=review, image=image)
                review.save()
                image_instance.save()
        else:
            review.save()
        return redirect("reviews:hotdetail", pk)
    else:
        review_form = ReviewForm()
        image_form = ReviewImageForm()
    context = {"review_form": review_form, "image_form": image_form}
    return render(request, "reviews/reviewcreate.html", context)


@login_required
def reviewdelete(request, pk):
    review = get_object_or_404(Reviews, pk=pk)
    if request.user == review.user:
        review.delete()
        return redirect("reviews:hotdetail", review.hotplace.pk)


@login_required
def hotupdate(request, pk):
    hotplace = get_object_or_404(HotPlace, pk=pk)
    if request.method == "POST":
        image_form = HotPlaceImageForm(request.POST, request.FILES, instance=hotplace)
        form = HotUpdateForm(request.POST, request.FILES, instance=hotplace)
        images = request.FILES.getlist("image")
        if form.is_valid() and image_form.is_valid():
            hotplace = form.save(commit=False)
            if len(images):
                for image in images:
                    image_instance = ImageHotPlace(hotplace=hotplace, image=image)
                    hotplace.save()
                    image_instance.save()
            else:
                hotplace.save()
            return redirect("reviews:hotdetail", pk)
    else:
        form = HotUpdateForm(instance=hotplace)
        image_form = HotPlaceImageForm(instance=hotplace)
    context = {
        "image_form": image_form,
        "form": form,
    }
    return render(request, "reviews/hotupdate.html", context)


def hotlist_theme(request, slug):
    if slug == "all":
        hotplaces = HotPlace.objects.all()
    else:
        hotplaces = HotPlace.objects.filter(theme=slug)
    context = {"hotplaces": hotplaces}
    return render(request, "reviews/hotlist_theme.html", context)


@login_required
def reviewupdate(request, pk):
    review = get_object_or_404(Reviews, pk=pk)
    review_form = ReviewForm(request.POST, request.FILES, instance=review)
    image_form = ReviewImageForm(request.POST, request.FILES, instance=review)
    images = request.FILES.getlist("image")
    if review_form.is_valid() and image_form.is_valid():
        review = review_form.save(commit=False)
        if len(images):
            for image in images:
                image_instance = ImageReviews(reviews=review, image=image)
                review.save()
                image_instance.save()
        else:
            review.save()
        return redirect("reviews:hotdetail", review.hotplace.pk)
    else:
        review_form = ReviewForm(instance=review)
        image_form = ReviewImageForm(instance=review)
    context = {"review_form": review_form, "image_form": image_form}
    return render(request, "reviews/reviewcreate.html", context)


"""
@require_POST
def likes(request, review_pk):
    if request.user.is_authenticated:
        # review = Reviews.objects.get(pk=review_pk)
        review = get_object_or_404(Reviews, pk=review_pk)
        if review.like_user.filter(pk=request.user.pk).exists():
            review.like_user.remove(request.user)
        else:
            review.like_user.add(request.user)
        return redirect("reviews:hotdetail", review_pk)
    else:
        return HttpResponseForbidden()
"""
