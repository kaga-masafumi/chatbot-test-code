import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

app = Flask(__name__)
CORS(app)

load_dotenv()  # .envファイルを読み込む

# OpenAIのAPIキーを設定
openai_api_key = os.getenv('OPENAI_API_KEY')  

# ChatOpenAIのインスタンスを作成
model = ChatOpenAI(model="gpt-4o-mini", openai_api_key=openai_api_key)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message')

    # LangChainを使ってメッセージを送信
    response = model([HumanMessage(content=message)])

    # レスポンス内容を抽出して返す
    return jsonify({'response': response.content})

if __name__ == '__main__':
    app.run(debug=True)