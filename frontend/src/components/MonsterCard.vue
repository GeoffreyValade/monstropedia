<script setup>
import { ref } from 'vue'
import MonsterEditForm from './MonsterEditForm.vue'

defineProps({
  monster: Object
})

const isEditing = ref(false) // permet de surveiller la valeur de isEditing pour gérer le toggle on/off du form d'edit
const toggleEdit = () => {
  isEditing.value = !isEditing.value
}  // permet de changer la valeur de isEditing pour activer/désactiver le form d'edit
</script>

<template>
  <div class="global-card">
    <div class="monster-card" :id="'monster-' + monster.id">
        <span><b>Challenge Rate :</b> {{ monster.cr }}</span>
      <h2>{{ monster.name }}</h2>
      <ul>
        <li><b>Type :</b> {{ monster.types }}</li>
        <li><b>Alignment :</b> {{ monster.alignment }}</li>
        <li><b>AC :</b> {{ monster.ac }} | <b>HP :</b> {{ monster.hp }}</li>
        <li><b>Speed :</b> {{ monster.speed }} | <b>Height :</b> {{ monster.height }}</li>
        <li><b>Legendary :</b> {{ monster.legendary ? 'Yes' : 'No' }}</li>
      </ul>
      <button class="edit-button" @click.stop="toggleEdit">
        <img class="feather-icon" src="/feather-pen128.png" alt="Edit" />
      </button>

      <button class="delete-button" @click="$emit('delete', monster.id)">
        <img class="skull-icon" src="/skull128.png" alt="Delete" />
      </button>
    </div>

    <MonsterEditForm 
  v-if="isEditing"
  :monster="monster"
  @update-monster="$emit('edit', monster.id, $event)" 
  @close="isEditing = false" 
/>
  </div>
</template>

<style scoped>
h2 {
  margin-top: 0px;
  margin-bottom: 10px;
}

.global-card {
  position: relative;
}

.monster-card {
  position: relative;
  text-align: center;
  color: #6D0000;
  padding: 10px;
  margin: 10px;
  min-height: 230px;
  min-width:20%;
  border-radius: 5px;
  background: #fdf1dc;
  background-image: url(/fond-mm-effet.png), url(/fond-ph.jpg);
  background-repeat: no-repeat, repeat;
  box-shadow: 4px 5px 4px 1px rgba(0, 0, 0, 0.4);
}

ul {
  list-style: none;
  padding:0;
  margin:0;
}

li {
  text-align: left;
}

.edit-button {
  right: 37px;
}

.delete-button {
  right: 5px;
}

button {
  position: absolute;
  top: 5px;
  width: 26px;
  height: 26px;
  padding:0;
  background: transparent;
  cursor: pointer;
  overflow: hidden;
}

.skull-icon, .feather-icon {
  width: 100%;
  height: 100%;
}
</style>