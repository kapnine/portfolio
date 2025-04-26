<script setup>
  import { ref } from 'vue'
  import axios from 'axios'

  const form = ref({
    name: '',
    email: '',
    message: '',
  })

  const responseMessage = ref('')

  const apiClient = axios.create({
    baseURL: import.meta.env.VITE_API_URL,
    timeout: 10000,
    headers: {
      'Content-Type': 'application/json',
    },
  });

  const submitForm = async () => {
    try {
      const response = await apiClient.post('/contact/', form.value)
      responseMessage.value = response.data.message
    } catch (error) {
      responseMessage.value = 'There was an error sending your message.'
      console.error('Error:', error)
    }
  }
</script>

<template>
  <v-container>
    <h2>Contact Me</h2>
    <p>Feel free to reach out to me!</p>
    <v-form @submit.prevent="submitForm">
      <v-text-field
        v-model="form.name"
        placeholder="Your Name"
        required
        type="text"
      />
      <v-text-field
        v-model="form.email"
        placeholder="Your Email"
        required
        type="email"
      />
      <v-textarea
        v-model="form.message"
        placeholder="Your Message"
        required
      />
      <v-btn type="submit">Send</v-btn>
      <p v-if="responseMessage">{{ responseMessage }}</p>
    </v-form>
  </v-container>
</template>
