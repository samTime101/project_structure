![Author](https://img.shields.io/badge/author-samip--regmi-blue)


> [!IMPORTANT]  
> CURRENT BRANCH i.e `feat/jwt` WAS RENAMED FROM `feat/auth_check` 


TODOS FOR THE PROJECT AT  [TODOs.md](./markdowns/TODOs.md) 

API INFORMATION AT [API_RESPONSE.md](./markdowns/API_RESPONSE.md)

---

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
npm install
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

**directory:`project_structure/`**

```
python3 manage.py runserver
```

## FRONT END 

**directory:`react_frontend/`**

```
npm run 
```

