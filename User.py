from flask import Flask, request, jsonify

app = Flask(__name__) 

#User
@app.route("/sensor_data", methods=["GET","POST"])
def receive_sensor_data():
    data = request.get_json()
    print("\n[<---]Reciving Data: ",type(data),"\n")
    print("\n[Live Data] :",data)
    if not data:
        return jsonify({"error": "Invalid data format"}), 415  # Handle unsupported media type
    return jsonify({"status": "success", "received_data": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6001, debug=True)
