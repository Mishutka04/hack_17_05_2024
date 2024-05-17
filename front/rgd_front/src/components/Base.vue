<template>
    <div class="col-sm-4 chat_block">
        <div class="item_list">
            <div class="list_title">
                <div>Диалоги</div>
            </div>
            <div class="item" :onclick="router.push('/route/' + 2)">
                <div>№ 1011</div>
                <div><img src="../assets/yes.png" alt="yes" width="30px" height="30px"></div>
            </div>
            <div class="item" :onclick="item(1)">
                <div>№ 1011</div>
                <div><img src="../assets/no.png" alt="yes" width="30px" height="30px"></div>
            </div>
            <div class="item">
                № 123231
            </div>
        </div>

    </div>
    <div class="col-sm-6">
    </div>
</template>

<script setup>
import { useRouter } from "vue-router";
const router = useRouter();
//function item(id) {
//    router.push('/route/' + id);
//}

</script>