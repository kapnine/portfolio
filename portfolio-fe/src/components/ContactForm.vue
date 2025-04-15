<script setup>
import { ref } from 'vue'
import axios from 'axios'

// Define reactive state
const form = ref({
  name: '',
  email: '',
  message: ''
})

const responseMessage = ref('')

// Define the submit function
const submitForm = async () => {
  try {
    const response = await axios.post('http://localhost:8000/contact/', form.value)
    responseMessage.value = response.data.message
  } catch (error) {
    responseMessage.value = 'There was an error sending your message.'
    console.error('Error:', error)
  }
}
</script>

<template>
  <v-app>
    <v-container>
      <h1>Contact Me</h1>
      <p>Feel free to reach out to me!</p>
      <v-form @submit.prevent="submitForm">
        <v-text-field
          type="text"
          v-model="form.name"
          placeholder="Your Name"
          required
        />
        <v-text-field
          type="email"
          v-model="form.email"
          placeholder="Your Email"
          required
        />
        <v-textarea
          v-model="form.message"
          placeholder="Your Message"
          required
        ></v-textarea>
        <v-btn type="submit">Send</v-btn>
        <p v-if="responseMessage">{{ responseMessage }}</p>
      </v-form>
    </v-container>
  </v-app>
</template>
