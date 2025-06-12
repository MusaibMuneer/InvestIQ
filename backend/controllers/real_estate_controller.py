from flask import Blueprint, request, jsonify
from models.real_estate_model import real_estate_model
from datetime import datetime
import numpy as np

real_estate_bp = Blueprint("real_estate", __name__)

@real_estate_bp.route("/real-estate", methods=["POST"])
def predict_real_estate():
    data = request.get_json()
    date_str = data.get("date")

    try:
        date_obj = datetime.strptime(date_str, "%Y-%m")
        input_features = np.array([[date_obj.year, date_obj.month]])
    except Exception:
        return jsonify({"error": "Invalid date format, use YYYY-MM"}), 400

    prediction = float(real_estate_model.predict(input_features))
    return jsonify({
        "predicted_real_estate_etf_price": round(prediction, 2),
        "predicted_for": date_str
    })
