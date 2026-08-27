# 📸 Insta Clone

A full-stack Instagram-style social media application built with **Python and Django**.

This project demonstrates a real-world social media platform with user authentication, profiles, posts, likes, comments, following, search, notifications, and responsive UI.

---

## 🚀 Features

### 👤 Authentication & Profiles

* User registration
* User login and logout
* Custom Django User Model
* Unique email address
* Profile picture
* User bio
* Edit profile
* User profile pages

### 👥 Social Features

* Follow and unfollow users
* Followers and following counts
* Personalized feed
* User search
* Social interactions between users

### 📸 Posts

* Create posts with images
* Add captions
* Home feed
* Following feed
* Post details
* Like and unlike posts
* Delete your own posts

### 💬 Comments

* Add comments to posts
* Display post comments
* Delete your own comments

### 🔔 Notifications

* Follow notifications
* Like notifications
* Comment notifications
* Unread notifications counter
* Read/unread notification state

### 📱 Responsive UI

* Responsive layout
* Mobile-friendly design
* Instagram-inspired interface
* Clean and modern CSS styling

---

## 🛠️ Tech Stack

| Technology | Usage                |
| ---------- | -------------------- |
| **Python** | Backend programming  |
| **Django** | Web framework        |
| **SQLite** | Development database |
| **HTML5**  | Page structure       |
| **CSS3**   | Responsive UI        |
| **Pillow** | Image processing     |
| **Git**    | Version control      |
| **GitHub** | Source code hosting  |

---

## 🏗️ Project Architecture

The project is organized into separate Django applications according to their responsibilities:

```text
Insta Clone/
│
├── accounts/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── posts/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
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

## 🧠 Django Concepts Demonstrated

This project was built to practice and demonstrate practical Django backend development concepts:

* Django Models
* Model Relationships
* `ForeignKey`
* `ManyToManyField`
* Custom User Model
* Authentication
* Forms
* Views
* URL Routing
* Templates
* CRUD Operations
* File and Image Uploads
* User Permissions
* Notifications
* Database Relationships
* Automated Testing
* Responsive Frontend Design

---

## 🧪 Testing

The project includes automated tests covering important application functionality.

Tests currently cover:

* User creation
* Email uniqueness
* User authentication
* Login and logout
* Follow and unfollow
* Post creation
* Post validation behavior
* Comments
* Comment relationships
* Likes and unlikes
* Multiple users liking posts
* Notifications
* Read/unread notifications

Run the complete test suite with:

```bash
python manage.py test
```

Current result:

```text
Found 14 test(s).

Ran 14 tests

OK
```

Django system checks also pass successfully:

```bash
python manage.py check
```

Result:

```text
System check identified no issues (0 silenced).
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

### 6. Apply migrations

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

Open the application:

```text
http://127.0.0.1:8000/
```

---

## 🔐 Security Notes

For development, the project uses SQLite and Django's development server.

Before production deployment, the following should be configured:

* Environment variables for secrets
* `DEBUG = False`
* Production `ALLOWED_HOSTS`
* PostgreSQL or another production database
* Secure media storage
* Static file collection
* HTTPS
* Production WSGI/ASGI configuration

---

## 🔮 Future Improvements

Planned improvements include:

* 💬 Direct messaging
* 📖 Stories
* 🔗 Post sharing
* #️⃣ Hashtags
* 🔎 Advanced search
* 📄 Pagination
* ⚡ AJAX interactions
* 🔌 Django REST Framework API
* 🗄️ PostgreSQL
* ☁️ Cloud media storage
* 🚀 Production deployment
* 🧪 Expanded integration and view tests

---

## 📌 Project Status

**Current status: Active Development**

The core social media functionality is implemented and tested.

The project is being continuously improved with additional backend features, testing, UI improvements, and production-ready architecture.

---

## 👩‍💻 Author

**Radwa Refaat Mahmoud Ahmed**

**Backend Django Developer | Python & Django Instructor | Software Engineer**

---

## 📄 License

This project is intended for educational and portfolio purposes.
