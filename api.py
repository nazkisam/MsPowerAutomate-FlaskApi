from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get-daily-report', methods=['GET'])
def get_report():
    return jsonify({
        "campaign": "Meta Summer Ads",
        "clicks": 2432,
        "impressions": 92144,
        "spend": 387.21
    },
    )

if __name__ == '__main__':
    app.run(debug=True)
