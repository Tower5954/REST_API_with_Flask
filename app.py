from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'My store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]


# POST - Used to receive data
# Get - Used to send data back only


# POST /store data: {name}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route('/store/<string:name>')     # 'http://127.0.0.1:5000/store/some_name'
def get_store(name):
    # iterate over stores
    # if the store name matches, return it
    # if none match, return it
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
        return jsonify({"[MSG]": "Store not found"})


# GET /store
@app.route('/store')
def get_stores():
    return jsonify({"stores": stores})


# POST /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store():
    pass


app.run(port=5000)
