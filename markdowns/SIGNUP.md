## API RESPONSE

`API ENDPOINT:/api/signup`

## RESPONSE FOR GET REQUEST(200)
```json
{
    "message": "User list retrieved successfully",
    "users": [
        {
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
        {
            "userId": 2,
            "email": "john.doe@example.com",
            "username": "john_doe",
            "phonenumber": "9876543210",
            "firstname": "John",
            "lastname": "Doe",
            "is_active": true,
            "is_staff": false,
            "is_superuser": false
        }
    ]
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
