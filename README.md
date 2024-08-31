# PERSONAL BUDGET TRACKER
#### Video Demo:  [CS50x 2024 Final Project: Personal Budget Tracker](https://youtu.be/Sm-D90pnNzI)
#### Description: This project aims to assist users in managing their finances by creating a customised budget tracker. It enables users to add expenses, make budgets, and monitor their spending over time. This project aims to give users a straightforward and practical tool for managing their personal finances, enabling them to make savings and refrain from overspending.

## Technologies Used
Frontend: HTML, CSS, JavaScript

Backend: Python, Flask

Template Engine: Jinja

For the backend, this project uses Flask, a powerful yet lightweight Python web framework. Using HTML, CSS, and JavaScript, the frontend is constructed to provide an intuitive user interface. The modern and designer-friendly Python templating language Jinja is used to render HTML pages dynamically in response to data and user input.

## Project Structure
* static: The project's static files, including JavaScript files, CSS stylesheets, and picture assets, are in this directory.
  * styles.css: The CSS rules for styling the web pages are contained in this file. It includes guidelines for changing the navbar brand element's text size and colour.
* templates: The HTML templates in this directory specify the organisation and design of the web pages. The Flask application dynamically generates these templates to produce the final web pages served to users.
  * apology.html: This template allows users to receive apology messages by extending the basic layout specified in layout.html. It has a picture showing a personalised meme with words taken from the Memegen API.
  * budget.html: The form for adding a new budget is rendered using this template. It adds form fields to enhance the basic layout specified in layout.html and allows users to specify the name and amount of the budget.
  * expense.html: The form for adding a new expense is rendered using this template. It adds form fields for choosing the budget, entering the expense category, and indicating the amount of the expense. It extends the basic layout defined in layout.html.
  * index.html: The budget tracker's main page is rendered using this template. It adds a form for choosing a budget and viewing expenses to the basic layout specified in layout.html.
  * index2.html: After the form is submitted, this template displays the budget tracker's home page. It shows a table with the expenses for the chosen budget, the total money allotted, and the balance due.
  * layout.html: This template establishes the standard layout for every web page inside the project. It has placeholders for displaying dynamic information and the header navigation bar.
  * login.html: The login form is rendered using this template. The basic layout specified in layout.html is expanded, and form fields are added for the username and password.
  * register.html: The registration form is rendered using this template. It adds form fields for entering the username, password, and password confirmation to the basic layout specified in layout.html.
* app.py: The primary Flask application, complete with route definitions for managing HTTP requests, is contained in this file. It lays out budgeting, data visualisation, spending control, and user identification procedures.
  * index Route ("/"): The budget tracker's home page is on this route. It handles both GET and POST requests.
    * GET Request: Renders the index.html template, displaying a form to view expenses and choose a budget.
    * POST Request: Handles the submission of the form, gets the details of the chosen budget from the database, computes the total cost of that budget, and renders the index2.html template with the cost information.
  * budget Route ("/budget"): Adding new budgets to the system is the responsibility of this route
    * GET Request: Generates the budget.html template, which includes an add-a-budget form.
    * POST Request: Handles the form submission, gets the user-entered budget name and amount, and adds the information to the database as a new budget entry.
  * login Route ("/login"): This route is responsible for login and user authentication.
    * GET Request: Generates the login.html template, which shows a form asking for the password and username.
    * POST Request: Handles the form submission, verifies the user's username and password, and logs them in if they match.
  * logout Route ("/logout"): this route logs the user out by deleting the session data.
    * GET Request: Takes the user to the login page while clearing the session data.
  * expense Route ("/expense"): Customers can include new costs in their spending plans with this route.
    * GET request: Renders the expense.html template, which includes a form for entering a new expense.
    * POST Request: This procedure handles the submission of the form, obtains the budget name, expenditure category, and user-entered amount, and adds the information as a new expense record to the database.
  * register Route ("/register"): This route is responsible for creating accounts and registering users.
    * GET Request: Generates a form asking for a username, password, and password confirmation by rendering the register.html template.
    * POST Request: Handles the form submission, verifies the user's inputs, creates a new user account and logs the user in if the inputs are correct.
* helpers.py: This file includes utility functions used throughout the project, such as the login_required decorator, which limits access to authenticated users, and the apology function, which renders error messages.
* personalbudgettracker.db: Three tables are included in this SQLite database file: users, budget, and expenses. User credentials are kept in the users table, budget information is kept in the budget table, and each user's specific spending information is kept in the expenses table.
