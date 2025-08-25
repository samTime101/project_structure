## API RESPONSE

`API ENDPOINT:/api/signup/`

## RESPONSE FOR GET REQUEST(405)
```json
{
    "detail": "Method \"GET\" not allowed."
}
```

## REQUEST FOR POST REQUEST

```json
{
    "email": "<email>",
    "username": "srijanregmi44",
    "phonenumber": "<phonenumber>",
    "firstname": "srijanregmi",
    "lastname": "regmi",
    "password": "<password>"
}

```

## RESPONSE FOR THE FOLLOWING POST REQUEST(201)

```json
{
    "message": "User created successfully",
    "user": {
        "userId": 4,
        "email": "<email>",
        "username": "srijanregmi44",
        "phonenumber": "<phonenumber>",
        "firstname": "srijanregmi",
        "lastname": "regmi"
    },
    "tokens": {
        "access": "<token>",
        "refresh": "<token>"
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
