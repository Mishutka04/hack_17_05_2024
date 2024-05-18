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
            <div class="item_list">
                <div class="list_title">
                    <div>Диалоги</div>
                </div>
                <div v-for="(dial, index) in dialog" :key='index' v-if="lines">
                    <div class="item" @click="Item_get(dial.id)">
                        <div>{{ dial.title }}</div>
                            <div v-if="dial.regulations_complies"><img src="../assets/yes.png" alt="yes" width="30px"
                                height="30px"></div>
                        <div v-else><img src="../assets/no.png" alt="yes" width="30px" height="30px"></div>
                    </div>
                </div>
            </div>

        </div>
        <div class="col-sm-6">
            <div class="stat_title">Результат</div>
            <div>Качество переговоров - {{ this.sr_count }} %</div>
            <div>Качество нарушений - {{ this.count_not_accept }}</div>
            <div>Качество переговоров без нарушений - {{ this.count_accept }}</div>
            <canvas id="myChart" width="500" height="500"></canvas>
        </div>
    </div>
</template>

<script>
import { useRouter } from "vue-router";
import { useRoute } from "vue-router";
import axios from 'axios';
import Chart from 'chart.js/auto';
export default {
    data() {
        return {
            lines: null,
            dialog: null,
            count_accept: 0,
            count_not_accept: 0,
            sr_count:0,
        }
    },
    setup() {
        const router = useRouter();
        const route = useRoute();
        function Mark_get(id) {
            router.push('/route/' + id);
        };
        function Item_get(id) {
            router.push('/route/' + route.params.category_id + '/chat/' + id);
        };
        return {
            Mark_get, Item_get, route
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/api/negotiations/' + this.route.params.category_id).then(response => {
            this.dialog = response.data;
            for (let i = 0; i < this.dialog.length; i++) {
                if (this.dialog[i].regulations_complies) {
                    this.count_accept =  this.count_accept + 1;
                } else {
                    this.count_not_accept =  this.count_not_accept + 1;
                };
                this.sr_count = this.sr_count + this.dialog[i].percentage_compliance;
            };
            this.sr_count = this.count_accept * 100 / this.dialog.length;
        }),
            axios.get('http://127.0.0.1:8000/api/lines/').then(response => {
                this.lines = response.data;

            }),
            setTimeout(() => {
                
                new Chart(document.getElementById('myChart'), {
                    type: 'pie',
                    data: {
                        labels: ["Нарушения", "Без нарушений"],
                        datasets: [{
                            label: "Единиц",
                            backgroundColor: ["#FF0000", "#008000"],
                            data: [ this.count_accept,  this.count_not_accept]
                        }]
                    },
                    options: {
                        title: {
                            display: true,
                            text: 'Predicted world population (millions) in 2050'
                        },
                        responsive: false,
                    }
                })}, 1000);
                console.log( this.count_accept);
    },

}

</script>