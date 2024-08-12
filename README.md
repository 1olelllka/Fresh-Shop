<h1>FreshShop</h1>
<h4>This is a grocery shop project, where you can buy vegetables and fruits. The project itself does not include payment system. Treat it as a simple CRUD project.</h4>
<h6>The project was originally created in December 2020. The purpose of the project was to learn and apply my knowledge about Django Framework. This is my very first project.</h6>
<h3>The frontend template:</h3>
<p>https://www.free-css.com/free-css-templates/page246/freshshop</p>

```diff
! This template was used ONLY for educational purposes !
```

- **Backend**:
  - Django v4.1.13
  - Django-Mptt (for the contact us feature)
  - SQLite
- **Frontend**:
  - HTML5 with DTL
  - CSS3
  - Bootstrap v4.1.0
  - JS (mostly provided by the template)


<h4>Important notices</h4>
<ul>
  <li>The contact us feature doesn't work unless you configured mptt service in settings.py - You need to add your credentials.</li>
  <li>The sample data was added by myself. As the current db is sqlite3, it isn't a big deal.</li>
  <li>In order to access admin panel -- username: testUser -- password: password1234</li>
  <li>For those who want to add photos to product catalogue, it's recommended to attach 400x400 photo.</li>
  <li>The project is on debug mode, as the static files won't load without it. I don't intend to set up reverse proxy like Nginx</li>
  <li>In settings.py the security key is visible. The project does not have any market value so I would think that this fact might be neglected</li>
</ul>

**Installation:**
*You need to have Docker and docker-compose installed*
```diff
docker compose up
```

<h3>Some Images from the project:</h3>
<hr>
<img width="1437" alt="Screenshot 2024-03-19 at 17 45 02" src="https://github.com/1olelllka/Fresh-Shop/assets/67587036/bdc074bf-3442-4349-a61c-94201561b4d5">
<img width="1440" alt="Screenshot 2024-03-19 at 17 47 33" src="https://github.com/1olelllka/Fresh-Shop/assets/67587036/c6cf5c87-d3a8-4ab4-865c-f94f9eb70818">
<img width="1440" alt="Screenshot 2024-03-19 at 17 48 35" src="https://github.com/1olelllka/Fresh-Shop/assets/67587036/af057865-ac87-4314-aee8-69b9211ba4a7">
<img width="1440" alt="Screenshot 2024-03-19 at 17 49 43" src="https://github.com/1olelllka/Fresh-Shop/assets/67587036/a5f7e091-17d2-4b0d-9a56-123e3e7d67d8">
<img width="1438" alt="Screenshot 2024-03-19 at 17 50 14" src="https://github.com/1olelllka/Fresh-Shop/assets/67587036/e78552aa-a144-4d06-a55f-217c6a35e186">