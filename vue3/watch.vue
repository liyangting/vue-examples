
<script setup lang="ts">
import { ref, reactive, watch ,watchEffect} from 'vue';
// 响应式数据
const message = ref('欢迎来到生命周期演示页面');
const count = ref(0);
const obj = reactive({
  name: '张三',
  age: 18
});

// 多数据源监听。监听目标是一个数组，表示监听多个依赖项
// 当监听目标是数组时，watch 不会提供旧值（即没有第二个参数）
// 需要同时监听多个响应式数据的变化
watch([count, message], ([newCount, newMessage]) => {
  console.log(`count 值已更新为 ${newCount}`);
  console.log(`message 值已更新为 ${newMessage}`);
});

// 多数据源监听。监听目标是一个数组，表示监听多个依赖项
watch([() => obj.age, () => obj.name], ([newAge, newName]) => {
  console.log(`age 值已更新为 ${newAge}`);
  console.log(`name 值已更新为 ${newName}`);
});





// 使用 watch 监听依赖变化 需要手动传入要监听的响应式数据（如 ref 或 reactive 对象的某个属性）
// 监听单个响应式数据，支持旧值获取
watch(() => message.value, (newValue, oldValue) => {
  console.log(`message 从 ${oldValue} 变更为 ${newValue}`);
});





// 使用 watchEffect 监听依赖变化 不需要手动指定监听目标，它会自动追踪回调函数内部使用的响应式数据
// 首次运行时就会执行一次回调，然后在依赖变化时再次触发
// 只能获取新值，无法像 watch 那样拿到旧值。
// watchEffect 适合用于处理副作用，如数据请求、DOM 操作等
watchEffect(() => {
  console.log(`当前 message 值为：${message.value}`);
});
</script>