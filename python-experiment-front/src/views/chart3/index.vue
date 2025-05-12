<script setup>
import { ref, onMounted } from 'vue'
import { selectChart3Api } from '@/api/chart'

const chart3Data = ref([]);

const getChart3Data = async () => {
    const result = await selectChart3Api();
    chart3Data.value = result.data.image;
}

onMounted(() => {
    getChart3Data();
})
</script>

<template>
    <div class="container">
        <img :src="chart3Data"/>
    </div>
</template>

<style scoped></style>