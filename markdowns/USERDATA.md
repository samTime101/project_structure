## API RESPONSE(THIS ROUTE REQUIRES AUTHENTICATION TOKEN)

`API ENDPOINT:/api/user/`

`
Authorization Bearer:<access_token>
`

## RESPONSE FOR GET WITH NO ACCESS TOKEN PROVIDED IN HEADER REQUEST(401)
```json
{
    "detail": "Authentication credentials were not provided."
}
```

## RESPONSE FOR GET WITH ACCESS INCORRECT TOKEN PROVIDED IN HEADER REQUEST(401)
```json
{
    "detail": "Given token not valid for any token type",
    "code": "token_not_valid",
    "messages": [
        {
            "token_class": "AccessToken",
            "token_type": "access",
            "message": "Token is invalid"
        }
    ]
}
```


## RESPONSE FOR GET WITH ACCESS CORRECT TOKEN PROVIDED IN HEADER REQUEST(200)
```json
{
    "userId": 4,
    "email": "srijanregmi44@gmail.com",
    "username": "srijanregmi44",
    "phonenumber": "9816365845",
    "firstname": "srijanregmi",
    "lastname": "regmi",
    "is_active": true,
    "is_staff": false,
    "is_superuser": false
}
```
