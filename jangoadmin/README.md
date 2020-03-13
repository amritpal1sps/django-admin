# jangoadmin<br>
- python3.6 -m pip install django<br>
- python3.6 -m pip install djangorestframework<br>
- sudo apt-get install libmysqlclient-dev<br>
- python3.6 -m pip install mysqlclient<br>
- python3.6 -m pip install boto3<br>
- python3.6 -m pip install django-storages<br>
- python3.6 -m pip install python-decouple<br>
- python3.6 -m pip install certifi<br>
- python3.6 -m pip install schedule<br>
- python3.6 manage.py migrate<br>
- python3.6 manage.py createsuperuser<br>
- python3.6 manage.py runserver<br>
<br>
# .env
- DEBUG=True/False<br>
- DBPWD=root<br>
- DBUSR=root<br>
- DBHOST=localhost<br>
- DBNAME=jadmin<br>
- EMAIL_HOST=somehost<br>
- EMAIL_HOST_USER=someuser<br>
- EMAIL_HOST_PASSWORD=somepassword<br>
- EMAIL_PORT=587/25<br>
- AWS_ACCESS_KEY_ID=someid<br>
- AWS_SECRET_ACCESS_KEY=somekey<br>
- AWS_STORAGE_BUCKET_NAME=somename<br>
- AWS_STORAGE_BUCKET_RGN=us-east-1<br>
- AWS_STORAGE_URL=https://s3.amazonaws.com/your-bucket-name/<br>
- GOOGLE_API_KEY=your-google-key<br>
- APIURL=http://192.168.0.124:8000/api/<br>
- WEBURL=http://192.168.0.124:8000/<br>


Additional modifications done in 2020:
1. Fixtures can be used instead of seeders.
2. Angular JS integrated instead of bootstrap in templates
3. Decorators has been added for login required or superadmin required.
4. Serializers has been added.