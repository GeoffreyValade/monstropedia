<script setup>
import { ref } from 'vue'

const props = defineProps({
  monster: Object
})

const emit = defineEmits(['create-monster'])

const data = ref({ ...props.monster }) // on crée une copie de la props dans data pour respecter les bonnes pratiques de vue

const submitCreation = () => {
  emit('create-monster', data.value)
}
</script>

<template>
  <form @submit.prevent="submitCreation">
    <label>
      Name :
      <input v-model="data.name" type="text" required />
    </label>

    <label>
      Type :
      <input v-model="data.types" type="text" required />
    </label>

    <label>
      CR :
      <input v-model="data.cr" type="text" required />
    </label>

    <label>
      AC :
      <input v-model="data.ac" type="number" required />
    </label>

    <label>
      HP :
      <input v-model="data.hp" type="number" required />
    </label>

    <label>
      Speed :
      <input v-model="data.speed" type="text" required />
    </label>

    <label>
      Height :
      <input v-model="data.height" type="text" required />
    </label>

    <label>
      Legendary :
      <input v-model="data.legendary" type="checkbox" />
    </label>

    <button type="submit">Create Monster</button>
  </form>
</template>

<style scoped>
form {
  position:absolute;
  left:100%;
  top:0;
  min-width:100%;
  color: black;
  text-align: left;
  background: #fdf1dc;
  padding: 10px;
  border-radius: 5px;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
  z-index:100;
}

label {
  display: block;
  margin-bottom: 10px;
}
</style>
