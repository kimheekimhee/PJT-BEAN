from django.test import TestCase

# Create your tests here.
location = Location.objects.get(location='서울')
for i in range(20):
    hotplace = HotPlace.objects.create()
    hotplace.hotplace = '서울시청'
    hotplace.addr = '서울'
    hotplace.x = '126.978652258309'
    hotplace.y = '37.566826004661'
    hotplace.theme = '관광'
    hotplace.country = '국내'
    hotplace.content = i
    hotplace.location_id = location.pk
    hotplace.save()

lst = ['미국', '러시아', '스페인', '영국', '일본', '홍콩', '프랑스', '싱가포르']

for i in lst:
    location = Location.objects.create()
    location.location = i
    location.country = 0
    location.save()
