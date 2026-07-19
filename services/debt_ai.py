def calculate_debt_recommendation(income, expenses, debt, loan_amount):

    disposable_income = income - expenses

    if disposable_income <= 0:
        return {
            "risk_level": "HIGH",
            "recommendation": "Debt restructuring recommended",
            "recommended_amount": loan_amount * 0.60
        }

    elif debt > income:
        return {
            "risk_level": "MEDIUM",
            "recommendation": "Consider settlement",
            "recommended_amount": loan_amount * 0.70
        }

    else:
        return {
            "risk_level": "LOW",
            "recommendation": "Continue regular EMI payments",
            "recommended_amount": loan_amount
        }