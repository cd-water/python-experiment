<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();
const showChart1 = async () => {
    router.push('/chart1');
}

const showChart2 = () => {
    router.push('/chart2');
}

const showChart3 = () => {
    router.push('/chart3');
}

</script>

<template>
    <div class="bg_image"></div>

    <div class="container">
        <h1 class="title">Python 交互式数据分析系统</h1>

        <div class="button-container">
            <el-button @click="showChart1()" class="chart-btn">图表1</el-button>
            <el-button @click="showChart2()" class="chart-btn">图表2</el-button>
            <el-button @click="showChart3()" class="chart-btn">图表3</el-button>
        </div>

        <div class="show-area">
            <router-view></router-view>
        </div>
    </div>
</template>

<style scoped>
.bg_image {
    position: fixed;
    background-image: url("../../assets/bg.jpg");
    background-size: cover;
    height: 100vh;
    width: 100vw;
    top: 0;
    left: 0;
}

.container {
    position: relative;
    height: 50vh;
    display: flex;
    flex-direction: column;
}

.title {
    text-align: center;
    color: rgb(58, 173, 77);
    font-size: 3em;
}

.button-container {
    height: 10%;
    min-height: 80px;
    display: flex;
    justify-content: center;
    gap: 50px;
    margin-bottom: 50px;
}

.chart-btn {
    display: flex;
    flex: 0 1 200px;
    border-radius: 25px;
    font-size: 2em;
    font-weight: 500;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    transition: all 0.3s ease;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: white;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.chart-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
}

.chart-btn:active {
    transform: translateY(0);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* .show-area {
    display: flex;
    justify-content: center;
} */
</style>