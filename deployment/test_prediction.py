import requests

# Using your live EC2 Public IP and the port 5000 you just opened
URL = "http://15.206.151.94:5000/predict" 

# Provide the exact file path to your sensor test CSV file on your computer
file_path = "deployment/test.csv"

try:
    with open(file_path, "rb") as f:
        response = requests.post(URL, files={"file": f})
    
    print("Status Code:", response.status_code)
    print("\n--- Model Evaluation Results ---")
    print(response.json())
except Exception as e:
    print("Error connecting to the server:", e)