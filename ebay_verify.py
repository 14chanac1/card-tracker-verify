#To get eBay API token
from flask import Flask, request, jsonify
import hashlib
import hmac

app = Flask(__name__)

VERIFICATION_TOKEN = "myCardTrackerToken12345"

@app.route("/ebay-notifications", methods=["GET", "POST"])
def ebay_notifications():
    if request.method == "GET":
        challenge_code = request.args.get("challenge_code", "")
        endpoint_url = "https://your-app-name.onrender.com/ebay-notifications"
        hash_value = hashlib.sha256(
            (challenge_code + VERIFICATION_TOKEN + endpoint_url).encode()
        ).hexdigest()
        return jsonify({"challengeResponse": hash_value})
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)