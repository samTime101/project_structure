## API RESPONSE

`API ENDPOINT:/api/get/categories/`

## RESPONSE FOR GET REQUEST(200)
```json
{
    "categories": [
        {
            "id": 1,
            "name": "Computer Science",
            "subCategories": [
                {
                    "id": 1,
                    "name": "programming",
                    "subSubCategories": [
                        {
                            "id": 1,
                            "name": "C programming"
                        },
                        {
                            "id": 2,
                            "name": "Python Programming"
                        },
                        {
                            "id": 3,
                            "name": "Rust Programming"
                        }
                    ]
                },
                {
                    "id": 2,
                    "name": "DSA",
                    "subSubCategories": []
                },
                {
                    "id": 3,
                    "name": "OOP",
                    "subSubCategories": []
                },
                {
                    "id": 4,
                    "name": "Database",
                    "subSubCategories": []
                },
                {
                    "id": 5,
                    "name": "Web",
                    "subSubCategories": []
                }
            ]
        }
    ]
}
```