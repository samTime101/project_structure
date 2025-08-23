## API RESPONSE

`API ENDPOINT:/api/signin/`

## RESPONSE FOR GET REQUEST(405)
```json
{
    "detail": "Method \"GET\" not allowed."
}
```

## REQUEST FOR POST REQUEST

```json
{
    "email": "samipregminp@gmail.com",
    "password": "<correctpassword>"
}

```

## RESPONSE FOR THE FOLLOWING POST REQUEST(200)

```json
{
    "message": "User signed in successfully",
    "user": {
        "userId": 1,
        "email": "samipregminp@gmail.com",
        "username": "samipregminp",
        "phonenumber": "9842265590",
        "firstname": "samip",
        "lastname": "regmi",
        "is_active": true,
        "is_staff": true,
        "is_superuser": true
    },
    "tokens": {
        "access": "<token>",
        "refresh": "<token>"
    }
}
```

## RESPONSE FOR WRONG CREDENTIALS(400)

```json
{
    "non_field_errors": [
        "Invalid email or password"
    ]
}
```