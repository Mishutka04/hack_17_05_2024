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
            <div>Метрика - 15%</div>

        </div>
    </div>
</template>

<script>
import { useRouter } from "vue-router";
import { useRoute } from "vue-router";
import axios from 'axios';
export default {
    data() {
        return {
            lines: null,
            dialog: null,
        }
    },
    setup() {
        const router = useRouter();
        const route = useRoute();
        function Mark_get(id) {
            console.log(id)
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
        }),
            axios.get('http://127.0.0.1:8000/api/lines/').then(response => {
                this.lines = response.data
            })
    },
}

</script>