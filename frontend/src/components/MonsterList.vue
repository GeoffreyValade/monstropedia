<script setup>
import MonsterCard from './MonsterCard.vue'

defineProps({
  monsters: Array
})
</script>

<template>
  <div class="monster-list">
    <MonsterCard
      v-for="monster in monsters"
      :key="monster.id"
      :monster="monster"
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
