# GPT Chat App

このプロジェクトは、OpenAIのGPTのAPIを使用したシンプルなチャットアプリケーションです。ユーザーはメッセージを入力し、AIからの応答をリアルタイムで受け取ることができます。

## 構成

- **フロントエンド**: Vue.jsを使用
- **バックエンド**: Flaskを使用

## 必要な環境

- Python 3.x
- Node.js
- npm (Node Package Manager)
- OpenAI APIキー

## インストール手順

1. **リポジトリをクローンします**:
   ```bash
   git clone https://github.com/kaga-masafumi/practice-chatbot.git
   cd practice-chatbot
   ```

2. **バックエンドの必要なパッケージをインストール**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **フロントエンドの必要なパッケージをインストール**:
   ```bash
   cd ../frontend
   npm install
   ```

4. **OpenAI APIキーを設定**:
   `backend/app.py` の中で、次の行を自分のAPIキーで修正します：
   ```python
   openai.api_key = 'your_openai_api_key'
   ```

## アプリケーションの起動

### バックエンドの起動

1. バックエンドディレクトリに移動します:
   ```bash
   cd backend
   ```

2. Flaskアプリケーションを起動します:
   ```bash
   python app.py
   ```

### フロントエンドの起動

1. フロントエンドディレクトリに移動します:
   ```bash
   cd ../frontend
   ```

2. Vue.jsアプリケーションを起動します:
   ```bash
   npm run serve
   ```

3. ブラウザで `http://localhost:8080` を開きます。

## 使用方法

チャットボックスにメッセージを入力して "Send" ボタンを押すと、AIからの応答が表示されます。

## ライセンス

このプロジェクトは [MIT License](LICENSE) に基づいています。
