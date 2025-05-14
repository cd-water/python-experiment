<script setup>
import { ref, watch } from 'vue'
import { createLineChartApi } from '@/api/chart';
import { ElMessage } from 'element-plus';

const lineChartBase64 = ref([])

const createLineChart = async () => {
    //检查日期是否在允许范围内
    const MIN_DATE = '2022-01-01';
    const MAX_DATE = '2025-04-30';

    if (axisForm.value.xBegin < MIN_DATE || axisForm.value.xEnd > MAX_DATE) {
        ElMessage.error('日期范围不在允许范围内');
        return;
    }
    
    const result = await createLineChartApi(axisForm.value)
    lineChartBase64.value = [
        result.data.chart1,
        result.data.chart2,
        result.data.chart3
    ]
}

const axisForm = ref({
    xDate: [],
    xBegin: '',
    xEnd: '',
    yValue: ''
})

watch(
    () => axisForm.value.xDate,
    (newValue, oldValue) => {
        if (newValue.length == 2) {
            axisForm.value.xBegin = newValue[0]
            axisForm.value.xEnd = newValue[1]
        } else {
            axisForm.value.xBegin = ''
            axisForm.value.xEnd = ''
        }
    }
)


</script>

<template>
    <div class="container">
        <el-form :model="axisForm" class="choice-form" label-width="100px">
            <el-form-item label="x轴日期项">
                <el-date-picker v-model="axisForm.xDate" type="daterange" range-separator="到" start-placeholder="起始日期"
                    end-placeholder="终止日期" value-format="YYYY-MM-DD" />
            </el-form-item>
            <el-form-item label="y轴数值项">
                <el-select v-model="axisForm.yValue" placeholder="请选择y轴数值项" clearable>
                    <el-option label="降水量" value="precipitation" />
                    <el-option label="最高温" value="temp_max" />
                    <el-option label="最低温" value="temp_min" />
                    <el-option label="风力大小" value="wind" />
                </el-select>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="createLineChart()" round size="large">生成折线统计图</el-button>
            </el-form-item>
        </el-form>

        <img :src="lineChartBase64[0]" alt="折线统计图(minAndMax)" class="line-chart" />
        <img :src="lineChartBase64[1]" alt="折线统计图" class="line-chart" />
        <img :src="lineChartBase64[2]" alt="折线统计图(预测)" class="line-chart" />
    </div>
</template>

<style scoped>
.container {
    position: relative;
    height: auto;
    display: flex;
    flex-direction: column;
    margin: 0 25px;
    gap: 20px;
}

.choice-form {
    padding: 20px;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    margin: 0 auto;
}

.line-chart {
    width: 60%;
    margin: auto;
}
</style>