from flask import Flask, render_template, request, url_for, redirect
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import requests
import jsonify

app = Flask(__name__)
api = Api(app)


@app.route("/processjson", methods=["POST"])
def processjson():
    data = request.get_json()
    total_price = 0
    grand_total = 0
    for i in range(len(data)):
        item = data[i]['item']
        category = data[i]['itemCategory']
        quantity = data[i]['quantity']
        price = data[i]['price']
        if str(category).lower() == "medicine" or str(category).lower() == "food":
            total_price = ((0.05 * float(price)) + float(price)) * quantity
        elif str(category).lower() == "imported":
            total_price = ((0.18 * float(price)) + float(price)) * quantity
        elif str(category).lower() == "book":
            total_price = float(total_price) * quantity
        elif str(category).lower() == "music":
            total_price = ((0.03 * float(price)) + float(total_price)) * quantity
        elif str(category).lower() == "clothes":
            if float(price) < 1000:
                total_price = ((0.05 * float(price)) + float(price)) * quantity
            elif float(price) > 1000:
                total_price = ((0.12 * float(price)) + float(price)) * quantity

        grand_total = float(grand_total) + total_price

        print('ITEM = {} , ACTUAL PRICE = {}, QUANTITY = {}, TOTAL PRICE = {}'.format(item, price, quantity, total_price))
        total_price = 0
    print('Grand total before  = {}'.format(grand_total))
    if grand_total > 2000:
        grand_total = grand_total - (0.05 * grand_total)

    print('GRAND_TOTAL = {}'.format(grand_total))
    return "SUCCESS!"


if __name__ == "__main__":
    app.run(debug=True)
