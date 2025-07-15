# 📅 Event Management API

**A containerized Django REST API for managing events and user registrations.**

Features:
- JWT authentication
- User registration
- Event CRUD (Create, Read, Update, Delete)
- Event registration with email notifications
- Event filtering by date, location, and title
- Swagger API documentation

---

## 🚀 Getting Started

### 🧰 Prerequisites
Make sure you have installed:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## 🐳 Deployment

### 1️⃣ Clone the repository:
```bash
git clone https://github.com/<your-username>/event-management-api.git
cd event-management-api
````

---

### 2️⃣ Create `.env` file:

In the project root, create a file named `.env` and paste this content:

```ini
# Database
POSTGRES_DB=eventdb
POSTGRES_USER=eventuser
POSTGRES_PASSWORD=eventpass
POSTGRES_HOST=db
POSTGRES_PORT=5432

# Django superuser
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@gmail.com
DJANGO_SUPERUSER_PASSWORD=1234

# Email settings
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=example@gmail.com
EMAIL_HOST_PASSWORD=examplepassword
DEFAULT_FROM_EMAIL=example@gmail.com
```

---

### 3️⃣ Build and start containers:

```bash
docker-compose up --build
```

---

## ✅ This will:

* 🔨 Build the Docker images
* 🗄️ Apply database migrations
* 👤 Create a Django superuser with credentials from `.env`
* 🌐 Start the API and PostgreSQL

---

## 🌐 Access the application

| Service             | URL                                                          |
| ------------------- | ------------------------------------------------------------ |
| 📖 **API root**     | [http://localhost:8000/](http://localhost:8000/)             |
| 📝 **Swagger Docs** | [http://localhost:8000/docs/](http://localhost:8000/docs/)   |
| 🔐 **Django Admin** | [http://localhost:8000/admin/](http://localhost:8000/admin/) |

Log in to the admin panel using:

```
Username: admin
Password: 1234
```

---

## 🔐 Authentication

The API uses **JWT tokens** for authentication.

### Obtain token:

```http
POST /api/token/
Content-Type: application/json

{
  "username": "admin",
  "password": "1234"
}
```

### Refresh token:

```http
POST /api/token/refresh/
Content-Type: application/json

{
  "refresh": "<your_refresh_token>"
}
```

Use the access token in the `Authorization` header:

```
Authorization: Bearer <access_token>
```

---


### 📖 API Endpoints

#### 🧑 Users

| Method | Endpoint               | Description         |
| ------ | ---------------------- | ------------------- |
| POST   | `/api/users/register/` | Register a new user |

#### 📅 Events

| Method | Endpoint            | Description                          |
| ------ | ------------------- | ------------------------------------ |
| GET    | `/api/events/`      | List all events (supports filtering) |
| POST   | `/api/events/`      | Create a new event (auth required)   |
| GET    | `/api/events/{id}/` | Retrieve event details               |
| PUT    | `/api/events/{id}/` | Update event (organizer only)        |
| PATCH  | `/api/events/{id}/` | Partially update event (organizer)   |
| DELETE | `/api/events/{id}/` | Delete event (organizer only)        |

#### 📝 Event Registration

| Method | Endpoint                     | Description                           |
| ------ | ---------------------------- | ------------------------------------- |
| POST   | `/api/events/{id}/register/` | Register for an event (auth required) |

---

### 🔍 Filtering

When listing events, you can filter by `date`, `location`, and `title`.

Examples:

```http
GET /api/events/?location=Kyiv
GET /api/events/?date=2025-07-20
GET /api/events/?title=Conference
```
---
## 🛠 Tech Stack

* **Backend**: Django 5.x, Django REST Framework
* **Auth**: JWT (`djangorestframework-simplejwt`)
* **Docs**: Swagger UI (`drf-yasg`)
* **Database**: PostgreSQL
* **Email**: SMTP (Gmail)

---

## 🧹 Useful Commands

### Run migrations manually (inside container):

```bash
docker-compose exec web python manage.py migrate
```

### Create a new superuser:

```bash
docker-compose exec web python manage.py createsuperuser
```

---

## 👥 License

MIT License


