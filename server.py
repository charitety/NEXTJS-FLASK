from flask import Flask, jsonify
from flask_cors import CORS

# app instance
app = Flask(__name__)
CORS(app)

@app.route("/api/home", methods=['GET'])
def return_home():
    return jsonify({
        'message': "This is great!",
        'people': ['Maria','Pablo','Roberto']

    })

if __name__ == "__main__":
    app.run(debug=True, port=8080)

#to activate virtual environment: venv\Scripts\activate.bat
#to run server run the following command from directory where server is: 
#python server.js 
