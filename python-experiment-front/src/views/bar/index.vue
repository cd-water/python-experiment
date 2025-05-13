<script setup>
import { ref, watch } from 'vue'
import { createBarChartApi } from '@/api/chart'
import { ElMessage } from 'element-plus';

const barChartBase64 = ref('')

const createBarChart = async () => {
    //检查日期是否在允许范围内
    const MIN_DATE = '2022-01-01';
    const MAX_DATE = '2025-04-30';

    if (barForm.value.begin < MIN_DATE || barForm.value.end > MAX_DATE) {
        ElMessage.error('日期范围不在允许范围内');
        return;
    }
    
    const result = await createBarChartApi(barForm.value)
    barChartBase64.value = result.data.chart

    
}

const barForm = ref({
    date: [],
    begin: '',
    end: ''
})

watch(
    () => barForm.value.date,
    (newValue, oldValue) => {
        if (newValue.length == 2) {
            barForm.value.begin = newValue[0]
            barForm.value.end = newValue[1]
        } else {
            barForm.value.begin = ''
            barForm.value.end = ''
        }
    }
)

</script>

<template>
    <div class="container">
        <el-form :model="barForm" class="choice-form" label-width="100px">
            <el-form-item label="统计日期区间">
                <el-date-picker v-model="barForm.date" type="daterange" range-separator="到" start-placeholder="起始日期"
                    end-placeholder="终止日期" value-format="YYYY-MM-DD" />
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="createBarChart()" round size="large">生成柱状图</el-button>
            </el-form-item>
        </el-form>
        <img :src="barChartBase64" alt="柱状图" class="bar-chart" />
    </div>
</template>

<style scoped>
.container {
    position: relative;
    min-height: 60vh;
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    border-radius: 8px;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
    height: 45vh;
}

.bar-chart {
    width: 60%;
    margin: auto;
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