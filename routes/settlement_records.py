from flask import Blueprint, jsonify
from models import SettlementRecord

settlement_bp = Blueprint(
    "settlement",
    __name__
)


@settlement_bp.route("/settlement_records", methods=["GET"])
def get_settlement_records():

    records = SettlementRecord.query.all()

    data = []

    for record in records:
        data.append({
            "settlement_id": record.settlement_id,
            "user_id": record.user_id,
            "loan_id": record.loan_id,
            "settlement_prediction": record.settlement_prediction,
            "recommended_amount": record.recommended_amount,
            "priority_level": record.priority_level
        })

    return jsonify(data)