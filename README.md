# CS361-Assignment 9: Microservice Implementation (Milestone #2) - Communication Contract

# How to programmatically REQUEST data from this microservice

This microservice for pet health forum works with HTTP request, which you can directly call from the "Postman" website.
I will explain the Postman application in the receive data method, but in this one, I would like to explain how you could
receive the HTTP Request basically, from only using couple more codes to execute the HTTP Request. Since it is written in 
Python Flask, you can programatically use "requests" library, such as using the requests.get("http://localhost:5000/posts/1"), 
then add the response.json() to the post, and call it with print(post).

# How to programatically RECEIVE data from this microservice

When you make the request in this microservice, you will receive response in the JSON format. Again, you can receive the
data from the Postman website, or in Python, you can use the requests library for receiving, with the same concept used in
requesting the data above. For using the Postman, you could first go through the method you would like to receive the data,
such as GET. Then, you can enter the "http://localhost:5000/posts/1" to the URL bar, and press the send button simply. 
For the POST, PUT, and DELETE methods, you need to navigate through the body tab just below the URL bar, and you can select
raw, then from the dropdown on right side, click JSON. After doing all of that, you need to enter the data in the text area
which you would like to request such as:

{
    "title": "My dog's health",
    "content": "My dog is having a health issue.",
    "author": "John Doe",
    "time": "Current Date&Time"
}

This is how I worked in the POST method of this microservice.

In the REQUEST data part, I explained how you could request the data from using the request library in Python, and in the
RECEIVE data part, I explained how you could do that in the application Postman. Personally, I use the Postman application
for requesting and receiving the data, because it was efficient, and direct.

# UML Diagram

![UML Diagram](https://github.com/altindeu/CS361-Milestone-2/assets/71780291/ef573adc-e1f4-45bd-84c2-aedd1aa58a4d)


