<template>
  <div class="about">
    <h1>This is an about page</h1>
    <div id="ele">{{ info }}</div>
  </div>
</template>

<script>
import axios from "../http-common";

export default {
  // el: "#ele",
  data() {
    return {
      info: null
    };
  },
  mounted() {
    // If it works, it'll respond with a success message
    axios.get("/").then(response => {
      this.info = response.data.message;
    });
  }
};
</script>
