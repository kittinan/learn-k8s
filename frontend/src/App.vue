<script setup>
import { ref } from "vue";
import axios from "axios";

const response = ref(null);
const loading = ref(false);
const error = ref(null);

const fetchInfo = async () => {
  loading.value = true;
  error.value = null;
  try {
    const apiUrl = `${import.meta.env.VITE_BACKEND_URL}/info`;
    const res = await axios.get(apiUrl);
    response.value = res.data;
  } catch (err) {
    console.error("Error fetching data:", err);
    error.value = err.message || "Failed to fetch data";
  } finally {
    loading.value = false;
  }
};
</script>

<template>
  <div class="container">
    <div class="card">
      <h1>Kubernetes Demo App</h1>

      <button class="fetch-button" @click="fetchInfo" :disabled="loading">
        {{ loading ? "Loading..." : "Get Server Info" }}
      </button>

      <!-- Show error if any -->
      <div class="error" v-if="error">
        <p>{{ error }}</p>
      </div>

      <!-- Display JSON response -->
      <div class="response-container" v-if="response && !error">
        <h3>Server Response:</h3>
        <pre class="json-response">{{ JSON.stringify(response, null, 2) }}</pre>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
  background-color: #f5f5f5;
}

.card {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  padding: 2rem;
  width: 80%;
  max-width: 600px;
  text-align: center;
}

h1 {
  color: #2c3e50;
  margin-bottom: 2rem;
}

.fetch-button {
  background-color: #42b883;
  color: white;
  border: none;
  padding: 12px 24px;
  font-size: 16px;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
  margin-bottom: 1.5rem;
}

.fetch-button:hover {
  background-color: #3aa876;
}

.fetch-button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.error {
  background-color: #ffecec;
  color: #e74c3c;
  padding: 1rem;
  border-radius: 4px;
  margin: 1rem 0;
}

.response-container {
  text-align: left;
  background-color: #f8f8f8;
  border-radius: 4px;
  padding: 1rem;
  margin-top: 1rem;
  max-height: 60vh;
  overflow-y: auto;
}

.json-response {
  white-space: pre-wrap;
  overflow-x: auto;
  background-color: #2c3e50;
  color: #ecf0f1;
  padding: 1.5rem;
  border-radius: 4px;
  font-family: "Courier New", monospace;
  line-height: 1.5;
  max-height: none;
}
</style>
