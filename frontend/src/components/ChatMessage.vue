<template>
  <div class="message" :class="{'user-message': isUser, 'bot-message': !isUser}" v-html="formattedText"></div>
</template>

<script>
import { marked } from 'marked';

export default {
  name: "ChatMessage",
  props: {
    text: {
      type: String,
      required: true,
    },
    isUser: {
      type: Boolean,
      default: false,
    },
  },
  computed: {
    formattedText() {
      return marked(this.text); // MarkdownをHTMLに変換
    },
  },
};
</script>

<style scoped>
.message {
  padding: 10px;
  margin: 5px;
  border-radius: 10px;
  width: fit-content;
  max-width: 60%;
}

.user-message {
  background-color: #d1ffd1; /* 自分のメッセージの色 */
  align-self: flex-end; /* 右寄せ */
}

.bot-message {
  background-color: #f0f0f0; /* ボットのメッセージの色 */
}
</style>