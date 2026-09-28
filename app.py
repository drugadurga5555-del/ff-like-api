from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

MAIN_JWT = "eyJhbGciOiJIUzI1NiIsInN2ciI6IjMiLCJ0eXAiOiJKV1QifQ.eyJhY2NvdW50X2lkIjo3Nzk5MTAzNTMyLCJuaWNrbmFtZSI6ImZEZDNiV3R3VnkxVUR3PT0iLCJub3RpX3JlZ2lvbiI6IklORCIsImxvY2tfcmVnaW9uIjoiSU5EIiwiZXh0ZXJuYWxfaWQiOiJjOWQ3YjkzMGY3N2M5NTc0NTA2NTlkZDQ0ZmU2OTRkZiIsImV4dGVybmFsX3R5cGUiOjgsInBsYXRfaWQiOjEsImNsaWVudF92ZXJzaW9uIjoiMi4xMzIuNCIsImNsaWVudF92ZXJzaW9uX2NvZGUiOiIyMDE5MTE4NTI1IiwiZW11bGF0b3Jfc2NvcmUiOjEwMCwiaXNfZW11bGF0b3IiOnRydWUsImNvdW50cnlfY29kZSI6IlNFIiwiZXh0ZXJuYWxfdWlkIjoxODM1MDAwODgxMDQwLCJyZWdfYXZhdGFyIjoxMDIwMDAwMDUsInNvdXJjZSI6MCwibG9ja19yZWdpb25fdGltZSI6MTY4NTIwOTMyOSwiY2xpZW50X3R5cGUiOjIsInNpZ25hdHVyZV9tZDUiOiIxYWM0YjgwZWNmMDQ3OGE0NDIwM2JmOGZhYzYxMjBmNSIsInVzaW5nX3ZlcnNpb24iOjIsInJlbGVhc2VfY2hhbm5lbCI6ImFuZHJvaWRfbWF4IiwicmVsZWFzZV92ZXJzaW9uIjoiT0I1NSIsImV4cCI6MTc5MDU4NjY5Nn0.mYPfWI9j019NOnMdQBKA9gkZ9RboZXxkkfnhGDa6CWM"
MAIN_OPEN_ID = "c9d7b930f77c957450659dd44fe694df"

@app.route('/like')
def like():
    uid = request.args.get('uid')
    if not uid:
        return jsonify({"error": "uid dalo -> /like?uid=123456"})

    # Like bhej raha hai
    return jsonify({
        "status": "Ready",
        "your_bot_open_id": MAIN_OPEN_ID,
        "target_uid": uid,
        "message": "Ab ye JWT aur Open ID se like jayega. Protobuf wala part add karna baki hai toh bol."
    })

@app.route('/')
def home():
    return "API READY HAI - /like?uid=YOUR_ID use kar"

app.run(host='0.0.0.0', port=10000)Enter
