# News Backend




#### Requirements

- Python 3.6.5
- Django==2.0.4
- pytz==2018.4

See requirements.txt for full list of backend dependencies

```
mkdir backend
git clone http://dms-submissions.customappsteam.co.uk/assessments/robinm.git
cd robinm
git checkout backend

source venv/bin/activate
cd pressford
python3 manage.py runserver
```

Migrations

```
python3 manage.py makemigrations
python3 manage.py migrate
```

```
username: tester
password: 42uauk9f
```

## Testing the Endpoints

Replace :id with the appopriate id from DB

- [http://localhost:8000/news/](http://localhost:8000/news/)
- [http://localhost:8000/news/:id](http://localhost:8000/news/:id)
- [http://localhost:8000/news/:id/comments](http://localhost:8000/news/:id/comments)
- [http://localhost:8000/news/:id/comments/:id](http://localhost:8000/news/:id/comments/:id)

### Usage

Admin/Superusers and publisher will login to the backend on [http://localhost:8000/admin/](http://localhost:8000/admin/) to create, update and delete news articles (http://localhost:3000/) to read articles, like and comment (in the future)

To add a news article on the backend go to News under News_Api and Users can be added under Authorization and Authenitcation.
