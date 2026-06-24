function getVideoDuration(file: File): Promise<number> {
  return new Promise((resolve, reject) => {
    const url = URL.createObjectURL(file);
    const video = document.createElement('video');
    video.preload = 'metadata';
    video.src = url;
    const cleanup = () => URL.revokeObjectURL(url);
    video.onloadedmetadata = () => {
      const seconds = Number(video.duration) || 0;
      cleanup();
      resolve(seconds);
    };
    video.onerror = (e) => {
      cleanup();
      reject(new Error('读取视频时长失败'));
    };
  });
}
const file = new File([''], 'test.mp4', { type: 'video/mp4' }); // 真实文件替换
const durationPromise = getVideoDuration(file as File);
durationPromise.then((duration) => {
  console.log('获取视频时长', duration);
});
