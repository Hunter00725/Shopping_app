
from flask import Flask, jsonify, request

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 999},
    {"id": 2, "name": "Smartphone", "price": 499},
    {"id": 3, "name": "Headphones", "price": 149}
]

cart = []

@app.route('/')
def home():
    return """
    <h1>Welcome to the Shopping App (v2)</h1>
    <p>View products at /products</p>
    <p>View cart at /cart</p>
    <p>Use POST /cart to add a product.</p>
    """

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({"products": PRODUCTS})

@app.route('/cart', methods=['GET'])
def get_cart():
    return jsonify({"cart": cart})

@app.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.get_json(silent=True) or {}
    product_id = data.get('product_id')

    if not isinstance(product_id, int):
        return jsonify({"error": "Valid product_id required"}), 400

    product = next(
        (p for p in PRODUCTS if p['id'] == product_id), None
    )

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    cart.append(product)
    return jsonify({
        "message": f"{product['name']} added to cart",
        "cart": cart
    }), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
