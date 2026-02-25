# MRC Constructions – Backend Setup Guide

This guide explains how to clone the project and set up the backend environment locally.

1. Clone the Repository

Clone the project to your local machine:

git clone https://github.com/osiota10/-MRC-Constructions.git

Navigate into the project directory:

cd -MRC-Constructions

2. Create a Backend Project Directory

Inside the current directory, create a new folder named backend:

mkdir backend
cd backend

3. Create a Virtual Environment

Create a virtual environment to manage project dependencies:

python -m venv venv

4. Activate the Virtual Environment
   On macOS/Linux:
   source venv/bin/activate
   On Windows:
   venv\Scripts\activate

5. Install Django

Once the virtual environment is activated, install Django:

pip install django

6. Install and Configure django-environ

Install django-environ to manage environment variables:

pip install django-environ

You can now configure your environment variables using a .env file in your project root.

Notes

Always ensure your virtual environment is activated before installing dependencies.

Add venv/ and .env to your .gitignore file to prevent them from being committed to version control.

Run pip freeze > requirements.txt to generate a dependency file if needed.

Your backend environment is now ready for development. 🚀
