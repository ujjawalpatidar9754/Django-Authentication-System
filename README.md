# 🔐 Django Full-Stack Authentication & Profile Management System

A robust, job-ready Full-Stack User Authentication and Profile Management Web Application built using Django, SQLite, and Bootstrap 5.

## 🚀 Key Features

* **User Authentication**: Secure Sign-up, Sign-in, and POST-based Logout workflow.
* **Password Recovery**: Integrated built-in Django Password Reset flow with custom token handling.
* **Profile Management**: Custom `Profile` database model extended with a 1-to-1 relationship with Django's built-in `User` model.
* **Automated Signals**: Utilizes Django `post_save` signals to automatically instantiate profile instances upon user creation.
* **Role-Based Access Control (RBAC)**: Integrated Superuser view/admin metrics directly inside the front-end interface.
* **Security Standards**: Strict Cross-Site Request Forgery (CSRF) protection and HTTP method constraint handling.
* **Responsive UI**: Styled using Bootstrap 5 dynamic templates with dynamic flash messages integration.

---

## 🛠️ Tech Stack

* **Backend**: Django (Python 3)
* **Frontend**: HTML5, CSS3, Bootstrap 5
* **Database**: SQLite3
* **Version Control**: Git & GitHub

---

## 💻 Installation & Setup Guide

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/ujjawalpatidar9754/Django-Authentication-System.git](https://github.com/ujjawalpatidar9754/Django-Authentication-System.git)
   cd Django-Authentication-System
