# Synopsis

This is a small web application that only accepts a POST request to the route
"/test". This route accepts two arguments "x" and "y" to then return a JSON
object {"sum":x+y}

# Usage
+ Run ```python3 -m venv .```
+ Activate virtual environment by ```source bin/activate```
+ Install dependencies ```pip3 install -r requirements.txt```
+ Run ```python3 app.py```

To test, simply run:
```curl -X POST http://0.0.0.0:5000/test --data '{"x": 4, "y": 2}' -H 'Content-Type: application/json'```

