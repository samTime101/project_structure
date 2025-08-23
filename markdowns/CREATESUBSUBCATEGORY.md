## API RESPONSE(THIS ROUTE REQUIRES AUTHENTICATION TOKEN)

> [!TIP]
>  U HAVE TO BE SUPERUSER TO CREATE SUB SUB CATEGORY 

`API ENDPOINT:/api/create/subsubcategory/`

`
Authorization Bearer:<access_token>
`


## REQUEST FOR POST WITH ACCESS CORRECT TOKEN PROVIDED IN HEADER REQUEST
```json
{
  "subSubCategoryName": "Rust Programming",
  "subCategoryID": 1
}


```


## RESPONSE (201)

```json
{
    "message": "Sub SubCategory created successfully",
    "subsubcategory": {
        "id": 3,
        "name": "Rust Programming",
        "subCategoryId": 1,
        "subCategoryName": "programming",
        "categoryId": 1,
        "categoryName": "Computer Science"
    }
}
```