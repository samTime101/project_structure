## API RESPONSE(THIS ROUTE REQUIRES AUTHENTICATION TOKEN)

> [!TIP]
>  U HAVE TO BE SUPERUSER TO CREATE CATEGORY 

`API ENDPOINT:/api/create/subcategory/`

`
Authorization Bearer:<access_token>
`


## REQUEST FOR POST WITH ACCESS CORRECT TOKEN PROVIDED IN HEADER REQUEST
```json
{
  "subCategoryName": "Web",
  "categoryID": 1
}
```


## RESPONSE (201)

```json
{
    "message": "Sub Category created successfully",
    "subcategory": {
        "id": 5,
        "name": "Web",
        "categoryId": 1,
        "categoryName": "Computer Science"
    }
}
```