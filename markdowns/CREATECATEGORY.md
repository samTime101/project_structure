## API RESPONSE(THIS ROUTE REQUIRES AUTHENTICATION TOKEN)

> [!TIP]
>  U HAVE TO BE SUPERUSER TO CREATE CATEGORY 

`API ENDPOINT:/api/create/category/`

`
Authorization Bearer:<access_token>
`


## REQUEST FOR POST WITH ACCESS CORRECT TOKEN PROVIDED IN HEADER REQUEST
```json
{
    "categoryName": "Computer Science"
}
```


## RESPONSE (201)

```json
{
    "message": "Category created successfully",
    "category": {
        "id": 6,
        "name": "Computer Science"
    }
}
```