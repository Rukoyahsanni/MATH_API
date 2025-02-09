import json

def is_armstrong(number):
    number = abs(int(number))  # Ensure it's an integer
    digits = [int(d) for d in str(number)]
    power = len(digits)
    return sum(d ** power for d in digits) == number

def is_prime(number):
    if number < 2:  
        return False
    number = int(number)
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def is_perfect(number):
    if number < 1:  
        return False
    number = int(number)
    return sum(i for i in range(1, number // 2 + 1) if number % i == 0) == number

def number_properties(number):
    properties = ["odd" if int(number) % 2 != 0 else "even"]
    
    if is_armstrong(number):
        properties.append("armstrong")

    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "class_sum": sum(int(d) for d in str(abs(int(number)))),
        "fun_fact": (
            f"{number} is an Armstrong number because " + 
            " + ".join([f"{d}^{len(str(int(number)))}" for d in str(abs(int(number)))])
        ) if is_armstrong(number) else "No special fun fact"
    }

def lambda_handler(event, context):
    try:
        query_params = event.get("queryStringParameters", {})
        number_str = query_params.get("number")

        if number_str is None:
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"error": True, "message": "Missing 'number' parameter"})
            }

        try:
            number = float(number_str)  # Ensure it's a valid number
        except ValueError:
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"error": True, "message": "Invalid number format"})
            }

        # Compute number properties
        result = number_properties(number)

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"success": True, **result})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": True, "message": str(e)})
        }
