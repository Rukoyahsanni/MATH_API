import json

def is_armstrong(number):
    digits = [int(digit) for digit in str(abs(int(number)))]  # Ensure it works for negative numbers
    power = len(digits)
    return sum(d ** power for d in digits) == abs(int(number))

def is_prime(number):
    number = int(number)
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def is_perfect(number):
    number = int(number)
    return sum(i for i in range(1, number) if number % i == 0) == number

def number_properties(number):
    properties = []
    
    if is_armstrong(number):
        properties.append("armstrong")
    if int(number) % 2 != 0:
        properties.append("odd")
    else:
        properties.append("even")

    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "class_sum": sum(int(digit) for digit in str(abs(int(number)))),
        "fun_fact": "{} is an Armstrong number because {}".format(
            number, " + ".join([f"{d}^{len(str(int(number)))}" for d in str(abs(int(number)))])
        ) if is_armstrong(number) else "No special fun fact"
    }

def lambda_handler(event, context):
    try:
        # Extract number from query string
        query_params = event.get("queryStringParameters", {})
        number_str = query_params.get("number")

        if number_str is None:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": "Missing 'number' parameter"
                })
            }

        # Convert number to float first (to allow floating points)
        try:
            number = float(number_str)
        except ValueError:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": "Invalid number format"
                })
            }

        # Compute number properties
        result = number_properties(number)

        return {
            "statusCode": 200,
            "body": json.dumps(result)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
