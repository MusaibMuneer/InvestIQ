from flask import Blueprint, request, jsonify
from models.stock_model import stock_model
from datetime import datetime
import numpy as np

stock_bp = Blueprint("stock", __name__)

@stock_bp.route("/stock", methods=["POST"])
def predict_stock():
    data = request.get_json()
    date_str = data.get("date")

    try:
        date_obj = datetime.strptime(date_str, "%Y-%m")
        input_features = np.array([[date_obj.year, date_obj.month]])
    except Exception:
        return jsonify({"error": "Invalid date format, use YYYY-MM"}), 400

    prediction = float(stock_model.predict(input_features))
    return jsonify({
        "predicted_stock_price": round(prediction, 2),
        "predicted_for": date_str
    })
