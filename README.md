# 麻洪豪 · Mahonghao

**机器人采回来的数据，我负责让它变成下游敢直接训的交付包。**

2027 届 · 上海应用技术大学 机器人工程 · 具身智能数据工程方向

[![portfolio](https://img.shields.io/badge/portfolio-mahonghao1.github.io-1677ff.svg)](https://mahonghao1.github.io/) [![RoboData CI](https://github.com/MAHONGHAO1/Embodied-AI-Data-Processing-Platform/actions/workflows/tests.yml/badge.svg)](https://github.com/MAHONGHAO1/Embodied-AI-Data-Processing-Platform/actions/workflows/tests.yml) [![Fund CI](https://github.com/MAHONGHAO1/AI-Fund-Management-Platform/actions/workflows/tests.yml/badge.svg)](https://github.com/MAHONGHAO1/AI-Fund-Management-Platform/actions/workflows/tests.yml)

现在在擎仓机器人（Quic Robot）做具身数据算法工程师，管真机数采平台、数据质量与上传链路。

说白了就是采集员按下录制，到算法同学把包拉进训练脚本，中间这一段路归我。这段路最容易出事，也最少有人愿意写清楚：相机少一路、时间戳跳了几帧、某个关节值是 NaN、交付包换台机器就加载不了。任何一个都能让一次训练白跑，而人往往要等到 loss 炸了才知道。

所以我做的工具都有一个共同点——**它敢说「这个不能用」**。

- **主页**：[mahonghao1.github.io](https://mahonghao1.github.io/)
- **联系**：Mahonghao11@outlook.com

## 两个能跑起来的项目

### [RoboData Workbench](https://github.com/MAHONGHAO1/Embodied-AI-Data-Processing-Platform) · v0.9.0

把机器人演示数据做成可检查、可追溯、验过才交付的训练集。导入 → 清洗筛选 → 标注审核 → 质检 → LeRobot v3.0 转换 → 打包 → 独立验包，哪一步没过，批次就停在那儿。

- 质检做在行一级：时间戳跳变、缺帧、重复帧、异常轨迹、NaN，报告直接给帧号
- 交付前用官方 LeRobot 离线加载、过 DataLoader、算 SHA-256，被退一次的时间够自己验十次
- ALOHA Coffee Episode 0–4 端到端跑通：5,500 帧、四路 640×480、50 FPS；SO-100 子集 5 条 / 3,562 帧通过转换与交付验收
- 289 项 pytest、26 项前端单测与 Chromium 流程通过；[在线看四路相机同步时间轴](https://mahonghao1.github.io/robodata/)（免安装）

**边界**：验收范围限公开 ALOHA 样例与 SO-100 子集。四路同屏是布局验证，帧—时间映射一致不代表相机硬件同步；标注审核由脚本模拟，不代表人工审核，也不宣称训练效果。

### [AI 智选基金助手](https://github.com/MAHONGHAO1/AI-Fund-Management-Platform) · v0.4.0

同一条思路用在基金上：先说清每个数字从哪来，再谈收益。净值来源、取数日期、回退原因逐只摊开，数据撑不起区间就写「不可用」，不拿 0.00% 糊过去。

- 真实净值 / AkShare 回退 / 模拟净值 / 离线演示四条路径都留痕
- 34 项 pytest、5 项前端单测、1 项浏览器流程通过
- **边界**：持仓是虚构合成样例，不连真实账户、不下单、不构成投资建议

### [QuicStation 数据采集端](https://mahonghao1.github.io/#platforms) · v0.4.2

公司内部商用系统，真机数采工作站控制端：QRDF / LeRobot 双格式并行录制、三相机适配、上传与审核准入联动。经许可展示脱敏界面，代码与提交记录不公开。

## 做过什么

| 时间 | 公司 | 岗位 |
| --- | --- | --- |
| 2026.10 – 至今 | 擎仓机器人 Quic Robot | 具身数据算法工程师（算法研究员方向） |
| 2026.06 – 2026.10 | 光轮智能 Lightwheel | 数据交付工程师（实习） |
| 2026.01 – 2026.06 | 中国电信人工智能研究院 TeleAI | 具身智能数据工程（实习） |
| 2025.07 – 2026.01 | 商汤科技 SenseTime | 智能车舱数据工程（实习） |

## 手上有什么

- **数据工程**：多模态采集 / 清洗 / 质检 / 标注，LeRobot 与 HDF5 格式转换；真机数采平台与上传链路的部署、对账、算子开发
- **前端**：React、TypeScript、Vite、ECharts、Vitest、Playwright 多视口回归
- **后端与服务**：FastAPI、Uvicorn、REST API、本机单用户服务、`uv` 锁版依赖
- **工程**：Python、C/C++、ROS1/2、Linux、SQL
- **证据与交付**：IBM Carbon / Material / Ant 设计 token，CHANGELOG、Release Notes、CI、审计报告
- **AI 协作研发**：codex / claude code 工作流，独立完成大规模代码审查、测试与线上处置

## 荣誉与专利

中国国际「互联网+」国家级铜奖 · 全国无人系统应用大赛国家级三等奖 · 「西门子杯」省部级三等奖 · 知行杯省部级三等奖 · 实用新型专利《一种机器人快速升降定位装置》第一发明人

---

![GitHub stats](https://github-readme-stats.vercel.app/api?username=MAHONGHAO1&show_icons=true&hide_border=true&count_private=true)
