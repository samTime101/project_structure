
## API RESPONSE(THIS ROUTE REQUIRES AUTHENTICATION TOKEN)

> [!TIP]
>  U HAVE TO BE SUPERUSER TO CREATE CATEGORY 

`API ENDPOINT:/api/create/question/`

`
Authorization Bearer:<access_token>
`

## REQUEST FOR POST WITH ACCESS CORRECT TOKEN PROVIDED IN HEADER REQUEST
```json
{
  "questionText": "Which of the following are loop statements in C?",
  "questionType": "multiple",
  "options": [
    { "optionId": "A", "text": "for" },
    { "optionId": "B", "text": "while" },
    { "optionId": "C", "text": "switch" },
    { "optionId": "D", "text": "do-while" }
  ],
  "correctAnswers": ["A", "B", "D"],
  "difficulty": "easy",
  "categoryId": 1,
  "subCategoryId": [2],
  "subSubCategoryId": [1]
}
```

## RESPONSE (201)

```json
{
    "message": "Question created successfully",
    "question": {
        "id": "68a9a353ec508872ae4ec633",
        "questionText": "Which of the following are loop statements in C?",
        "questionType": "multiple",
        "options": [
            {
                "optionId": "A",
                "text": "for"
            },
            {
                "optionId": "B",
                "text": "while"
            },
            {
                "optionId": "C",
                "text": "switch"
            },
            {
                "optionId": "D",
                "text": "do-while"
            }
        ],
        "correctAnswers": [
            "A",
            "B",
            "D"
        ],
        "difficulty": "easy",
        "category": "Computer Science",
        "subCategory": [
            "DSA"
        ],
        "subSubCategory": [
            "C programming"
        ],
        "createdAt": "2025-08-23T11:17:39.901532",
        "updatedAt": "2025-08-23T11:17:39.901556"
    }
}
```