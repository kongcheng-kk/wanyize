# 网页设计 · 课程作业

万逸泽 · 24001010412

---

## 在线预览

点击下面的链接即可直接看到**渲染后的网页效果**：

| 页面 | 内容 | 在线地址 |
| :--- | :--- | :--- |
| **9-1** | CSS transition 过渡（时长 / 延迟 / 缓动曲线） | [▶ 打开网页](https://kongcheng-kk.github.io/wanyize/9-1.html) |
| **10-1** | CSS animation 关键帧动画（变色盒子 / direction / steps） | [▶ 打开网页](https://kongcheng-kk.github.io/wanyize/10-1.html) |
| **15-1** | 逢 7 过 · 一百个盒子 | [▶ 打开网页](https://kongcheng-kk.github.io/wanyize/15-1.html) |
| **15-2** | JavaScript 程序结构（顺序 / 条件 / 循环） | [▶ 打开网页](https://kongcheng-kk.github.io/wanyize/15-2.html) |
| **17-4** | 远程接口测试台（GET / POST / PUT / PATCH / DELETE） | [▶ 打开网页](https://kongcheng-kk.github.io/wanyize/17-4.html) |
| **17-5** | JavaScript 的两种定时器（setTimeout / setInterval） | [▶ 打开网页](https://kongcheng-kk.github.io/wanyize/17-5.html) |
| **17-6** | Promise 与 async · 包饺子异步流程 | [▶ 打开网页](https://kongcheng-kk.github.io/wanyize/17-6.html) |
| **18-1** | Canvas 粒子动画 · 粒子拼出「万逸泽」 | [▶ 打开网页](https://kongcheng-kk.github.io/wanyize/18-1.html) |
| **18-2** | Canvas 电商系统全栈架构图（可交互动画） | [▶ 打开网页](https://kongcheng-kk.github.io/wanyize/18-2.html) |
| **18-3** | SVG 知识库智能客服系统架构图（科研方向） | [▶ 打开网页](https://kongcheng-kk.github.io/wanyize/18-3.html) |
| **18-4** | ECharts 箱线图 · 1950 年以来各国收入分布 | [▶ 打开网页](https://kongcheng-kk.github.io/wanyize/18-4.html) |
| **18-5** | ECharts 关系图 · 画在笛卡尔坐标系上 | [▶ 打开网页](https://kongcheng-kk.github.io/wanyize/18-5.html) |
| **18-8** | 数据大屏 · 三列布局 · 中国地图实时监控 | [▶ 打开网页](https://kongcheng-kk.github.io/wanyize/18-8.html) |

> **为什么要用上面的链接？**
> GitHub 的代码页面（点进 `.html` 文件看到的那一页）只会把 HTML **以源码形式**展示出来，
> 这是 GitHub 的安全设计，它不会执行网页里的 HTML/CSS/JavaScript。
> 想看真实效果，必须通过 GitHub Pages 的在线地址打开。

---

## 文件说明

- `9-1.html` —— CSS transition 过渡：有无过渡的对比、四个子属性拆解、可调时长/延迟/缓动的实验台（含 transitionend 日志）、五条缓动曲线赛跑、九张卡片 hover 放大与六个常见坑
- `10-1.html` —— CSS animation 关键帧动画：可暂停/变速/单次播放的变色盒子、@keyframes 时间轴、八个 animation 子属性、direction 四种跑法、steps() 逐帧与打字机、fill-mode 四种取值对比
- `15-1.html` —— 100 个盒子，按「7 的倍数 / 个位是 7 / 十位是 7」三条规则筛出空盒子
- `15-2.html` —— JavaScript 三种基本控制结构演示：顺序、条件（if / switch / 三元）、循环（for / while / do…while / for…of / break / continue / 嵌套）
- `17-4.html` —— 远程接口测试台：切换 GET / POST / PUT / PATCH / DELETE，自定义请求体与地址，展示状态码、耗时、响应头、JSON 高亮、错误提示与请求历史
- `17-5.html` —— JavaScript 的两种定时器：setTimeout 圆环倒计时与 clearTimeout 取消、setInterval 秒表与 clearInterval 暂停、0ms 定时器的事件循环顺序、setInterval 任务堆叠与递归 setTimeout 的甘特图对比
- `17-6.html` —— Promise 与 async/await 演示包饺子流程：先买原料，再用 `Promise.all` 让和面、和馅同时进行，附实时时间轴、运行日志、错误补救与串行/并行耗时对比
- `18-1.html` —— Canvas 粒子动画：数千粒子按「万逸泽」像素轮廓就位，可切换字样与密度、打散重聚、鼠标推挤，实时 FPS 显示，附三步走、实现原理、API 速查与五个细节
- `18-2.html` —— Canvas 绘制的电商系统全栈架构图：客户端 / 接入 / 微服务 / 中间件 / 数据 / 第三方六层，逛商品、提交订单、发货通知三条链路的流动数据包动画，节点可点击查看职责说明
- `18-3.html` —— 内联 SVG 绘制的知识库智能客服系统架构图：七层 26 模块（接入 / 会话 / 语义理解 / RAG 检索 / 生成 / 知识底座 / 运营评测），支持点击模块看职责、播放 11 步问答链路，并附六个科研方向与三层评测指标
- `18-4.html` —— ECharts 箱线图：dataset 的 filter / aggregate / sort 三级变换，把 1540 行原始表算成 19 个国家的收入分位数，附原始散点开关与 dataZoom；ECharts 5.5.1、聚合插件与示例数据都放在 `cdn/echarts/`，离线可用
- `18-5.html` —— ECharts 关系图：`layout:'none'` + `coordinateSystem:'cartesian2d'` 把周一到周日 7 个节点钉在类目轴与数值轴上，箭头表示流向，可重新生成随机数据、切换数值标签
- `18-8.html` —— ECharts 数据大屏（全国电商实时监控）：三列布局，中列上方为中国地图（省级填色 + 城市散点 + 上海发出的飞线），另有 KPI、TOP8 条形、品类环图、24 小时趋势、渠道玫瑰、履约仪表与实时成交列表；地图数据用 DataV.GeoAtlas 行政区划（含台湾省、南海诸岛），仅用于教学演示

每个页面都是自包含的单文件，CSS 与 JavaScript 全部内嵌；图片放在 `image/`，图标字体与库放在 `cdn/`，均以相对路径引用。`cdn/echarts/` 内含 ECharts 主库、聚合变换插件与示例数据（json + 供 file:// 兜底的 js 副本）。
