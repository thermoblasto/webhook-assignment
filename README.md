# assignment
Wwebhook to read Json input

## Pre-requisite
- Docker engine installed and running
- Based on docker compose v1

## To initiate
 1. Clone the code into a empty working directory.
 2. Change to the directory and run the below code.
 
    ```
    docker-compose -f docker-compose.yml up --build
    ```
 3. Wait for the service to boot up.

## To Test
 1. Open a service like postman
 2. Put address as 127.0.0.1:8000/attribution
 3. For initial test, pass the sample json `Push API test example - Test` as the body
 4. For checking the results, connect to mysql database using the credentails in app.py and check the data in attribution_indentifier for id fields and attribution for rest of the info.
 5. Try with different json values for testing

![image](https://user-images.githubusercontent.com/14836328/166162913-3886a84c-9888-4fb2-8fd9-2be0330e0794.png)

![image](https://user-images.githubusercontent.com/14836328/166162922-8a6f4a9c-6263-4acd-a907-0a37cd85e74d.png)
![image](https://user-images.githubusercontent.com/14836328/166162935-1566b511-887e-4f4d-ad00-27cf9b812c95.png)
