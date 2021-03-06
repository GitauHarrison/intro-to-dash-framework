# Dash Web Framework For Python

### Overview

Dash is primarily used for building web analytic applications. It is built on top of [Flask](https://flask.palletsprojects.com/en/1.1.x/), [Plotly.js](https://plotly.com/javascript/) and [React.js](https://reactjs.org/) to enhance data visualization with highly custom user interfaces in pure Python. It is best suited to work with data in Python.

### Installation

To get started with Dash, you will need to create an application. In your terminal, create a project folder using `mkdir` command:

```python
$ mkdir dash_app # create project folder
$ cd dash_app # navigate into the project folder
```

Create and activate your virtual environment:

```python
$ mkvirtualenv venv # I am using virtualenvwrapper
```

Install dash using `pip3`:

```python
(venv)$ pip3 install dash
(venv)$ pip3 install pandas

```

### Create sample application

With the project setup complete, you will need to create a python file called `app.py` inside your project folder:

```python
(venv)$ touch app.py
```

Create a sample web app as seen in the `app.py` file. It is recommended that you write the code line after line rather than copying and pasting it.

### Testing

Run your code as follows:

```python
(venv)$ python3 app.py

# Output
Dash is running on http://127.0.0.1:8050/

 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
```

Click on the localhost URL seen in your terminal to open the app in your default web browser. Alternatively, you can paste the URL http://127.0.0.1:8050/ in your browser tab to see the application.

![Example Graph](/images/example_graph.png)

------------------------------

If you do not wish to create your own project but would rather use this project's files, you will need to:

1. Clone this repo to your local machine:

```python
$ git clone git@github.com:GitauHarrison/intro-to-dash-framework.git
```

2. Create and activate your virtualenvironment:

```python
$ mkvirtualenv venv # I am using virtualenvwrapper
```

3. Install used dependancies:

```python
(venv)$ pip3 install -r requirements.txt
```

4. Run your application:

```python
(venv)$  python3 app.py # replace app.py with the other files to test them out too
```

5. Access the application in your web browser by clicking on the URL in your terminal or pasting that link in a tab in your browser. You should be able to see the web application.