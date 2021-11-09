# Tradexa Technologies Private Limited

### Please Note 
* I have used a prebuild theme, Have not created it from scratch .
* I have added session based authentication in the login page and login is required to access the post route .
* If the user will press logout button the session will get deleted .

### Steps to Follow
1. Create an application that has two apps User and Product.
2. User with user and Post model
    - User: first_name, last_name, email, password, username
    - Post: user, text, created_at, updated_at 
    - Foreign key relationship exists between User and Post on Model level not on Database level. 

3. Products app with Product model. 
    - Product : name, weight, price, created_at, updated_at Both of the apps should use two different databases. Create a form that   an authenticated user can use to create a post.

4. Register all models on the admin dashboard.
