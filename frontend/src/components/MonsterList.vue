<script setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'
import MonsterCard from './MonsterCard.vue'

const monsters = ref([]) // on initialise un tableau vide "monsters" pour accueillir nos données de response.data
const types = ref([]) // on initialise un tableau vide "types" pour accueillir nos données de response.data
const alignments = ref([])
const nameFilter = ref('')
const selectedType = ref('All')
const selectedAlignment = ref('All')
const selectedHealth = ref('Any')
const selectedArmor = ref('Any')
const selectedChallenge = ref('Any')
const selectedLegendary = ref('Any')

const fetchTypes = async () => {
  try {
    const response = await axios.get('http://localhost:8000/types')
    types.value = ['All', ...response.data] // injection d'une valeur "All" dans les types
  } catch (error) {
    console.error("Erreur lors de l'appel à l'API pour les types :", error)
  }
}

const fetchAlignments = async () => {
  try {
    const response = await axios.get('http://localhost:8000/alignments')
    alignments.value = ['All', ...response.data] // injection d'une valeur "All" dans les types
  } catch (error) {
    console.error("Erreur lors de l'appel à l'API pour les alignements :", error)
  }
}

onMounted(() => {
  fetchTypes()
  fetchAlignments()
})

const fetchMonsters = async () => {
  try {
    const response = await axios.get('http://localhost:8000/monsters', {
      params: {
        name: nameFilter.value,
        alignment: selectedAlignment.value !== 'All' ? selectedAlignment.value : null,
        types: selectedType.value !== 'All' ? selectedType.value : null
      }
    })
    monsters.value = response.data
  } catch (error) {
    console.error("Erreur lors de l'appel API:", error)
  }
}

const deleteMonster = async (id) => {
  try {
    const response = await axios.delete('http://localhost:8000/monster/' + id)
    if (response.status === 200) {
      monsters.value = monsters.value.filter(monster => monster.id !== id)
    }
  } catch (error) {
    console.error("Erreur lors de l'appel API:", error)
  }
}

const editMonster = async (id, updatedData) => {
  try {
    const response = await axios.put(`http://localhost:8000/monster/${id}`, {
      id, 
      name: updatedData.name,
      types: updatedData.types,
      cr: updatedData.cr,
      alignment: updatedData.alignment,
      ac: updatedData.ac,
      hp: updatedData.hp,
      height: updatedData.height,
      speed: updatedData.speed,
      legendary: updatedData.legendary
    })

    if (response.status === 200) {
      const index = monsters.value.findIndex(monster => monster.id === id)
      if (index !== -1) {
        Object.assign(monsters.value[index], response.data)
      }
    }
  } catch (error) {
    console.error("Erreur lors de l'édition du monstre :", error)
  }
}

const buttonText = computed(() => {
  return nameFilter.value ? "Search" : "Show'em all !"
})
</script>

<template>
  <div class="search-panel">
    <input v-model="nameFilter" placeholder="Search by name"/>
    <div class="filters">
      <div>
        <label for="typeFilter">Type : </label>
        <select v-model="selectedType">
          <option v-for="type in types" :key="type" :value="type" >{{ type }}</option>
        </select>
      </div>
      <div>
        <label for="alignmentFilter">Alignment : </label>
        <select v-model="selectedAlignment">
          <option v-for="alignment in alignments" :key="alignment" :value="alignment">{{ alignment }}</option>
        </select>
      </div>
      <div>
        <label for="healthFilter">Health Points : </label>
        <select id="healthFilter" v-model="selectedHealth">
          <option v-for="(label, value) in { Any: 'Any', True: 'Yes', False: 'No' }" :key="value" :value="value">
            {{ label }}
          </option>
        </select>
      </div>
      <div>
        <label for="armorFilter">Armor Class : </label>
        <select id="armorFilter" v-model="selectedArmor">
          <option v-for="(label, value) in { Any: 'Any', True: 'Yes', False: 'No' }" :key="value" :value="value">
            {{ label }}
          </option>
        </select>
      </div>
      <div>
        <label for="challengeFilter">Challenge Rate : </label>
        <select id="challengeFilter" v-model="selectedChallenge">
          <option v-for="(label, value) in { Any: 'Any', True: 'Yes', False: 'No' }" :key="value" :value="value">
            {{ label }}
          </option>
        </select>
      </div>
      <div>
        <label for="legendaryFilter">Legendary ? </label>
        <select id="legendaryFilter" v-model="selectedLegendary">
          <option v-for="(label, value) in { Any: 'Any', True: 'Yes', False: 'No' }" :key="value" :value="value">
            {{ label }}
          </option>
        </select>
      </div>
    </div>
    <button @click="fetchMonsters">{{ buttonText }}</button>
  </div>
    
  <div class="monster-list">
    <MonsterCard
      v-for="monster in monsters"
      :key="monster.id"
      :monster="monster"
      @delete="deleteMonster"
      @edit="editMonster"
    />
  </div>
</template>

<style scoped>

.monster-list {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
}

button {
  border-radius: 8px;
  border: 1px solid transparent;
  padding: 0.6em 1.2em;
  font-size: 1em;
  font-weight: 500;
  font-family: inherit;
  background-color: #1a1a1a;
  cursor: pointer;
  transition: border-color 0.25s;
}

button:hover {
  border-color: #646cff;
}

button:focus,
button:focus-visible {
  outline: 4px auto -webkit-focus-ring-color;
}

.search-panel {
  display:inline-flex;
  flex-direction: column;
  gap:20px;
  align-items: center;
  width:100%;
}

.filters {
  display:grid;
  grid-template-columns: 1fr 1fr;
  gap:10px;
  text-align:left;
}

.filters div {
  display:flex;
  gap:5px;
}

input {
  margin: 0.5em;
  padding: 0.6em;
  font-size: 1em;
  width: 200px;
}
</style>
