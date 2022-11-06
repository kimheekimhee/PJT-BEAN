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
lst = ['제주', '서울', '부산', '강원도', '인천', '충청도','전라도', '경기도']
for i in lst:
    location = Location.objects.create()
    location.location = i
    location.country = 0
    location.save()

for i in lst:
    location = ImageLocation.objects.create(image=i[0], location_id=i[1])
    location.save()
lst = [
('images/제주1.jpg',1),
('images/제주2.jpg',1),
('images/제주3.jpg',1),
('images/서울1.jpg',2),
('images/서울2.jpg',2),
('images/서울3.jpg',2),
('images/부산1.jpg',3),
('images/부산2.jpg',3),
('images/부산3.jpg',3),
('images/강원도1.jpg',4),
('images/강원도2.jpg',4),
('images/강원도3.jpg',4),
('images/인천1.jpg',5),
('images/인천2.jpg',5),
('images/인천3.jpg',5),
('images/충청도1.jpg',6),
('images/충청도2.jpg',6),
('images/충청도3.jpg',6),
('images/전라도1.jpg',7),
('images/전라도2.jpg',7),
('images/전라도3.jpg',7),
('images/경기도1.jpg',8),
('images/경기도2.jpg',8),
('images/경기도3.jpg',8),
('images/미국1.jpg',9),
('images/러시아1.jpg',10),
('images/스페인1.jpg',11),
('images/영국1.jpg',12),
('images/싱가포르1.jpg',16),
('images/프랑스1.jpg',15),
('images/홍콩1.jpg',14),
('images/일본1.jpg',13)]