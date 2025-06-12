from flask import jsonify

# Import each controller you make
from controllers.gold_controller import gold_bp
from controllers.real_estate_controller import real_estate_bp
from controllers.stock_controller import stock_bp

def register_routes(app):
    @app.route("/ping")
    def ping():
        return jsonify({"message": "pong"})

    # Register blueprints
    app.register_blueprint(gold_bp, url_prefix="/predict")
    app.register_blueprint(real_estate_bp, url_prefix="/predict")
    app.register_blueprint(stock_bp, url_prefix="/predict")
