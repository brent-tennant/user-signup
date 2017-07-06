# user-signup

#Instructions

If the user's form submission is not valid, you should reject it and re-render the form with some feedback to inform the user of what they did wrong. The following things should trigger an error:

The user leaves any of the following fields empty: username, password, verify password.
The user's username or password is not valid -- for example, it contains a space character or it consists of less than 3 characters or more than 20 characters (e.g., a username or password of "me" would be invalid).
The user's password and password-confirmation do not match.
The user provides an email, but it's not a valid email. Note: the email field may be left empty, but if there is content in it, then it must be validated. The criteria for a valid email address in this assignment are that it has a single @, a single ., contains no spaces, and is between 3 and 20 characters long.
Each feedback message should be next to the field that it refers to.

For the username and email fields, you should preserve what the user typed, so they don't have to retype it. With the password fields, you should clear them, for security reasons.

If all the input is valid, then you should show the user a welcome page that uses the username input to display a welcome message of: "Welcome, [username]!"

Use templates (one for the index/home page and one for the welcome page) to render the HTML for your web app.
While we've covered how to specify different input types than just text (e.g., password and email), for this assignment do not use the email input type. Instead, just use text, which does not do any client-side validation. This will enable us to check that the server side validation is working by letting errors through the client side. You should, however, use type='password' for the password and password verification inputs, to hide the characters typed (this input type does not included any additional validation).
Submit
To turn in your assignment and get credit, follow the submission instructions.

Bonus Missions
Use a Regular Expression (also called a regex) to validate the input fields. See this article about Regular Expressions for more information.

If you haven't already, refactor your templates so that you are using a base template for the boilerplate HTML that is needed for both the home page and the welcome page, and template extensions for the additional HTML your app uses.
