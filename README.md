# Number Classification API

## Overview
This is a simple **Number Classification API** built using **AWS Lambda** and **API Gateway**. It classifies numbers based on specific criteria and provides responses accordingly.

---

## 🚀 About This Project  

This project utilizes **AWS Lambda** for serverless execution and **API Gateway** for managing HTTP requests. It is designed to efficiently handle number classification logic with minimal infrastructure management.

### **Key Features**
- 📌 Serverless architecture using AWS Lambda
- 🌍 API exposed via AWS API Gateway
- ⚡ Fast and scalable number classification

---

## 🔧 Technologies & Resources Used  
- **AWS Lambda** – Serverless function execution  
- **AWS API Gateway** – HTTP request handling  
- **Python** – Core programming language  

---

## 🛠️ Setup & Deployment  

### **1️⃣ Clone the repository**  
```sh
git clone https://github.com/Rukoyahsanni/MATH_API.git
cd MATH_API


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

