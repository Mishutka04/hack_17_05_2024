<script>
import Chat from "./components/Chat.vue"
import BarChart from "./components/BarChart.vue"
import Line from "./components/Line.vue"
export default {
  name: 'App',
  components: { BarChart, Chat, Line },
  data() {
    return {
      category: null,
    }
  }
}
</script>

<template>
  <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
    <div class="container-fluid">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" href="#">Active</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" href="#">Disabled</a>
        </li>
      </ul>
    </div>
  </nav>
  <div class="row">
    <div class="col-sm-2 left_row">
      <div class="item_list">
        <div class="list_title">
          Маршруты
        </div>
        <div class="item">
          № 123231
        </div>
        <div class="item">
          № 123231
        </div>
        <div class="item">
          № 123231
        </div>
      </div>
    </div>
    <router-view :key='$route.fullPath'></router-view>
  </div>
</template>

<style>
.chart-container {
  background-color: #eee8d5;
  border-radius: 0.5rem;
}
</style>
