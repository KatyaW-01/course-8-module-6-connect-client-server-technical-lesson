from flask import Flask, request, jsonify, send_from_directory
# Import any helper functions you create in store.py

app = Flask(__name__, static_folder='../client', static_url_path='')

# TASK: Define a route for "/"
# This should return index.html from the static folder


# TASK: Define a route for "/api/data"
# This should return a JSON object with a message and status
# Hint: You can use a function from store.py to generate the response
products = [
    {"id": 1, "name": "Notebook", "category": "Stationery"},
    {"id": 2, "name": "Headphones", "category": "Electronics"}
]

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

@app.route("/products", methods=["POST"])
def add_product():
    data = request.get_json()
    new_id = max([p["id"] for p in products], default=0) + 1
    new_product = {"id": new_id, "name": data["name"], "category": data["category"]}
    products.append(new_product)
    return jsonify(new_product), 201

if __name__ == '__main__':
    app.run(debug=True)
