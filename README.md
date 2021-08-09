# django_time_task_app


## Asynchronous Tasks With Django and Celery 

## #1 why we use celery and Redis with django??
If a long process is part of your application's workflow, you can use Celery to execute that process in the background, as resources become available, so that your application can continue to respond to client requests.
And 
This extension enables you to store the periodic task schedule in the database.
The periodic tasks can be managed from the Django Admin interface, where you can create, edit and delete periodic tasks and how often they should run.


## #2 Project Setup
### #1 Pacakages Requirements 
	Python
	Django
	django_celery_beat
	django_celery_results
	celery==4.4.7
	redis==3.5.3
	[Project Templates Ready to use](https://github.com/Kumar021/django_time_task_app/blob/master/code/requirements.txt) 

## # 2 How to use my project templates(https://github.com/Kumar021/django_time_task_app)

 - [ ] #1 Clone proejct
 - [ ] #2 Install Python & Create Virtual Environments and activate
 - [ ] #3 Install redis
 - [ ] #4 pip install -r requirements.txt
 - [ ] #5 python manage.py migrate
 - [ ] #6 Start django server - python manage.py runserver 
 - [ ] #7 Let's go to django admin localhost:8080/admin.
 - [ ] #8 Let's make a crontab Crontab > Add crontab
	![alt text](https://github.com/Kumar021/django_time_task_app/blob/master/code/img/3dd9pno3z8miartnckan.png?raw=true)

 - [ ]  #9 Let's create a crontab .Here I created one
 ![alt text](https://github.com/Kumar021/django_time_task_app/blob/master/code/img/bojci16hsrh89fnko09z.png?raw=true)
 - [ ]  #10 Let's create a periodic task
	Click Periodic tasks > Add. Create a new name of your choice. Find send_notification task that we have created up there
	
 - [ ]  #11 Schedule > Crontab Schedule > Find the crontab you just created.
	Add the Start Datetime
	This is where you pass the arguments subject and message
 - [ ]  #12 Start redis-server 
 - [ ]  #13 Start django serve 
 - [ ]  #14 Start celery celery -A djangocelery(app name) worker --loglevel=info in dieffrent terminal
 - [ ]  #15 Start celery beat in different terminal 
	celery -A djangocelery(app name) beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
 - [ ]  #16 Let's check out the terminal of celery beat for output

	If you want to learn more about django_celery_beat
	https://django-celery-beat.readthedocs.io/en/latest/



	

