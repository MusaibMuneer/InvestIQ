from flask import Blueprint, request, jsonify
from models.gold_model import gold_model

from datetime import datetime
import numpy as np

gold_bp = Blueprint("gold", __name__)

@gold_bp.route("/gold", methods=["POST"])
def predict_gold():
    data = request.get_json()
    date_str = data.get("date")

    try:
        date_obj = datetime.strptime(date_str, "%Y-%m")
        input_features = np.array([[date_obj.year, date_obj.month]])
    except Exception:
        return jsonify({"error": "Invalid date format, use YYYY-MM"}), 400

    predicted_price = float(gold_model.predict(input_features))
    return jsonify({
        "predicted_gold_price": round(predicted_price, 2),
        "predicted_for": date_str
    })
