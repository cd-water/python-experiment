import { createRouter, createWebHistory } from "vue-router";

import LayoutView from "@/views/layout/index.vue";
import HomeView from "@/views/home/index.vue";
import Chart1 from "@/views/chart1/index.vue";
import Chart2 from "@/views/chart2/index.vue";
import Chart3 from "@/views/chart3/index.vue";

const routes = [
  {
    path: "/",
    name: "",
    component: LayoutView,
    redirect: "/home", //重定向
    children: [
      { path: "/home", component: HomeView },
      { path: "/chart1", component: Chart1 },
      { path: "/chart2", component: Chart2 },
      { path: "/chart3", component: Chart3 },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes,
});

export default router;
