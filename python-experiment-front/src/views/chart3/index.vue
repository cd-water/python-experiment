<script setup>
import { ref, onMounted } from 'vue'
import { selectChart3Api } from '@/api/chart'

const chart3Data = ref([]);

const getChart3Data = async () => {
    const result = await selectChart3Api();
    chart3Data.value = [
        result.data.chart1,
        result.data.chart2,
    ];
}

onMounted(() => {
    getChart3Data();
})
</script>

<template>
    <div class="container">
        <img :src="chart3Data[0]" style="border-radius: 10px;" />
        <img :src="chart3Data[1]" style="border-radius: 10px;" />
    </div>
</template>

<style scoped>
.container {
    position: relative;
    height: 45vh;
    display: flex;
    flex-direction: row;
    margin: 0 25px;
    gap: 20px;
}
</style>