# API Examples - XDriver

---

# 1. Test API

## Request

```http
GET /
```

## Response

```json
{
  "message": "Hello! Welcome to XDriver API",
  "status": "Server is running"
}
```

---

# 2. Sign Up

## Request

```http
POST /signup/
```

## Body

```json
{
  "first_name": "Othmane",
  "last_name": "Belkarda",
  "email": "othy@gmail.com",
  "password": "123456",
  "password_confirm": "123456",
  "phone_number": "0612345678",
  "user_type": "driver",
  "vehicle_info": "Dacia Logan 2020"
}
```

## Response

```json
{
  "success": "Driver registered successfully",
  "user_id": 1,
  "user_type": "driver"
}
```

---

# 3. Sign In

## Request

```http
POST /signin/
```

## Body

```json
{
  "email": "othy@gmail.com",
  "password": "123456"
}
```

## Response

```json
{
  "success": "Login successful",
  "user_id": 1,
  "user_type": "driver",
  "first_name": "Othmane",
  "last_name": "Belkarda",
  "email": "othy@gmail.com"
}
```

---

# 4. Publish Ride

## Request

```http
POST /publish_Ride/
```

## Body

```json
{
  "driver_id": 1,
  "departure_location": "Casablanca",
  "arrival_location": "Rabat",
  "departure_date_time": "2026-05-15T10:00:00Z",
  "available_seats": 4,
  "distance": 95
}
```

## Response

```json
{
  "status": "success",
  "ride_id": 1
}
```

---

# 5. Search Ride

## Request

```http
GET /search/Casablanca/Rabat/15-05-2026/
```

## Response

```json
{
  "status": "success",
  "count": 1,
  "data": [
    {
      "id": 1,
      "departure_location": "Casablanca",
      "arrival_location": "Rabat",
      "departure_date_time": "2026-05-15T10:00:00Z",
      "available_seats": 4,
      "distance": "95.00"
    }
  ]
}
```

---

# 6. Book Ride

## Request

```http
POST /book_ride/
```

## Body

```json
{
  "passenger_id": 1,
  "ride_id": 1
}
```

## Response

```json
{
  "message": "Ride booked successfully"
}
```

---

# 7. Passenger Ride History

## Request

```http
GET /ride_history/1
```

## Response

```json
{
  "history": [
    {
      "ride_id": 1,
      "departure": "Casablanca",
      "arrival": "Rabat",
      "driver_First_Name": "Othmane",
      "driver_Last_Name": "Belkarda"
    }
  ]
}
```

---

# 8. Driver Ride History

## Request

```http
GET /ride-history/1/
```

## Response

```json
{
  "status": "success",
  "data": [
    {
      "id": 1,
      "departure_location": "Casablanca",
      "arrival_location": "Rabat",
      "departure_date_time": "2026-05-15T10:00:00Z",
      "available_seats": 4,
      "distance": "95.00"
    }
  ]
}
```

---

# 9. Edit Ride

## Request

```http
PUT /edit_ride/
```

## Body

```json
{
  "ride_id": 1,
  "driver_id": 1,
  "available_seats": 3
}
```

## Response

```json
{
  "status": "success",
  "message": "Ride updated successfully"
}
```

---

# 10. Delete Ride

## Request

```http
DELETE /delete_ride/
```

## Body

```json
{
  "ride_id": 1,
  "driver_id": 1
}
```

## Response

```json
{
  "status": "success",
  "message": "Ride deleted successfully"
}
```