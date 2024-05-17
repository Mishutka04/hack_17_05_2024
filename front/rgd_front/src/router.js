import { createRouter, createWebHashHistory } from 'vue-router';
import Line from './components/Line.vue';
import Base from './components/Base.vue';
import Chat from './components/Chat.vue';


export default createRouter({
    history: createWebHashHistory(),
    routes: [
        {name: 'base',path: '', component: Base},
    ]
})