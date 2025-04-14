<script setup>
import axios from 'axios';
</script>

<template>
  <div class="contact">
    <h1>Contact Me</h1>
    <p>If you have any questions, feel free to reach out!</p>
    <form @submit.prevent="submitForm">
      <input type="text" v-model="form.name" placeholder="Your Name" required />
      <input type="email" v-model="form.email" placeholder="Your Email" required />
      <textarea v-model="form.message" placeholder="Your Message" required></textarea>
      <button type="submit">Send</button>
      <p v-if="responseMessage">{{ responseMessage }}</p>
    </form>
  </div>
</template>

<script>
export default {
  name: 'ContactForm',
  data() {
    return {
      form: {
        name: '',
        email: '',
        message: ''
      },
      responseMessage: ''
    };
  },
  methods: {
    async submitForm() {
      try {
        const response = await axios.post('http://localhost:8000/contact/', this.form);
        this.responseMessage = response.data.message;
      } catch (error) {
        this.responseMessage = 'There was an error sending your message.';
        console.error('Error:', error);
      }
    }
  }
};
</script>

<style scoped>
  .contact {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
  }
</style>
