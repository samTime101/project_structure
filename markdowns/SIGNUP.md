## API RESPONSE

`API ENDPOINT:/api/signup`

## RESPONSE FOR GET REQUEST(405)
```json
{
    "detail": "Method \"GET\" not allowed."
}
```

## REQUEST FOR POST REQUEST

```json
{
    "email": "new@new.com",
    "username": "new101",
    "phonenumber": "9801234566",
    "firstname": "Samip",
    "lastname": "Regmi",
    "password": "Superman123"
}

```

## RESPONSE FOR THE FOLLOWING POST REQUEST(201)

```json
{
    "message": "User created successfully",
    "user": {
        "userId": 5,
        "email": "new@new.com",
        "username": "new101",
        "phonenumber": "9801234566",
        "firstname": "Samip",
        "lastname": "Regmi"
    }
}
```

## IF REGISRETED USER TRIES TO SIGNIN WITH SAME CREDENTIALS(400)

```json
{
    "email": [
        "user with this email already exists."
    ],
    "username": [
        "user with this username already exists."
    ],
    "phonenumber": [
        "user with this phonenumber already exists."
    ]
}
```
