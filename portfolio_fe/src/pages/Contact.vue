<script setup>
  import { ref } from 'vue'
  import axios from 'axios'

  axios.defaults.xsrfCookieName = 'csrftoken';
  axios.defaults.xsrfHeaderName = 'X-CSRFToken';
  axios.defaults.withCredentials = true; // This is crucial!

  const form = ref({
    name: '',
    email: '',
    message: '',
  })

  const responseMessage = ref('')
  const errors = ref({})

  const apiClient = axios.create({
    baseURL: '/api',
    timeout: 10000,
    headers: {
      'Content-Type': 'application/json',
    },
    withCredentials: true,
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFToken',
  });


  const getCSRF = async () => {
    await apiClient.get('/csrf/')
  }

  const validateForm = () => {
    errors.value = {}

    // Validate name
    if (!form.value.name.trim()) {
      errors.value.name = 'Name is required.'
    } else if (form.value.name.length > 100) {
      errors.value.name = 'Name must be less than 100 characters.'
    }

    // Validate email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    if (!form.value.email.trim()) {
      errors.value.email = 'Email is required.'
    } else if (!emailRegex.test(form.value.email)) {
      errors.value.email = 'Invalid email format.'
    }

    // Validate message
    if (!form.value.message.trim()) {
      errors.value.message = 'Message is required.'
    } else if (form.value.message.length > 500) {
      errors.value.message = 'Message must be less than 500 characters.'
    }

    return Object.keys(errors.value).length === 0
  }

  const submitForm = async () => {
    if (!validateForm()) {
      responseMessage.value = 'Please fix the errors before submitting.'
      return
    }

    try {
      await getCSRF()
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
        :error-messages="errors.name"
        placeholder="Your Name"
        required
        type="text"
      />
      <v-text-field
        v-model="form.email"
        :error-messages="errors.email"
        placeholder="Your Email"
        required
        type="email"
      />
      <v-textarea
        v-model="form.message"
        :error-messages="errors.message"
        placeholder="Your Message"
        required
      />
      <v-btn type="submit">Send</v-btn>
      <p v-if="responseMessage">{{ responseMessage }}</p>
    </v-form>
  </v-container>
</template>
