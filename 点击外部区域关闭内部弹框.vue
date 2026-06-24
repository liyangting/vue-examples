<script setup lang="ts">
//全局点击事件处理器，用于实现"点击外部区域关闭弹窗"的交互功能
import { onMounted, onBeforeUnmount, ref } from 'vue';
export const visible = ref(false); // 弹窗是否显示的状态变量
const handleDocumentClick = (event: MouseEvent) => {
  if (!visible.value) return; // 如果弹窗不显示，直接返回
  const target = event.target as Node | null; // 获取点击事件的目标元素
  if (!target) return; // 如果目标元素不存在，直接返回
  // 点击视频外部区域关闭弹窗
  const layoutContent = document.querySelector('.course-content'); // 获取弹窗内容区域元素
  if (layoutContent && !layoutContent.contains(target)) {
    // 如果点击事件的目标元素不在弹窗内容区域内，关闭弹窗
    visible.value = false;
  }
};

onMounted(() => {
  document.addEventListener('click', handleDocumentClick);
});
onBeforeUnmount(() => {
  document.removeEventListener('click', handleDocumentClick);
});
</script>