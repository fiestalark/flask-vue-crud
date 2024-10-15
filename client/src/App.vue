<!-- App.vue -->
<script setup>
import { ref, watch } from 'vue'
import { RouterView } from 'vue-router'
import { useDark, useToggle } from '@vueuse/core'

const isDark = useDark()
const toggleDark = useToggle(isDark)

watch(isDark, (newValue) => {
  document.documentElement.setAttribute('data-bs-theme', newValue ? 'dark' : 'light')
}, { immediate: true })
</script>

<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Bookshelf</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Books</a>
            </li>
          </ul>
          <button @click="toggleDark()" class="btn btn-outline-secondary">
            <span v-if="isDark">🌙</span>
            <span v-else>☀️</span>
          </button>
        </div>
      </div>
    </nav>
    <div class="container mt-4">
      <RouterView />
    </div>
  </div>
</template>

<style>
/* Custom color variables */
:root {
  --custom-light-bg: #f0f4f8;
  --custom-light-text: #1a202c;
  --custom-light-navbar: #e2e8f0;
  
  --custom-dark-bg: #1a202c;
  --custom-dark-text: #f0f4f8;
  --custom-dark-navbar: #2d3748;
}

/* Light mode styles */
[data-bs-theme="light"] {
  --bs-body-bg: var(--custom-light-bg);
  --bs-body-color: var(--custom-light-text);
  --bs-navbar-bg: var(--custom-light-navbar);
}

/* Dark mode styles */
[data-bs-theme="dark"] {
  --bs-body-bg: var(--custom-dark-bg);
  --bs-body-color: var(--custom-dark-text);
  --bs-navbar-bg: var(--custom-dark-navbar);
}

/* Apply custom navbar background */
.navbar {
  background-color: var(--bs-navbar-bg);
}

/* Ensure proper contrast for navbar items */
[data-bs-theme="light"] .navbar {
  --bs-navbar-color: var(--custom-light-text);
  --bs-navbar-hover-color: rgba(0, 0, 0, 0.7);
}

[data-bs-theme="dark"] .navbar {
  --bs-navbar-color: var(--custom-dark-text);
  --bs-navbar-hover-color: rgba(255, 255, 255, 0.7);
}

/* Style for the toggle button */
.btn-outline-secondary {
  border: none;
  color: var(--bs-body-color);
}

.btn-outline-secondary:hover {
  background-color: rgba(var(--bs-secondary-rgb), 0.1);
}

/* Additional custom styles */
.navbar-nav {
  align-items: center;
}
</style>