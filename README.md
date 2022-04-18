```
pip install fastapi
pip install "uvicorn[standard]"
```

to run:

```
uvicorn main:app --reload

uvicorn sql_app.main:app --reload
```

pages:

/docs
/redoc

Heroku shit

heroku ps:scale web=0
