# XDriver API

XDriver is a Django REST-style backend API for a carpooling application where:

- Drivers can publish rides
- Passengers can search and book rides
- Users can authenticate using signup/signin
- Drivers can manage rides
- Passengers can view booking history

---

# Features

## Authentication
- User registration
- User login
- User logout

## Driver Features
- Publish rides
- Edit rides
- Delete rides
- View ride history

## Passenger Features
- Search for rides
- Book rides
- View booking history

---

# Technologies Used

- Python
- Django
- SQLite
- JSON API

---

# Project Structure

```bash
XDriver/
│
├── Authentication/
├── Ride/
├── Booking/
├── manage.py
```

---

# Installation

## Clone the repository

```bash
git clone <your-repo-url>
cd XDriver
```

## Create virtual environment

```bash
python -m venv venv
```

## Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## Install dependencies

```bash
pip install django
```

---

# Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# Run Server

```bash
python manage.py runserver
```

Server URL:

```bash
http://127.0.0.1:8000/
```

---

# Authentication Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Test API |
| POST | `/signup/` | Register user |
| POST | `/signin/` | Login |
| POST | `/signout/` | Logout |

---

# Ride Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/publish_Ride/` | Publish ride |
| GET | `/ride-history/<id>/` | Driver ride history |
| GET | `/search/<departure>/<arrival>/<date>/` | Search rides |
| DELETE | `/delete_ride/` | Delete ride |
| PUT | `/edit_ride/` | Edit ride |

---

# Booking Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/book_ride/` | Book ride |
| GET | `/ride_history/<id>` | Passenger booking history |

---

# Models

## Passenger

```python
Passenger
- first_name
- last_name
- email
- password
- phone_number
- avg_rating
- number_of_rides
```

## Driver

```python
Driver
- first_name
- last_name
- email
- password
- phone_number
- avg_rating
- vehicle_info
- number_of_rides
```

## Ride

```python
Ride
- driver
- departure_location
- arrival_location
- departure_date_time
- available_seats
- distance
```

## Booking

```python
Booking
- ride
- passenger
- booking_date_time
```

---

# Future Improvements

- JWT Authentication
- Payment Integration
- Real-time notifications
- Ride price prediction using Machine Learning
- Rating system
- Chat system
- GPS tracking

---

# Author

Othmane Belkarda