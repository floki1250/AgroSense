<template>
  <div class="overlay" :style="{

    left: `${x}px`,
    top: `${y}px`,

  }">
    <commonFancyLoading />
  </div>
</template>
<script setup>
import { useMouse } from '@vueuse/core'

const { x, y, sourceType } = useMouse()
</script>
<style>
.overlay {
  position: absolute;
  pointer-events: none;
  z-index: 99 !important;
  cursor: crosshair !important;
}
</style>
