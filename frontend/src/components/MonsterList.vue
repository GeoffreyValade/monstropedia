<script setup>
import MonsterCard from './MonsterCard.vue'
import { ref, watchEffect } from 'vue'
import axios from 'axios'

const props = defineProps({
  monsters: Array
})

const monstersList = ref([...props.monsters])

watchEffect(() => {
  monstersList.value = [...props.monsters]
})

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
      v-for="monster in monstersList"
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
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 10px;
}
</style>

<style scoped>

.monster-list {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  width:100%;
}
</style>