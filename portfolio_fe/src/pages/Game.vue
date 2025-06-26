<template>
  <div class="text-body-2 font-weight-light mb-n1">A Game Four</div>
  <v-container>
    <GameBoard />
    <ScoreDisplay />
    <GameController />
  </v-container>
</template>
<script setup>
  import { defineAsyncComponent, ref, watchEffect } from 'vue'
  import GameBoard from '../components/GameBoard.vue'
  import ScoreDisplay from '../components/ScoreDisplay.vue'
  import GameController from '../components/GameController.vue'
</script>
