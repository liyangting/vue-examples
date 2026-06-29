<template> 
 <div class="lifecycle-demo">
    <h1>Vue 3 生命周期演示</h1>
    <p>{{ message }}</p>
    <p>打开控制台查看生命周期日志。</p>
    <button @click="triggerAction">触发动作</button>
  </div>
</template>

<script setup lang="ts">
import { onBeforeMount, onMounted, onBeforeUpdate, onUpdated, onBeforeUnmount, onUnmounted, onErrorCaptured, onActivated, onDeactivated, ref} from 'vue';
// 响应式数据
const message = ref('欢迎来到生命周期演示页面');
const triggerAction = () => {   
    message.value = '你点击了按钮！';
    alert('你点击了按钮！');
};
onBeforeMount(() => {
  console.log('组件挂载前，状态和 DOM 都未初始化');
});
onMounted(() => {
  console.log('组件挂载完成');
});
onBeforeUpdate(() => {
  console.log('组件更新前，状态已更新，但 DOM 未同步');
});
onUpdated(() => {
  console.log('组件更新完成，DOM 已同步');
});
onBeforeUnmount(() => {
  console.log('组件即将卸载，还可以访问状态和 DOM');
});
onUnmounted(() => {
  console.log('组件已卸载，无法访问状态和 DOM');
});
onErrorCaptured(() => {
  console.log('组件捕获到错误');
});
onActivated(() => {
  console.log('组件激活，DOM 已挂载');
});
onDeactivated(() => {
  console.log('组件停用，DOM 已卸载');
});
</script>