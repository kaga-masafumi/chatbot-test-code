#  Chatbot Code Created for Learning Purposes

This project is a simple chat application powered by OpenAI's GPT API. Users can input messages and receive real-time responses from the AI.

## Structure

- **Frontend**: Built with Vue.js
- **Backend**: Built with Flask

## Requirements

- Python 3.x
- Node.js
- npm (Node Package Manager)
- OpenAI API key

## Installation Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kaga-masafumi/practice-chatbot.git
   cd practice-chatbot
   ```

2. **Install the necessary packages for the backend**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Install the necessary packages for the frontend**:
   ```bash
   cd ../frontend
   npm install
   ```

4. **Set your OpenAI API key**:
   Modify the following line in `backend/app.py` with your actual API key:
   ```python
   openai.api_key = 'your_openai_api_key'
   ```

## Running the Application

### Start the Backend

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Start the Flask application:
   ```bash
   python app.py
   ```

### Start the Frontend

1. Navigate to the frontend directory:
   ```bash
   cd ../frontend
   ```

2. Start the Vue.js application:
   ```bash
   npm run serve
   ```

3. Open your browser and go to `http://localhost:8080`.

## Usage

Type a message in the chat box and click the "Send" button to receive a response from the AI.

## License

This project is licensed under the [MIT License](LICENSE).
