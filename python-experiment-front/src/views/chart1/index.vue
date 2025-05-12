<script setup>
import { ref, onMounted } from 'vue'
import { selectChart1Api } from '@/api/chart'

const chart1Data = ref([]);

const getChart1Data = async () => {
    const result = await selectChart1Api();
    chart1Data.value=[
        result.data.chart1,
        result.data.chart2
    ]
}

onMounted(() => {
    getChart1Data();
})
</script>

<template>
    <div class="container">
        <img :src="chart1Data[0]" style="border-radius: 10px;"/>
        <img :src="chart1Data[1]" style="border-radius: 10px;"/>

        <div v-if="chart1Data[0] || chart1Data[1]" class="person-data">
            <h2>Stephen Curry 个人生涯</h2>
            <p>美国职业篮球运动员（控球后卫）
                1988年3月14日生于俄亥俄州阿克伦
                现效力：金州勇士队（2009年至今）
                <br>
                主要成就：
                <br>
                🏆 4届NBA总冠军（2015/2017/2018/2022）
                <br>
                ⭐ 2次常规赛MVP & 1次总决赛MVP
                <br>
                👑 历史三分王（常规赛+季后赛双纪录）
                <br>
                🔥 2届得分王 & 最佳关键球员（2024）
                <br>
                🌟 11届全明星 & 2届全明星MVP
                <br>
                🏅 NBA75大巨星 & 10次最佳阵容
                <br>
                国家队荣誉：
                <br>
                🇺🇸 世锦赛冠军（2010）
                🇺🇸 篮球世界杯冠军（2014）
                🇺🇸 奥运会金牌（2024巴黎）
            </p>
        </div>
    </div>
</template>

<style scoped>
.container {
    position: relative;
    height: 55vh;
    display: flex;
    flex-direction: row;
    margin: 0 25px;
    gap: 20px;
}

.person-data {
    flex: 0 0 280px;
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.person-data h2 {
    color: #131010;
    font-size: 1.5em;
    margin-bottom: 15px;
    border-bottom: 2px solid #007bff;
    padding-bottom: 8px;
}
</style>