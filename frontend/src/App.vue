<script setup>
import { ref } from 'vue'
import MonsterList from './components/MonsterList.vue'
import MonsterCreateForm from './components/MonsterCreateForm.vue'

defineProps({
  monster: Object
})

const isEditing = ref(false)
const toggleEdit = () => {
  isEditing.value = !isEditing.value
}
</script>

<template>
  <button class="edit-button" @click="toggleEdit">
    <img class="feather-icon" src="/feather-pen128.png" alt="Edit" />
  </button>

  <MonsterCreateForm 
      v-if="isEditing" 
      :monster="monster" 
      @update-monster="$emit('edit', monster.id, $event)" 
    />

  <h1>Monstropedia</h1>
  <MonsterList />
</template>

