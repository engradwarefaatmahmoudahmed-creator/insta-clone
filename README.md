# 📸 Insta Clone

A full-stack Instagram-style social media application built with **Python and Django**.

This project demonstrates the development of a social media platform with user authentication, profiles, posts, likes, comments, following, search, and notifications.

---

## 🚀 Features

### 👤 User Authentication & Profiles

* User registration
* User login and logout
* Custom User Model
* Profile picture
* User bio
* Edit profile
* User profile pages

### 👥 Social Features

* Follow and unfollow users
* Followers and following counts
* Search for users
* Personalized feed

### 📸 Posts

* Create posts with images
* Add captions
* View post details
* Like and unlike posts
* Delete your own posts

### 💬 Comments

* Add comments to posts
* Display comments
* Delete your own comments

### 🔔 Notifications

* Follow notifications
* Like notifications
* Comment notifications
* Unread notifications counter

### 📱 Responsive Design

* Responsive layout
* Mobile-friendly interface
* Clean Instagram-inspired UI

---

## 🛠️ Technologies

* **Python**
* **Django**
* **SQLite**
* **HTML5**
* **CSS3**
* **Pillow**
* **Git & GitHub**

---

## 📂 Project Structure

```text
Insta Clone/
│
├── accounts/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── posts/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── notifications/
│   ├── migrations/
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── insta_clone/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│   └── base.html
│
├── static/
│   └── css/
│       └── style.css
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/engradwarefaatmahmoudahmed-creator/insta-clone.git
```

### 2. Navigate to the project

```bash
cd insta-clone
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Create a superuser

```bash
python manage.py createsuperuser
```

### 8. Run the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

---

## 🧪 Project Testing

The project was tested using Django's system check command:

```bash
python manage.py check
```

Result:

```text
System check identified no issues (0 silenced).
```

Core application features were also manually tested, including:

* User authentication
* Profiles
* Posts
* Likes
* Comments
* Following and unfollowing
* User search
* Notifications

---

## 🎯 Project Goals

The main goal of this project was to build a practical Django application that demonstrates real-world backend development concepts, including:

* Django Models
* Views and URLs
* Templates
* Forms
* Authentication
* Database relationships
* File and image uploads
* User interactions
* Notifications
* CRUD operations
* Responsive frontend design

---

## 🔮 Future Improvements

Possible future improvements include:

* Direct messaging
* Stories
* Post sharing
* Hashtags
* Advanced search
* Pagination
* REST API using Django REST Framework
* AJAX-based interactions
* Production deployment
* PostgreSQL database
* Cloud media storage

---

## 👩‍💻 Author

**Radwa Refaat Mahmoud Ahmed**

Backend Django Developer | Python & Django Instructor | Software Engineer
