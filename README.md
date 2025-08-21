![Author](https://img.shields.io/badge/author-samip--regmi-blue)

## TODO

### SQL (sqldb_app)
- [ ] Add models: 
  - `Category`
  - `SubCategory`
  - `SubSubCategory`
  - `Role`
  - `UserRole`

### MONGO
- [ ] Add mongo

### DJANGO 
- [ ] Add `/api/sigin` in `mcq_project/urls.py`

### FRONTEND (REACT)
- [ ] Implement Signup frontend using API
  - `/api/signup`

### COMPLETED
- [x] seperate `sqldb_app`
- [x] Separate `signin_app`
- [x] Separate `signup_app`


> [!NOTE]  
> APP PROJECT TUTORIAL FOLLOWED FROM [HERE](https://www.geeksforgeeks.org/reactjs/how-to-connect-django-with-reactjs/)

## TO RUN PROJECT

```
git clone https://github.com/samTime101/project_structure.git
cd project_structure
```

## VIRTUAL ENV

```
python3 -m venv <envname>
source <envname>/bin/activate
```

## REQUIREMENTS(DJANGO)

```
pip install django
pip install djangorestframework
python3 -m pip install django-cors-headers
```

## REQUIREMENTS(FRONTEND)

```
cd react_frontend
npm install bootstrap jquery axios
```

## DATABASE
```
python3 manage.py makemigrations sqldb_app
python3 manage.py migrate
python3 manage.py createsuperuser
```

> [!TIP]
> ADD A SUPERUSER TO SEE DATA IN FRONTEND


## DJANGO SERVER
```
python3 manage.py runserver
```

## FRONT END 
```
npm run 
```

