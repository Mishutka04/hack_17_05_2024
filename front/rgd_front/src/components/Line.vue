<template>
    <div class="col-sm-4 chat_block">
        <div class="item_list">
            <div class="list_title">
                <div>Диалоги</div>
            </div>
            <div class="item" :onclick="item">
                <div>№ 1011</div>
                <div><img src="../assets/yes.png" alt="yes" width="30px" height="30px"></div>
            </div>
            <div class="item" :onclick="item">
                <div>№ 1011</div>
                <div><img src="../assets/no.png" alt="yes" width="30px" height="30px"></div>
            </div>
            <div class="item">
                № 123231
            </div>
        </div>

    </div>
    <div class="col-sm-6">
        <div class="stat_title">Результат</div>
        <div>Метрика - 15%</div>

        <BarChart />
    </div>
</template>

<script>
export default {
    methods: {
        item(id) {
            console.log(this.$route.params.eventid)
        }
    }
}


</script>