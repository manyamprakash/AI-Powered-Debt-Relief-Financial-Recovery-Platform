from flask import Blueprint, jsonify
from models import FinancialProfile

financial_profile_bp = Blueprint(
    "financial_profile",
    __name__
)


@financial_profile_bp.route("/financial_profiles", methods=["GET"])
def get_financial_profiles():

    profiles = FinancialProfile.query.all()

    data = []

    for profile in profiles:
        data.append({
            "profile_id": profile.profile_id,
            "user_id": profile.user_id,
            "monthly_income": profile.monthly_income,
            "monthly_expenses": profile.monthly_expenses,
            "existing_debts": profile.existing_debts,
            "financial_health_score": profile.financial_health_score
        })

    return jsonify(data)