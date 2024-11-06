## Note 

To install all the dependencies inside the requriements file 
```bash 
# make sure you also upgrade your pip, it is not the latest
pip install --upgrade pip
sudo apt-get install python3-dev libpq-dev
pip install -r requirements.txt
```

* the .env in case you are using different port for the postgres container 
```bash 
postgresql+asyncpg://<username>:<password>@<hostname>:<port>/<database_name>

```
* To run the application
```bash 
uvicorn app.main:app  --reload 
uvicorn app.main:app --reload --port 8080
```


* In order to access the swagger docs
```bash 
# you can access in order to get the ui 
http :8080/docs
http :8080/redoc
```