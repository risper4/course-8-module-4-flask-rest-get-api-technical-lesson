# app.py

from flask import Flask, jsonify, request

app = Flask(__name__)

# TODO: Define mock data for a list of products
# Example: Each product should have id, name, price, and category

# TODO: Implement a homepage route that returns a JSON welcome message

# TODO: Implement GET /products to return all products or filter by category

# TODO: Implement GET /products/<id> to return a single product by ID

data = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]

@app.route('/')
def index() :
    return jsonify({'message' : 'Welcome to the Product API!', 'resource_endpoint' : '/products'}) ,200

@app.route('/products')
def get_products() :
    category = request.args.get(category)
    if category:
        filtered = [item for item in data if item['category'] == category]
        return jsonify(filtered), 200
    else :
        return jsonify(data), 200
    
@app.route('/product/<int:id>')
def get_product(id):
    product = next([product for product in data if product['id'] == id], None)
    if product:
        return jsonify(product), 200
    else :
        return ({'message' : 'Product not found'}), 404

if __name__ == "__main__":
    app.run(port=5555, debug=True)
