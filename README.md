# FreshShop - Freshness Picked Daily, Health Delivered Naturally! (Django)
This is a beginner-level grocery shop project created using Django, where users can browse, add, and manage fruits and vegetables.

---

## Project Overview

- **Backend**: Django v4.1.13
  - **Database**: SQlite3
- **Frontend**: HTML5, Django Template Language (DTL), CSS3, Bootstrap v4.1.0, Vanilla JS

## Installation and Setup

1. Go to the `settings.py` inside the `fresh_shop` directory:
   ```bash
   cd fresh_shop
   ```
2. Scroll down and change the following code by inserting your data:
   ```python
   EMAIL_HOST_USER = '<your-gmail>'     
   EMAIL_HOST_PASSWORD = '<your-password-or-code>'
   ```
   This is essential for Contact Us feature, as it sends a sample email to the user.
3. Make sure you have Docker and docker-compose installed.
4. Run the following from the project root:
   
   ```bash
   docker compose up
   ```
5. You are ready to use the app.

### Important Notices
  - Sample data includes preloaded products such as fruits and vegetables stored in the SQLite3 database.
  - In order to access admin panel on URI `/admin/`:
    
    ```plain
    username: testUser
    password: password1234
    ```
  - For those who want to add photos to product catalogue, it's recommended to attach 400x400 photo.
  - The project is currently running in debug mode, which is useful for development and testing. However, be aware that in production, this should be turned off for security reasons.
  - Although the security key is exposed here for simplicity, best practice in production is to use environment variables to keep sensitive data secure.

#### Disclamer
The frontend design was adapted from a free template for educational purposes only. It serves as a visual aid for learning, and the template can be found here: 
https://www.free-css.com/free-css-templates/page246/freshshop

---

## Screenshots
<img width="1437" alt="Screenshot 2024-03-19 at 17 45 02" src="https://github.com/1olelllka/Fresh-Shop/assets/67587036/bdc074bf-3442-4349-a61c-94201561b4d5">
<img width="1440" alt="Screenshot 2024-03-19 at 17 47 33" src="https://github.com/1olelllka/Fresh-Shop/assets/67587036/c6cf5c87-d3a8-4ab4-865c-f94f9eb70818">
<img width="1440" alt="Screenshot 2024-03-19 at 17 49 43" src="https://github.com/1olelllka/Fresh-Shop/assets/67587036/a5f7e091-17d2-4b0d-9a56-123e3e7d67d8">
