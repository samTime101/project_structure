## API RESPONSE

`API ENDPOINT:/api/signin`

## REQUEST FOR POST REQUEST

```json
{
    "email": "samip@example.com",
    "password": "Superman123"
}

```

## RESPONSE FOR THE FOLLOWING POST REQUEST(200)

```json
{
    "message": "User signed in successfully",
    "user": {
        "userId": 4,
        "email": "samip@example.com",
        "username": "samip101",
        "phonenumber": "9801234567",
        "firstname": "Samip",
        "lastname": "Regmi",
        "is_active": true,
        "is_staff": false,
        "is_superuser": false
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