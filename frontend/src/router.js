import Vue from "vue";
import VueRouter from "vue-router";
import Home from "./views/Home";
import Search from "./views/Search";

Vue.use(VueRouter);

const router = new VueRouter({
    mode: "history",
    routes: [
        {path:"/", component: Home},
        {path:"/search", component: Search}
    ]
});

export default router;