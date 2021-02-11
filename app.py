from flask import Flask, request, jsonify
from utils.scraping import Webscraping

app = Flask(__name__)

@app.route('/stock/<symbol>', methods=['GET'])
def api_get_stock(symbol):
  if symbol:
    webscraping = Webscraping()
    stock = webscraping.get_stock(symbol)
    return jsonify(stock)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)