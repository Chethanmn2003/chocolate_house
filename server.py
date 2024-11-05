from flask import Flask, jsonify, request, render_template
from app.main import add_seasonal_flavor, add_ingredient, add_customer_feedback

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Endpoint to add new flavor
@app.route('/seasonal_flavor', methods=['GET','POST'])
def create_seasonal_flavor():
    data = request.json
    if 'name' not in data or 'price' not in data:
        return jsonify({"error": "Missing name or price"}), 400

    flavor = add_seasonal_flavor(data['name'], data['price'])
    if flavor is None:
        return jsonify({"error": "Failed to add seasonal flavor"}), 500

    return jsonify({"id": flavor.id, "name": flavor.name, "price": flavor.price}), 201

# Endpoint to add ingredient
@app.route('/ingredient', methods=['GET','POST'])
def create_ingredient():
    data = request.json
    if 'name' not in data or 'quantity' not in data:
        return jsonify({"error": "Missing name or quantity"}), 400

    ingredient = add_ingredient(data['name'], data['quantity'])
    if ingredient is None:
        return jsonify({"error": "Failed to add ingredient"}), 500

    return jsonify({"id": ingredient.id, "name": ingredient.name, "quantity": ingredient.quantity}), 201

# Endpoint to add feedback
@app.route('/feedback', methods=['GET','POST'])
def create_feedback():
    data = request.json
    if 'customer_name' not in data or 'feedback_text' not in data or 'rating' not in data:
        return jsonify({"error": "Missing customer_name, feedback_text or rating"}), 400

    feedback = add_customer_feedback(data['customer_name'], data['feedback_text'], data['rating'])
    if feedback is None:
        return jsonify({"error": "Failed to add feedback"}), 500

    return jsonify({"id": feedback.id, "customer_name": feedback.customer_name, "feedback_text": feedback.feedback_text, "rating": feedback.rating}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
