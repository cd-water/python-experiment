<script setup>
import { ref, onMounted } from 'vue'
import { selectChart2Api } from '@/api/chart'

const chart2Data = ref();

const getChart2Data = async () => {
    const result = await selectChart2Api();
    chart2Data.value = result.data.chart1;
}

onMounted(() => {
    getChart2Data();
})

</script>

<template>
    <div class="container">
        <img :src="chart2Data" style="border-radius: 10px;" width="60%"/>
        <!-- <img :src="chart2Data[1]" style="border-radius: 10px;" /> -->
    </div>
</template>

<style scoped>
.container {
    margin-top: 50px;
    display: flex;
    justify-content: center;
    align-items: center;
}
/* .container {
    position: relative;
    height: 55vh;
    display: flex;
    flex-direction: row;
    margin: 0 25px;
    gap: 20px;
} */
</style>