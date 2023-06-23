1. api => interface to communicate betw. 2 softwares[allows 2 softwares to talk to each other]
2. mobile sends request to yt.& yt gives data to us [but only json data transfer is there] [waiter in hotel]
********** 
django
django-rest-framework             # from settings
**********
11111111111111111111111 -new update
**********
3. django-admin startproject demo
2. python manage.py startapp app1
3. models.py[class Book]   => [Tutorial 1: Serialization]
4. serializers.py[in app]   => [Tutorial 1: Serialization]
5. views.py => [Tutorial: 3. Class-based Views]
6. urls.py[in app]  => [Tutorial 4: Authentication & Permissions]
7. urls.py[in project] => path("api/v1/", include("app1.urls")),
8. admin.py
9. settings.py => [add "rest_framework" & "app1"]
3. python manage.py makemigrations => model created => api\migrations\0001_initial.py(see)
4. python manage.py migrate 
5. python manage.py runserver => [8000/api/v1/books/] => 8000/api/v1/books/1, 2.....

20. python manage.py createsuperuser [ab, ..., 12345]

