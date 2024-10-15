## Flask - Vue - Crud

This is a project to learn how to connect Vue to Flask, following along [these instructions](https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/)


### To Do

- Add SQLite3 DB

##### Erorr Handling
- This tutorial only deals with the happy path. Handling errors is a separate exercise. Check your understanding and add proper error handling on both the front and back-end.
    - Backend: 
        - Database errors
        - Invalid inputs

##### GET Route
- Looking for an extra challenge? Write an automated test for this. Review this resource for more info on testing a Flask app.

##### POST Route
- Can you think of any potential errors on the client or server? Handle these on your own to improve user experience.

##### PUT Route
- Take a moment to think about how you would handle the case of an id not existing. What if the payload is not correct? Refactor the for loop in the helper as well so that it's more Pythonic.
- Challenge: Instead of using a new modal, try using the same modal for handling both POST and PUT requests.
- You can clean the component up by moving the methods that make HTTP calls to a utils or services file.
- Also, try to combine some of the methods that contain similar logic, like handleAddSubmit and handleEditSubmit.

##### Delete Route
- Instead of deleting on the button click, add a confirmation alert.
- Display a "No books! Please add one." message when no books are present in the table.

##### Alerts:
- Think about where showMessage should be set to false. Update your code.
- Try using the Alert component to display errors.
- Refactor the alert to be dismissible.
- Get alerts from backend responses