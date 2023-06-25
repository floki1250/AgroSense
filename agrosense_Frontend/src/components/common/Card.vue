<template>
  <div class="card">
    <div class="card-details">
      <div>
        <img :src="img" style="border-radius: 2rem" />
      </div>
      <hr />
      <p class="text-title">{{ title }}</p>
      <p class="description">{{ description }}</p>
      <div>
        <div class="chips mt-1">ID : {{ id }}</div>
        <div class="chips mt-1">Usage :{{ usage }}</div>
      </div>
      <div class="flex justify-content-end">
        <Button icon="pi pi-pencil" class="p-button-rounded p-button-info p-button-text" @click="$emit('edit')" />
        <Button icon="pi pi-trash" class="p-button-danger p-button-text p-button-rounded" @click="$emit('delete')" />
      </div>
    </div>
    <button class="card-button" @click="$emit('details')">More info</button>
  </div>
</template>
<script>
export default {
  props: {
    img: {
      type: String,
      default: "https://fakeimg.pl/200/",
    },
    title: {
      type: String,
      default: "-",
    },
    description: {
      type: String,
      default: " ",
    },
    id: {
      type: Number,
      default: 0,
    },
    usage: {
      type: Number,
      default: 0,
    },
  },
  setup (props) {
    return {
      title: props.title,
      img: props.img,
      id: props.id,
      usage: props.usage,
    };
  },
};
</script>
<style scoped>
img {
  width: 200px;
  height: 150px;
  border-radius: 1rem;
}

.description {
  color: rgb(131, 131, 131);
  font-size: 1em;
  font-weight: bold;
}

.card {
  width: 250px;
  height: fit-content;
  min-height: 350px;
  border-radius: 2rem;
  position: relative;

  border: 2px solid #ffffff;
  transition: 0.5s ease-out;
  overflow: visible;
}

.card-details {
  color: black;
  height: 100%;
  gap: 2px;
  display: grid;
  place-content: center;
}

.chips {
  background-color: whitesmoke;
  border-radius: 2rem;
  padding: 0.5em;
  color: rgb(134, 134, 134);
  font-weight: bold;
}

.card-button {
  transform: translate(-50%, 125%);
  width: 60%;
  border-radius: 1rem;
  border: none;
  background-color: #7dddb5;

  color: #ffffff;
  font-size: 1rem;
  padding: 0.5rem 1rem;
  position: absolute;
  left: 50%;
  bottom: 0;
  opacity: 0;
  transition: 0.3s ease-out;
}

.text-body {
  color: rgb(134, 134, 134);
}

/*Text*/
.text-title {
  font-size: 1.2em;
  font-weight: bold;
}

/*Hover*/
.card:hover {
  border-color: #7dddb5;
  box-shadow: 0 4px 18px 0 rgba(0, 0, 0, 0.25);
}

.card:hover .card-button {
  transform: translate(-50%, 50%);
  opacity: 1;
}
</style>
