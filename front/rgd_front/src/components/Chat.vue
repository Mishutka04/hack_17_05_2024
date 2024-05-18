<template>
  <div class="row">
    <div class="col-sm-2 left_row">
      <div class="item_list">
        <div class="list_title">
          Маршруты
        </div>
        <div v-for="(line, index) in lines" :key='index' v-if="lines">
          <div class="item" @click="Mark_get(line.id)">
            {{ line.title }}
          </div>
        </div>
      </div>
    </div>

    <div class="col-sm-4 chat_block">
      <div class="chat">
        <div class="chat_title">ID: 123123</div>
        <div class="chat_messages" style="overflow-y:scroll;">
          <div v-if="message">
            <div class="left_message">
              <div class="message left">
                <div class="voice">
                  <div class="play">
                    <img src="../assets/play.svg" alt="" width="50px" height="50px"
                      @click="play(message[0].audio_file)">
                  </div>
                  <div class="sound">
                    <img src="../assets/sound.svg" alt="" height="50px">
                  </div>

                </div>
                <div class="text">
                  {{ message[0].audio_text }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="col-sm-6">
      <div class="stat_title">Результат</div>
      <div>Метрика - 15%</div>
      <div>
        <canvas id="myChart" width="500" height="500"></canvas>
      </div>

    </div>
  </div>
</template>

<script>
import { useRoute } from "vue-router";
import { useRouter } from "vue-router";
import axios from 'axios';
import Chart from 'chart.js/auto';
export default {
  data() {
    return {
      lines: null,
      message: null,
      audio_voice: null,
      chat_id: null
    }
  },
  setup() {
    const route = useRoute();
    const router = useRouter();

    function Mark_get(id) {
      router.push('/route/' + id);
    };
    return {
      Mark_get, route
    }
  },
  methods: {
    play(path_file) {
      if (this.audio_voice) {

        console.log('stop');
        this.audio_voice.pause();
        this.audio_voice = null;

      } else {
        console.log('start');
        console.log(path_file);
        this.audio_voice = new Audio(path_file); // path to file
        this.audio_voice.play();
      }
    }
  },
  mounted() {
    const ctx = document.getElementById('myChart');
    new Chart(ctx, {
      type: 'pie',
      data: {
        labels: ["Нарушения", "Без нарушений"],
        datasets: [{
          label: "Population (millions)",
          backgroundColor: ["#FF0000", "#008000"],
          data: [10, 30]
        }]
      },
      options: {
        title: {
          display: true,
          text: 'Predicted world population (millions) in 2050'
        },
        responsive: false,
      }
    });
    axios.get('http://127.0.0.1:8000/api/negotiations_info/' + this.route.params.chat_id,).then(response => {
      this.message = response.data
    }),
    axios.get('http://127.0.0.1:8000/api/lines/').then(response => {
                this.lines = response.data
            })
  }
}




</script>