
from flask import Flask
from config import Config
from database import db

print("Starting FinRelief AI...")
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

from models import *
from routes.user_routes import user_bp
from routes.loan_routes import loan_bp
from routes.financial_profiles import financial_profile_bp
from routes.settlement_records import settlement_bp
from routes.ai_routes import ai_bp
app.register_blueprint(user_bp)
app.register_blueprint(loan_bp)
app.register_blueprint(financial_profile_bp)
app.register_blueprint(settlement_bp)
app.register_blueprint(ai_bp)
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return {"message": "FinRelief AI Backend Running Successfully"}

if __name__ == "__main__":
    app.run(debug=True)