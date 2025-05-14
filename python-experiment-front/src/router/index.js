import { createRouter, createWebHistory } from "vue-router";

import LayoutView from "@/views/layout/index.vue";
import HomeView from "@/views/home/index.vue";
import LineChart from "@/views/line/index.vue";
import PieChart from "@/views/pie/index.vue";
import BarChart from "@/views/bar/index.vue";
import ClassifyChart from "@/views/classify/index.vue";

const routes = [
  {
    path: "/",
    name: "",
    component: LayoutView,
    redirect: "/home", //重定向
    children: [
      { path: "/home", component: HomeView },
      { path: "/line", component: LineChart },
      { path: "/pie", component: PieChart },
      { path: "/bar", component: BarChart },
      { path: "/newChart", component: ClassifyChart },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes,
});

export default router;
