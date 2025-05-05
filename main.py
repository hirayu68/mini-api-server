from flask import Flask, request, jsonify

app = Flask(__name__)

# 保存するためのリスト
messages = []

# POSTリクエストでメッセージを受け取る
@app.route("/post", methods=["POST"])
def post_message():
    data = request.get_json()
    message = data.get("message")
    if message:
        messages.append(message)
        print(messages)  # 確認用ログ
        return jsonify({"status": "ok", "message": "受け取りました"})
    else:
        return jsonify({"status": "error", "message": "メッセージがありません"}), 400

if __name__ == "__main__":
    app.run(debug=True)
