from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST'])
def check_number():
    if request.json and "123" in request.json['unique_code']:
        return("Correct!") 
    return jsonify(request.json)
    # return("fail")

if __name__ == '__main__':
    app.run(debug=True)