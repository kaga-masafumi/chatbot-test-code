import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

load_dotenv()  # .envファイルを読み込む

# OpenAIのAPIキーを設定
openai.api_key = os.getenv('OPENAI_API_KEY')  

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message')

    # OpenAI APIを呼び出す（新しいインターフェース）
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # 使用するモデル
        messages=[{"role": "user", "content": message}]
    )

    # レスポンス内容を抽出して返す
    return jsonify({'response': response['choices'][0]['message']['content']})

if __name__ == '__main__':
    app.run(debug=True)