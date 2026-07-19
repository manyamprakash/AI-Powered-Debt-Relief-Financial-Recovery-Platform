from database import db
from datetime import datetime


# -----------------------------
# User Model
# -----------------------------
class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(15))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    loans = db.relationship("Loan", backref="user", lazy=True)
    financial_profile = db.relationship(
        "FinancialProfile",
        backref="user",
        uselist=False,
        lazy=True
    )
    settlements = db.relationship(
        "SettlementRecord",
        backref="user",
        lazy=True
    )
    ai_history = db.relationship(
        "AIHistory",
        backref="user",
        lazy=True
    )

    def __repr__(self):
        return f"<User {self.name}>"

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }


# -----------------------------
# Loan Model
# -----------------------------
class Loan(db.Model):
    __tablename__ = "loans"

    loan_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    loan_type = db.Column(db.String(50))
    loan_amount = db.Column(db.Float, nullable=False)
    interest_rate = db.Column(db.Float)
    tenure = db.Column(db.Integer)
    remaining_balance = db.Column(db.Float)
    status = db.Column(db.String(20), default="Active")


# -----------------------------
# Financial Profile Model
# -----------------------------
class FinancialProfile(db.Model):
    __tablename__ = "financial_profiles"

    profile_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    monthly_income = db.Column(db.Float)

    monthly_expenses = db.Column(db.Float)

    existing_debts = db.Column(db.Float)

    financial_health_score = db.Column(db.Float)

# -----------------------------
# Settlement Record Model
# -----------------------------
class SettlementRecord(db.Model):
    __tablename__ = "settlement_records"

    settlement_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    loan_id = db.Column(db.Integer)

    settlement_prediction = db.Column(db.String(100))
    recommended_amount = db.Column(db.Float)
    priority_level = db.Column(db.String(20))


# -----------------------------
# AI History Model
# -----------------------------
class AIHistory(db.Model):
    __tablename__ = "ai_history"

    history_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    recommendation = db.Column(db.Text)
    risk_level = db.Column(db.String(20))
    predicted_payment = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)