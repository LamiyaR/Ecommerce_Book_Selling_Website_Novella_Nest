# Novella Nest — Ecommerce Book Selling Website

An online bookstore built with **Django 3.2**, featuring product listings, cart & checkout, user accounts, and an admin interface for managing inventory and orders.  

---

## ✨ Features

- **Browse & Search Books** — View listings with details, price, and cover images  
- **Categories/Genres** — Fiction, Non-Fiction, Children, Fantasy, etc.  
- **Cart & Checkout** — Add to cart, update quantities, remove items  
- **User Accounts** — Sign up, log in, manage orders  
- **Admin Dashboard** — Manage books, categories, and orders via Django Admin  
- **Media Support** — Upload and render book cover images  
- **Responsive UI** — Template-based pages for desktop & mobile

---

## 🧱 Tech Stack

- **Backend:** Django 3.2  
- **Database:** SQLite (development) / PostgreSQL (production optional)  
- **Frontend:** Django Templates (HTML/CSS/JS)  
- **Images:** Pillow

### Key Dependencies
```

Django==3.2.3
Pillow==8.2.0
asgiref==3.3.4
pytz==2021.1
sqlparse==0.4.1

```

---

## 📂 Project Structure (important parts)

```

django-book-shop/          # main project folder (internal name can stay; users don’t see it)
├─ manage.py
├─ requirements.txt
├─ db.sqlite3
├─ templates/                 # HTML templates (update headings/labels here)
├─ media/                     # uploaded book cover images
├─ bookshop/               # Django project config (settings, urls, static)
│  ├─ settings.py
│  ├─ urls.py
│  ├─ asgi.py / wsgi.py
│  └─ static/
└─ store/                     # main app (models, views, forms, urls)
├─ models.py
├─ views.py
├─ urls.py
├─ forms.py
└─ admin.py

````
---

## 🚀 Getting Started (Local)

### 1) Setup
```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
````

### 2) Database & Admin

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 3) Run

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


