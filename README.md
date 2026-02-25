# MRC Constructions – Backend Setup Guide

This guide explains how to clone the project and set up the backend environment locally.

---

## 📦 Clone the Repository

Clone the project to your local machine:

```bash
git clone https://github.com/osiota10/-MRC-Constructions.git
```

Navigate into the project directory:

```bash
cd -MRC-Constructions
```

---

## 📁 Create a Backend Project Directory

Inside the current directory, create a new folder named `backend` and navigate into it:

```bash
mkdir backend
cd backend
```

---

## 🐍 Create a Virtual Environment

Create a virtual environment to manage project dependencies:

```bash
python -m venv venv
```

---

## ▶️ Activate the Virtual Environment

### On macOS/Linux:

```bash
source venv/bin/activate
```

### On Windows:

```bash
venv\Scripts\activate
```

---

## 🚀 Install Django

Once the virtual environment is activated, install Django:

```bash
pip install django
```

---

## 🔐 Install and Configure `django-environ`

Install `django-environ` to manage environment variables:

```bash
pip install django-environ
```

You can now configure your environment variables using a `.env` file in your project root.

---

## 📝 Notes

- Always ensure your virtual environment is activated before installing dependencies.
- Add `venv/` and `.env` to your `.gitignore` file to prevent them from being committed to version control.
- Run the following command to generate a dependency file if needed:

```bash
pip freeze > requirements.txt
```

---

Your backend environment is now ready for development. 🚀
