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

## 📥 Install Dependencies from `requirements.txt`

Once the virtual environment is activated, install all required dependencies using:

```bash
pip install -r requirements.txt
```

If `requirements.txt` does not yet exist, you can generate it with:

```bash
pip freeze > requirements.txt
```

---

## 🔐 Configure Environment Variables

Create a `.env` file in your project root to manage environment variables (recommended when using `django-environ`).

Example:

```env
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
```

Make sure to add the following to your `.gitignore` file:

```
venv/
.env
```

---

## 📝 Notes

- Always ensure your virtual environment is activated before installing dependencies.
- Never commit your `.env` file or `venv/` directory to version control.
- After installation, you can verify Django is installed with:

```bash
python -m django --version
```

---

Your backend environment is now ready for development. 🚀
