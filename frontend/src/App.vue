<template>
  <div id="app">
    <h1>Hello from Vue 3 + FastAPI 🎉</h1>
    <button @click="loadApi">Call Backend API</button>
    <p v-if="message">Response: {{ message }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const message = ref('')

async function loadApi() {
  try {
    const res = await fetch('/api/hello')
    const data = await res.json()
    message.value = data.msg
  } catch (err) {
    message.value = 'API request failed'
  }
}
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  padding: 2rem;
  text-align: center;
}
button {
  padding: 0.5rem 1rem;
  margin-top: 1rem;
  cursor: pointer;
}
</style>
