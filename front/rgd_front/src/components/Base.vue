<template>
    <div class="container">
        <div class="row">
            <div class="col-sm-5 height">
                <div class="category">
                    <div class="category_description">
                        <div>
                            <div>Категория</div>
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
                                            <div>№ 1011</div>
                                            <div><img src="../assets/yes.png" alt="yes" width="30px" height="30px">
                                            </div>
                                        </div>
                                        <div class="mark_item">
                                            <div>№ 1011</div>
                                            <div><img src="../assets/yes.png" alt="yes" width="30px" height="30px">
                                            </div>
                                        </div>
                                    </div>
                                    <div class="mark_items">
                                        <div class="mark_item">
                                            <div>№ 1011</div>
                                            <div><img src="../assets/yes.png" alt="yes" width="30px" height="30px">
                                            </div>
                                        </div>
                                        <div class="mark_item">
                                            <div>№ 1011</div>
                                            <div><img src="../assets/yes.png" alt="yes" width="30px" height="30px">
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
                    <div>Категория</div>
                    <div class="line"></div>
                    <div class="grafic">
                        График
                    </div>
                </div>
                <div class="stat">
                    <div>Категория</div>
                    <div class="line"></div>
                    <div>sss</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { useRouter } from "vue-router";
import axios from 'axios';
export default {
    data() {
        return {
            lines: null,
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
        })
    },
}

</script>