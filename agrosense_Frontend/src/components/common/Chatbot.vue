<template>
  <div class="chatbot card">
    <div class="message_container">
      <div v-for="message in messages" :key="message.id" class="message">
        <div class="message-content">{{ message.text }}</div>
      </div>
    </div>

    <div class="input-container">
      <InputText v-model="inputText" @keydown.enter="sendMessage" type="text" placeholder="Type your message..." />
      <Button label="Send" icon="pi pi-send" class="p-button-info p-button-text" @click="sendMessage" />
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      inputText: '',
      messages: []
    };
  },
  methods: {
    sendMessage () {
      if (this.inputText.trim() !== "") {
        this.messages.push({
          id: Date.now(),
          text: this.inputText
        });
        this.inputText = "";
        this.$nextTick(() => {
          this.scrollChatToBottom();
        });
      }
    },
    scrollChatToBottom () {
      const container = this.$el.querySelector(".message_container");
      container.scrollTop = container.scrollHeight;
    }
  },
  mounted () {
    this.scrollChatToBottom();
  }
};
</script>

<style scoped>
.chatbot {
  max-width: 400px;
  margin: 0 auto;
}

.message_container {
  height: 200px;
  overflow-y: auto;
  scroll-behavior: smooth;
  transform: scaleY(-1);
}

.message {
  background-color: #f1f1f1;
  border-radius: 2rem;
  padding: 8px;
  margin-bottom: 8px;
}

.input-container {
  display: flex;
  margin-top: 16px;
}

input[type="text"] {
  flex-grow: 1;
  border: 1px solid #ccc;

  padding: 8px;
}

button {
  margin-left: 8px;
  padding: 8px 16px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>
