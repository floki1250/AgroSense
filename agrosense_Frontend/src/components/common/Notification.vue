<template>
  <div>
    <h5>Notification</h5>
  </div>

  <div class="Notif-scroll">
    <div v-for="i in 50" :key="i">
      <div class="NotifItem">
        Notif{{ i }}
      </div>
    </div>
  </div>
</template>

<style scoped>
h5 {
  color: rgb(138, 138, 138);
  font-weight: 500;
}

.NotifItem {
  margin: 5px;
  background-color: rgb(255, 255, 255);
  padding: 10px;
  border-radius: 2rem;
  box-shadow: rgba(236, 236, 236, 0.08) 0px 4px 12px;
  border: 1px solid rgba(70, 209, 156, 0.26);
}

.Notif-scroll {
  max-height: 100px;
  /* set the maximum height of the container */
  overflow: auto;
  /* enable scrolling when content exceeds container height */
}
</style>
