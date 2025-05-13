<script setup>
import { ref, onMounted, watch } from 'vue'
import { createPieChartApi } from '@/api/chart'
import { ElMessage } from 'element-plus';

const pieChartBase64 = ref('')

const createPieChart = async () => {
    //检查日期是否在允许范围内
    const MIN_DATE = '2022-01-01';
    const MAX_DATE = '2025-04-30';

    if (pieForm.value.begin < MIN_DATE || pieForm.value.end > MAX_DATE) {
        ElMessage.error('日期范围不在允许范围内');
        return;
    }
    
    const result = await createPieChartApi(pieForm.value)
    pieChartBase64.value = result.data.chart
}

const pieForm = ref({
    date: [],
    begin: '',
    end: ''
})

watch(
    () => pieForm.value.date,
    (newValue, oldValue) => {
        if (newValue.length == 2) {
            pieForm.value.begin = newValue[0]
            pieForm.value.end = newValue[1]
        } else {
            pieForm.value.begin = ''
            pieForm.value.end = ''
        }
    }
)

</script>

<template>
    <div class="container">
        <el-form :model="pieForm" class="choice-form" label-width="100px">

            <el-form-item label="统计日期区间">
                <el-date-picker v-model="pieForm.date" type="daterange" range-separator="到" start-placeholder="起始日期"
                    end-placeholder="终止日期" value-format="YYYY-MM-DD"/>
            </el-form-item>

            <el-form-item>
                <el-button type="primary" @click="createPieChart()" round size="large">生成饼状图</el-button>
            </el-form-item>
        </el-form>
    </div>

    <img :src="pieChartBase64" alt="饼状图" class="pie-chart"/>
</template>

<style scoped>
.container {
    position: relative;
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    border-radius: 8px;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
    height: 10vh;
}

.pie-chart {
    width: 60%;
    margin: 0 auto;
    display: block; 
}

.choice-form {
    padding: 20px;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);

    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: row;
    margin: 0 auto;
}
</style>