<template>
    <div class="chat-input">
      <textarea v-model="message" placeholder="Type your message..." rows="3"></textarea>
      <button @click="sendMessage">Send</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        message: '',
      };
    },
    methods: {
      sendMessage() {
        if (this.message.trim() === '') return;
        this.$emit('send', this.message);
        this.message = ''; // メッセージをクリア
      },
    },
  };
  </script>
  
  <style scoped>
  .chat-input {
    display: flex;
    flex-direction: column;
    margin-top: 10px;
  }
  
  textarea {
    width: 100%;
    resize: none;
    margin-bottom: 10px;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
  }
  
  button {
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 10px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #218838;
  }
  </style>