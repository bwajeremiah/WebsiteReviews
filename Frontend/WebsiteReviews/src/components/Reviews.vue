<script setup>
import { ref } from 'vue'
import StarRatingModule from 'vue-star-rating'
const StarRating = StarRatingModule.default ?? StarRatingModule
const websiteData = ref([])
const errorMessage = ref('')
const websiteUrl = ref('')
const websiteRating = ref(0)
const easyNav = ref(false)
const adFlood = ref(false)
const actuallyFree = ref(false)
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
      body: JSON.stringify({ 
        url:  websiteUrl.value ,rating: websiteRating.value,easyNav: easyNav.value,adFlood: adFlood.value,actuallyFree: actuallyFree.value
       })
    })
    if (!response.ok) {
      throw new Error(`Request failed with status ${response.status}`)
    }
  } catch (error) {
    errorMessage.value = error instanceof Error ? error.message : 'Unable to add note'
  }
}
async function addAndShow(){
  await addWebsite()
  await fetchWebsites()
}
</script>

<template>
  <button @click="fetchWebsites">See Sites</button>
  <p v-if="errorMessage">{{ errorMessage }}</p>
  <div v-else-if="websiteData.length" class="sites">
  <article v-for="(website, i) in websiteData" :key="website.url ?? i" class="site">
    <h3>{{ website.url }}</h3>
    <p><star-rating :rating="website.rating" :read-only="true" :max-rating="5" /> </p>
    <ul>
      <li>Easy nav: {{ website.easyNav ? 'Yes' : 'No' }}</li>
      <li>Ad flood: {{ website.adFlood ? 'Yes' : 'No' }}</li>
      <li>Actually free: {{ website.actuallyFree ? 'Yes' : 'No' }}</li>
    </ul>
  </article>
</div>
  <p v-else>No sites loaded yet.</p>
  <input v-model="websiteUrl" placeholder="Enter a new website url"></input>
  <label><input v-model="easyNav" type="checkbox" /> Easy nav</label>
  <label><input v-model="adFlood" type="checkbox" /> Ad flood</label>
  <label><input v-model="actuallyFree" type="checkbox" /> Actually free</label>
  <star-rating v-model:rating="websiteRating" :max-rating="5" :increment="0.5" />   
  <button @click="addAndShow">Add Website</button>
</template>
<style>
.vue-star-rating {
  justify-content: center;
}
</style>