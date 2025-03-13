<script setup>
import { ref, onMounted, onUnmounted, nextTick } from 'vue'

const props = defineProps({
  monster: Object
})

const emit = defineEmits(['update-monster', 'close'])

const updatedData = ref({ ...props.monster }) 
const formRef = ref(null) 

const handleClickOutside = (event) => {
  if (formRef.value && !formRef.value.contains(event.target)) {
    emit('close')
  }
}

onMounted(async () => {
  await nextTick()
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})

const submitEdit = () => {
  emit('update-monster', updatedData.value)
}
</script>

<template>
  <form ref="formRef" @submit.prevent="submitEdit">
    <label>
      Name :
      <input v-model="updatedData.name" type="text" required />
    </label>

    <label>
      Alignment :
      <input v-model="updatedData.alignment" type="text" required />
    </label>

    <label>
      Type :
      <input v-model="updatedData.types" type="text" required />
    </label>

    <label>
      CR :
      <input v-model="updatedData.cr" type="text" required />
    </label>

    <label>
      AC :
      <input v-model="updatedData.ac" type="number" required />
    </label>

    <label>
      HP :
      <input v-model="updatedData.hp" type="number" required />
    </label>

    <label>
      Speed :
      <input v-model="updatedData.speed" type="text" required />
    </label>

    <label>
      Height :
      <input v-model="updatedData.height" type="text" required />
    </label>

    <label>
      Legendary :
      <input v-model="updatedData.legendary" type="checkbox" />
    </label>

    <button type="submit">Save Changes</button>
  </form>
</template>

<style scoped>
form {
  position: absolute;
  display: flex;
  flex-direction: column;
  left: 100%;
  top: 0;
  min-width: 80%;
  color: black;
  text-align: left;
  background: #fdf1dc;
  padding: 10px;
  border-radius: 5px;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
  z-index: 100;
}

label {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
}
</style>
