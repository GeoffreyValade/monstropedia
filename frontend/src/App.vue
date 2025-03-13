<script setup>
import { ref } from 'vue'
import MonsterList from './components/MonsterList.vue'
import MonsterCreateForm from './components/MonsterCreateForm.vue'
import SearchPanel from './components/SearchPanel.vue'

defineProps({
  monster: Object
})

const monsters = ref([])

const updateMonsters = (newMonsters) => {
  monsters.value = newMonsters
}

const isEditing = ref(false)
const toggleEdit = () => {
  isEditing.value = !isEditing.value
}

const createNewMonster = async (id, updatedData) => {
  try {
    const response = await axios.post(`http://localhost:8000/monster/`, {
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
</script>

<template>

  <div>
    <button class="edit-button" @click="toggleEdit">
      <img class="feather-icon" src="/feather-pen128.png" alt="Edit" />
    </button>
  
    <MonsterCreateForm 
        v-if="isEditing" 
        :monster="monster" 
        @update-monster="createNewMonster" 
      />
    <h1>Monstropedia</h1>
  </div>

  <SearchPanel @update:monsters="updateMonsters" />
  
  <MonsterList :monsters="monsters" />

</template>

<style scoped>

button {
  position:relative;
  z-index:100;
}

</style>
