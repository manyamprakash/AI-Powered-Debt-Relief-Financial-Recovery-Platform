from flask import Blueprint, request, jsonify
from database import db
from models import Loan

loan_bp = Blueprint("loans", __name__)

# CREATE LOAN
@loan_bp.route("/loans", methods=["POST"])
def create_loan():
    data = request.json

    loan = Loan(
        user_id=data["user_id"],
        loan_type=data["loan_type"],
        loan_amount=data["loan_amount"],
        interest_rate=data["interest_rate"],
        tenure=data["tenure"],
        remaining_balance=data["remaining_balance"],
        status=data.get("status", "Active")
    )

    db.session.add(loan)
    db.session.commit()

    return jsonify({
        "message": "Loan created successfully",
        "loan_id": loan.loan_id
    }), 201


# GET ALL LOANS
@loan_bp.route("/loans", methods=["GET"])
def get_loans():
    loans = Loan.query.all()

    return jsonify([
        {
            "loan_id": loan.loan_id,
            "user_id": loan.user_id,
            "loan_type": loan.loan_type,
            "loan_amount": loan.loan_amount,
            "interest_rate": loan.interest_rate,
            "tenure": loan.tenure,
            "remaining_balance": loan.remaining_balance,
            "status": loan.status
        }
        for loan in loans
    ])


# GET ONE LOAN
@loan_bp.route("/loans/<int:id>", methods=["GET"])
def get_loan(id):
    loan = Loan.query.get(id)

    if not loan:
        return jsonify({"message": "Loan not found"}), 404

    return jsonify({
        "loan_id": loan.loan_id,
        "user_id": loan.user_id,
        "loan_type": loan.loan_type,
        "loan_amount": loan.loan_amount,
        "interest_rate": loan.interest_rate,
        "tenure": loan.tenure,
        "remaining_balance": loan.remaining_balance,
        "status": loan.status
    })


# UPDATE LOAN
@loan_bp.route("/loans/<int:id>", methods=["PUT"])
def update_loan(id):
    loan = Loan.query.get(id)

    if not loan:
        return jsonify({"message": "Loan not found"}), 404

    data = request.json

    loan.loan_type = data.get("loan_type", loan.loan_type)
    loan.loan_amount = data.get("loan_amount", loan.loan_amount)
    loan.interest_rate = data.get("interest_rate", loan.interest_rate)
    loan.tenure = data.get("tenure", loan.tenure)
    loan.remaining_balance = data.get("remaining_balance", loan.remaining_balance)
    loan.status = data.get("status", loan.status)

    db.session.commit()

    return jsonify({"message": "Loan updated successfully"})


# DELETE LOAN
@loan_bp.route("/loans/<int:id>", methods=["DELETE"])
def delete_loan(id):
    loan = Loan.query.get(id)

    if not loan:
        return jsonify({"message": "Loan not found"}), 404

    db.session.delete(loan)
    db.session.commit()

    return jsonify({"message": "Loan deleted successfully"})