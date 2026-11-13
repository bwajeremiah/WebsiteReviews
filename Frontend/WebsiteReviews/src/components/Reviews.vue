<script setup>
import { ref } from 'vue'
import StarRatingModule from vue-star-rating 
const rating = ref(0)
const websiteData = ref([])
const errorMessage = ref('')
const newNoteText = ref('')
const selectDelete = ref('')
const editNoteText = ref('')
const editNoteId = ref('')
const StarRating = (StarRatingModule in any).defauly ?? StarRatingModule
async function fetchWebsites() {
  errorMessage.value = ''

  try {
    const response = await fetch('/api/website/')
    if (!response.ok) {
      throw new Error(`Request failed with status ${response.status}`)
    }

    websiteData.value = await response.json()
  } catch (error) {
    errorMessage.value = error instanceof Error ? error.message : 'Unable to fetch notes'
  }
}
async function addWebsite() {
  errorMessage.value = ""
  try {
    const response = await fetch('/api/website', {
      method: 'POST', 
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ url:  websiteUrl.value },{rating: websiteRating.value},{easyNav: easyNav.Value},{adFlood: adFlood.value})
    })
    if (!response.ok) {
      throw new Error(`Request failed with status ${response.status}`)
    }
  } catch (error) {
    errorMessage.value = error instanceof Error ? error.message : 'Unable to add note'
  }
}
async function adAndShow(){
  addWebsite
  await fetchWebsites 
}
</script>

<template>
  <button @click="fetchNotes">See Sites</button>
  <p v-if="errorMessage">{{ errorMessage }}</p>
  <ul v-else-if="notesData.length">
    <li v-for="webiste in websiteData" :key="note.id">
      ({{ website.url }}, Rating{{ website.rating }})
    </li>
  </ul>
  <p v-else>No notes loaded yet.</p>
  <input v-model="newWebsiteText" placeholder="Enter a new website url"></input>
  <star-rating v-model="rating" :max-rating="5" :increment="0.5"></star-rating>   
  <button @click="addAndShow">Add Website</button>
</template>