# 麻洪豪 Mahonghao

> 具身智能数据工程方向 · 2027 届 · 上海应用技术大学 机器人工程

[![portfolio](https://img.shields.io/badge/portfolio-mahonghao1.github.io-1677ff.svg)](https://mahonghao1.github.io/) [![RoboData CI](https://github.com/MAHONGHAO1/Embodied-AI-Data-Processing-Platform/actions/workflows/tests.yml/badge.svg)](https://github.com/MAHONGHAO1/Embodied-AI-Data-Processing-Platform/actions/workflows/tests.yml) [![Fund CI](https://github.com/MAHONGHAO1/AI-Fund-Management-Platform/actions/workflows/tests.yml/badge.svg)](https://github.com/MAHONGHAO1/AI-Fund-Management-Platform/actions/workflows/tests.yml)

- **现在**：擎仓机器人（Quic Robot）— 具身数据算法工程师，做真机数采平台、数据质量与上传链路
- **方向**：把机器人演示数据变成可检查、可追溯、可验证后交付的训练样本
- **主页**：[mahonghao1.github.io](https://mahonghao1.github.io/) · **联系**：Mahonghao11@outlook.com

## 当前作品

| 项目 | 版本与技术栈 | 一句话 | 在线展示 |
| --- | --- | --- | --- |
| [RoboData Workbench](https://github.com/MAHONGHAO1/Embodied-AI-Data-Processing-Platform) | v0.8.0 · React + TypeScript / FastAPI / Python | 具身数据的可追溯质检、LeRobot v3.0 转换与独立交付验包 | [项目深度页](https://mahonghao1.github.io/robodata/) |
| [AI 智选基金助手](https://github.com/MAHONGHAO1/AI-Fund-Management-Platform) | v0.3.0 · React + TypeScript / FastAPI / Python | 数据可追溯的本地组合分析工作台，明确区分有效值与不可用状态 | [作品集首页](https://mahonghao1.github.io/) |
| [数据采集端 QuicStation](https://mahonghao1.github.io/#platforms) | v0.4.2 · 公司内部系统 | 真机数采工作站控制端：QRDF / LeRobot 双格式并行录制、三相机适配、上传与审核准入联动 | [界面展示](https://mahonghao1.github.io/#platforms) · 代码不公开 |

**共同主线**：数据来源可追溯 · 指标口径明确 · 不可用状态显式标注 · 能力边界写进界面和文档。前两个项目为**本机单用户**运行，展示页是静态截图与验收证据，不提供公网交互实例；基金项目的持仓是虚构合成样例，不连接真实账户、不执行交易、不提供投资建议。第三个为公司内部商用系统，经许可展示脱敏界面，代码与提交记录不公开。

### RoboData Workbench

- 接入 → 清洗筛选 → 标注审核 → 质检 → 转换 → 打包交付，人工与自动节点混合编排；未通过质检的批次强制拦截
- 质检规则内建：时间戳、缺帧重复、异常轨迹、NaN 行级定位；交付包经官方 LeRobot 离线加载、DataLoader 复核与 SHA-256 防篡改
- **验收范围**：固定 ALOHA Coffee 公开样例与 SO-100 子集的限定范围验证。逐路文件时间映射检查**不代表相机硬件同步**；四相机同屏是 16:9 布局验证，批次元数据为演示构造
- **测试口径**：本仓库 Python 246 项 pytest 通过，前端 Vitest 与 Playwright 多视口回归，CI 见上方 badge。工作中另有擎仓内部回归 678 项（采集端与平台），不在本仓库范围，两项不叠加计算

### AI 智选基金助手

- 多源净值获取与自动重试、跨源切换、模拟数据兜底；逐只基金标注净值来源、日期与回退状态
- 收益与风险指标明确区分有效值和不可用状态，不以 0.00% 替代空值；组合、净值序列与证据链在同一工作台核对
- 当前 v0.3.0 为 React + TypeScript 的 16:9 固定工作台，旧版 Streamlit 入口保留作迭代对照
- **数据边界**：虚构合成组合、离线演示、不含真实账户或投资建议

## 实习经历

| 时间 | 公司 | 岗位 |
| --- | --- | --- |
| 2026.10 – 至今 | 擎仓机器人(Quic Robot) | 具身数据算法工程师(算法研究员方向) |
| 2026.06 – 2026.10 | 光轮智能(Lightwheel) | 数据交付工程师实习生 |
| 2026.01 – 2026.06 | 中国电信人工智能研究院(Tele ai) | 具身智能数据工程实习生 |
| 2025.07 – 2026.01 | 商汤科技(Sensetime) | 智能车舱数据工程实习生 |

## 技能

- **数据工程**：多模态数据采集 / 清洗 / 质检 / 标注，LeRobot / HDF5 格式转换；真机数采平台与上传链路的部署、对账与算子开发
- **前端**：React、TypeScript、Vite、ECharts、Vitest、Playwright 多视口回归
- **后端与服务**：FastAPI、Uvicorn、REST API、本机单用户服务、`uv` 锁版依赖
- **工程开发**：Python、C/C++、ROS1/2、Linux、SQL
- **设计与证据**：IBM Carbon / Material / Ant 设计 token、数据边界声明、CHANGELOG / Release Notes / CI
- **AI 协作研发**：codex / claude code 等 AI 编码工作流，独立完成大规模代码审查、测试与线上处置

## 荣誉与专利

中国国际"互联网+"国家级铜奖 · 全国无人系统应用大赛国家级三等奖 · "西门子杯"省部级三等奖 · 知行杯省部级三等奖 · 实用新型专利《一种机器人快速升降定位装置》第一发明人

---

![GitHub stats](https://github-readme-stats.vercel.app/api?username=MAHONGHAO1&show_icons=true&hide_border=true&count_private=true)
