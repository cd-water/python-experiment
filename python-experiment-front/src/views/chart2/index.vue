<script setup>
import { ref, onMounted } from 'vue'
import { selectChart2Api } from '@/api/chart'

const chart2Data = ref([]);

const getChart2Data = async () => {
    const result = await selectChart2Api();
    chart2Data.value = result.data.image;
}

onMounted(() => {
    getChart2Data();
})

</script>

<template>
    <div class="container">
        <img :src="chart2Data"/>
    </div>
</template>

<style scoped></style>