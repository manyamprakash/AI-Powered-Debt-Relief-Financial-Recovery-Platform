from flask import Blueprint, request, jsonify
from services.debt_ai import calculate_debt_recommendation

ai_bp = Blueprint("ai", __name__)

@ai_bp.route("/ai/recommendation", methods=["POST"])
def recommendation():

    data = request.get_json()

    result = calculate_debt_recommendation(
        data["income"],
        data["expenses"],
        data["debt"],
        data["loan_amount"]
    )

    return jsonify(result)