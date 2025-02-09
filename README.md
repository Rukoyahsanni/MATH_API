# Number Classification API

## Overview
This API provides information about a given number, including its properties such as being prime, perfect, Armstrong, even/odd classification, and a fun fact about it.

## Endpoint
```
GET <your-url>/api/classify-number?number=<integer>
```

## Request Parameters
- `number`: An integer value passed as a query parameter.

## Response Format
### Success Response (200 OK)
```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "class_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### Error Response (400 Bad Request)
```json
{
  "number": "alphabet",
  "error": true
}
```

## Functionality
- Accepts `GET` requests with a `number` parameter.
- Returns JSON in the specified format.
- Handles edge cases gracefully (e.g., non-numeric inputs, negative numbers, and numbers with multiple properties).
- Provides appropriate HTTP status codes.

## Deployment and Hosting
- The code must be hosted on GitHub.
- The repository must be public and include a well-structured `README.md` file.

