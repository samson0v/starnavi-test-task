# Starnavi Test Task

## Tech stack
1. python 3.9
2. Django 3.1.7
3. Django Rest Framework 3.12.2
4. PostgreSQL 13

## Setup project
1. Clone GitHub repository.
2. Create .env file in system python module (there is .env.example file to see what fields are required). Make sure you fill in all required fields. Without them django project can't run the server.
3. Create virtualenv (run the next command in your terminal "python -m venv venv").
4. Install all required dependencies ("pip install -r requirements.txt").
5. Run migrations (python manage.py migrate).
6. Run server (python manage.py runserver).

## Api Endpoints
**POSTS ACTIONS**
1. **api/posts/** - return all posts
2. **api/posts/:id/** - return specific post
3. **like_or_dislike** - like or dislike specific post
4. **api/users/:id/** - return specific user
5. **api/users/:id/user_activity/** - return specific user activity
6. **api/likes/:id/** - return specific like
7. **api/analytics/** - return analytics about how many likes was made

**USER AUTH**
1. **api/api-sign-up-user/** - register new user
2. **api-auth/login** - user login
3. **api-token-auth/** - user login by JWT (Authorization: JWT [you_token])
4. **api-auth/logout** - user logout

## Support
**Feel free to message me on my email about any technical issues!**
