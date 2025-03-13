<script setup>
import MonsterCard from './MonsterCard.vue'
import { ref, computed, watchEffect } from 'vue'
import axios from 'axios'

const props = defineProps({
  monsters: Array
})

// Faire une copie locale réactive
const monstersList = ref([...props.monsters])

// Mettre à jour la copie locale quand les props changent
watchEffect(() => {
  monstersList.value = [...props.monsters]
})

// Paramètres de pagination
const itemsPerPage = 12
const currentPage = ref(1)

// Calcul du nombre total de pages
const totalPages = computed(() => Math.ceil(monstersList.value.length / itemsPerPage))

// Filtrer les monstres pour afficher seulement ceux de la page courante
const paginatedMonsters = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  const end = start + itemsPerPage
  return monstersList.value.slice(start, end)
})

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++
  }
}

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--
  }
}

const deleteMonster = async (id) => {
  try {
    const response = await axios.delete(`http://localhost:8000/monster/${id}`)
    if (response.status === 200) {
      monstersList.value = monstersList.value.filter(monster => monster.id !== id)
    }
  } catch (error) {
    console.error("Erreur lors de l'appel API:", error)
  }
}

const editMonster = async (id, updatedData) => {
  try {
    const response = await axios.put(`http://localhost:8000/monster/${id}`, updatedData)

    if (response.status === 200) {
      const index = monstersList.value.findIndex(monster => monster.id === id)
      if (index !== -1) {
        Object.assign(monstersList.value[index], response.data)
      }
    }
  } catch (error) {
    console.error("Erreur lors de l'édition du monstre :", error)
  }
}
</script>

<template>
  <div class="monster-list">
    <MonsterCard
      v-for="monster in paginatedMonsters"
      :key="monster.id"
      :monster="monster"
      @delete="deleteMonster"
      @edit="editMonster"
    />
  </div>

  <div class="pagination">
    <button @click="prevPage" :disabled="currentPage === 1">Précédent</button>
    <span>Page {{ currentPage }} / {{ totalPages }}</span>
    <button @click="nextPage" :disabled="currentPage === totalPages">Suivant</button>
  </div>
</template>

<style scoped>
.monster-list {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  gap: 10px;
  width:100%;
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
  margin-top: 20px;
}

button {
  padding: 5px 10px;
  cursor: pointer;
}

button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>
