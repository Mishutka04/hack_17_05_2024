<template>
    <div class="container">
        <div class="row">
            <div class="col-sm-5 height">
                <div class="category">
                    <div class="category_description">
                        <div>
                            <div class="block_title">Категория</div>
                            <div class="line"></div>
                            <div v-for="(line, index) in lines" :key='index' v-if="lines">
                                <div class="item" @click="Mark_get(line.id)">
                                    <div>{{ line.title }}</div>
                                </div>
                            </div>
                        </div>
                        <div class="mark">
                            <div class="container">
                                <div class="mark_content">
                                    <div class="mark_items">
                                        <div class="mark_item">
                                            <div><img src="../assets/yes.png" alt="yes" width="30px" height="30px">
                                            <div>Нарушений нет</div>
                                            
                                            </div>
                                        </div>
                                        <div class="mark_item">
                                            <div><img src="../assets/no.png" alt="yes" width="30px" height="30px">
                                            <div>Нарушения</div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
            <div class="col-sm-7 height">
                <div class="graph">
                    <div class="block_title">График</div>
                    <div class="line"></div>
                    <div class="grafic">
                        <canvas id="myChart" width="300" height="300"></canvas>
                    </div>
                </div>
                <div class="stat">
                    <div class="block_title">Дополнительная информация</div>
                    <div class="line"></div>
                    <div class="stat_item">Качество переговоров - {{ this.sr_count }} %</div>
                    <div class="stat_item">Качество нарушений - {{ this.count_not_accept }}</div>
                    <div class="stat_item">Качество переговоров без нарушений - {{ this.count_accept }}</div>
                    
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { useRouter } from "vue-router";
import axios from 'axios';
import Chart from 'chart.js/auto';
export default {
    components: {
        
    },
    data() {
        return {
            lines: null,
            count_accept: 0,
            count_not_accept: 0,
            sr_count: 0,
        }
    },
    setup() {
        const router = useRouter();
        function Mark_get(id) {
            console.log(id)
            router.push('/route/' + id);
        };
        return {
            Mark_get
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/api/lines/').then(response => {
            this.lines = response.data
        }),
            axios.get('http://127.0.0.1:8000/api/negotiations/').then(response => {
                for (let i = 0; i < response.data.length; i++) {
                    if (response.data[i].regulations_complies) {
                        this.count_accept = this.count_accept + 1;
                    } else {
                        this.count_not_accept = this.count_not_accept + 1;
                    };
                    this.sr_count = this.sr_count + response.data[i].percentage_compliance;
                };
                this.sr_count = this.count_accept * 100 / response.data.length;
            }),
            setTimeout(() => {

                new Chart(document.getElementById('myChart'), {
                    type: 'pie',
                    data: {
                        labels: ["Нарушения", "Без нарушений"],
                        datasets: [{
                            label: "Единиц",
                            backgroundColor: ["#FF0000", "#008000"],
                            data: [this.count_accept, this.count_not_accept]
                        }]
                    },
                    options: {
                        title: {
                            display: true,
                            text: 'Predicted world population (millions) in 2050'
                        },
                        responsive: false,
                    }
                })
            }, 1000);
    },
}

</script>