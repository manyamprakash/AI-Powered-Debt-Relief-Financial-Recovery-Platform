# AI-Powered Debt Relief & Financial Recovery Platform

## Project Description

The AI-Powered Debt Relief & Financial Recovery Platform is a Flask-based web application that helps users manage their loans and financial information. The system stores data in PostgreSQL and provides AI-based debt recommendations.

---

## Features

- User Management
- Loan Management
- Financial Profile Management
- Settlement Records Management
- AI-Based Debt Recommendation
- REST API using Flask
- PostgreSQL Database Integration

---

## Technologies Used

- Python
- Flask
- PostgreSQL
- SQLAlchemy
- Postman
- VS Code

---

## Project Structure

backend/
│
├── app.py
├── config.py
├── database.py
├── models.py
├── requirements.txt
├── README.md
│
├── routes/
│   ├── user_routes.py
│   ├── loan_routes.py
│   ├── financial_profiles.py
│   ├── settlement_records.py
│   └── ai_routes.py
│
├── services/
│   └── debt_ai.py

---

## Database Tables

- users
- loans
- financial_profiles
- settlement_records

---

## API Endpoints

### GET /users

Returns all users.

### GET /loans

Returns all loans.

### GET /financial_profiles

Returns financial profile information.

### GET /settlement_records

Returns settlement records.

### POST /ai/recommendation

Returns an AI-based debt recommendation.

Sample Request

```json
{
  "income": 50000,
  "expenses": 30000,
  "debt": 50000,
  "loan_amount": 50000
}
```

Sample Response

```json
{
  "risk_level": "LOW",
  "recommendation": "Continue regular EMI payments",
  "recommended_amount": 50000
}
```

---

## How to Run the Project

1. Install Python
2. Install PostgreSQL
3. Install dependencies

```
pip install -r requirements.txt
```

4. Configure the `.env` file with your PostgreSQL details.

5. Run the application

```
python app.py
```

6. Open

```
http://127.0.0.1:5000
```

---

## Future Scope

- User Authentication
- Credit Score Prediction
- Machine Learning Models
- Email Notifications
- Dashboard

---

## Author

Manyam Prakash

---

## License

This project is developed for academic purposes only.