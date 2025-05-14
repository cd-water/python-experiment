<script setup>
import { ref, watch } from 'vue'
import { createClassifyChartApi } from '@/api/chart'
import { ElMessage } from 'element-plus';

const classifyChartBase64 = ref([])

const createClassifyChart = async () => {
    //检查日期是否在允许范围内
    const MIN_DATE = '2022-01-01';
    const MAX_DATE = '2025-04-30';

    if (classifyForm.value.begin < MIN_DATE || classifyForm.value.end > MAX_DATE) {
        ElMessage.error('日期范围不在允许范围内');
        return;
    }

    const result = await createClassifyChartApi(classifyForm.value)
    classifyChartBase64.value = [
        result.data.chart1,
        result.data.chart2
    ]

}

const classifyForm = ref({
    date: [],
    begin: '',
    end: ''
})

watch(
    () => classifyForm.value.date,
    (newValue, oldValue) => {
        if (newValue.length == 2) {
            classifyForm.value.begin = newValue[0]
            classifyForm.value.end = newValue[1]
        } else {
            classifyForm.value.begin = ''
            classifyForm.value.end = ''
        }
    }
)

</script>

<template>
    <div class="container">
        <el-form :model="classifyForm" class="choice-form" label-width="100px">
            <el-form-item label="统计日期区间">
                <el-date-picker v-model="classifyForm.date" type="daterange" range-separator="到"
                    start-placeholder="起始日期" end-placeholder="终止日期" value-format="YYYY-MM-DD" />
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="createClassifyChart()" round size="large">生成分类图</el-button>
            </el-form-item>
        </el-form>
        <img :src="classifyChartBase64[0]" alt="分类图" class="classify-chart" />
        <img :src="classifyChartBase64[1]" alt="分类图" class="classify-chart" />
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

.classify-chart {
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