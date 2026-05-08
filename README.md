# Best Cars Dealership – Full Stack Capstone Project

## Project Overview
A full-stack web application for Best Cars Dealership, a national car retailer in the U.S.
Built as the IBM Full Stack Software Developer Professional Certificate Capstone Project.

## Technologies Used
- **Frontend:** React.js, HTML5, CSS3, Bootstrap
- **Backend:** Django (Python), Node.js, Express.js
- **Database:** SQLite (Django), MongoDB (dealers/reviews)
- **Microservices:** Flask + VADER (Sentiment Analysis)
- **Deployment:** Docker, Kubernetes, IBM Cloud Code Engine
- **CI/CD:** GitHub Actions

## Features
- Browse car dealerships nationwide
- Filter dealerships by state
- View and submit dealer reviews
- Sentiment analysis on reviews (positive/neutral/negative)
- User registration, login, and logout
- Admin panel for managing car makes and models

## Architecture
- Django serves the main web application
- Node.js/Express + MongoDB handles dealers and reviews data
- Flask microservice analyzes review sentiment using VADER
- React frontend for dynamic user interactions

## Setup
```bash
git clone https://github.com/akashshawdev/xrwvm-fullstack_developer_capstone.git
cd xrwvm-fullstack_developer_capstone/server
pip install -r requirements.txt
python manage.py runserver
```

## Author
Akash Shaw
