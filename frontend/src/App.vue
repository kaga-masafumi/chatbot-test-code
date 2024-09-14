<template>
  <div id="app">
    <h1>Chat with GPT</h1>
    <div class="chat-window">
      <div class="messages">
        <ChatMessage
          v-for="(msg, index) in messages"
          :key="index"
          :text="msg.text"
          :isUser="msg.isUser"
        />
      </div>
      <ChatInput @send="handleSend" />
    </div>
  </div>
</template>

<script>
import ChatInput from './components/ChatInput.vue';
import ChatMessage from './components/ChatMessage.vue';
import axios from 'axios';

export default {
  components: {
    ChatInput,
    ChatMessage,
  },
  data() {
    return {
      messages: [],
    };
  },
  methods: {
    async handleSend(message) {
      this.messages.push({ text: message, isUser: true });
      
      try {
        const res = await axios.post('http://localhost:5000/chat', { message });
        this.messages.push({ text: res.data.response, isUser: false });
      } catch (error) {
        console.error(error);
        // エラー処理を追加することをお勧めします
      }
    },
  },
};
</script>

<style>
#app {
  max-width: 1200px; /* 任意の横幅を設定 */
  margin: 20px auto;
  text-align: left;
}

.chat-window {
  border: 1px solid #ccc;
  border-radius: 10px;
  padding: 10px;
  height: 500px; /* 高さを設定 */
  display: flex;
  flex-direction: column;
  overflow-y: auto;
}

.messages {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}
</style>
