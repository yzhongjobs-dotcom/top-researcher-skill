# 逆向分析计划

2026-10-28 与用户确认。目标：通过对顶会顶刊的逆向分析，完善、细化规则层，使 agent 读完本文件夹后能按顶级研究者的水平做科研。

## 分析方法：纵、横、序列三条线

- **纵向（重点）**：逐篇读透全文，理清逻辑链、承诺—兑现关系和关键决策点，按 [references/README.md](references/README.md) 的模板写入 `references/papers/`。
- **横向**：把同一个 section 放在一起比较，得出每个 section 写到什么程度才是顶会顶刊标准，写入 `references/sections/`；跨 section 的专题写入 `references/topics/`。为便于对齐，纵向画像从一开始就按 section 分栏。
- **序列**：同一课题组的论文按时间排列，看研究方向怎样逐篇推进，写入 `references/lineages/`。

论文类型只粗分**理论/方法型**和**应用/问题驱动型**，作为规律的适用条件标注；写论文时选定一种类型、一个目标期刊和 2–3 篇锚点论文，整篇按一套逻辑走。

## 样本（暂定）

选择优先级：高引论文（年均引用为准）→ Yanan Li、Chenguang Yang 课题组 → 与在研方向接近的近年强论文 → 对照样本。高引不等于适合所有类型：控制理论文化的高引论文（如 He 等 TSMC2016）按其类型条件学习。

**核心精读，约 24 篇**

| 来源 | 论文 |
|---|---|
| 课题组序列（Burdet / Yang / Li） | Ganesh ICRA2010*（需下载）→ Yang T-RO2011（R11）→ Li & Ge TCST2014 → Ge 等 IJC2014 → Li T-RO2015* → Li T-RO2018* → Yang TMECH2018（R01）→ Peng/Yang 等 NN 增强最优导纳（RL）* → Li NMI2019* → Xing T-RO2023（R12） |
| 高引经典 | Kang TMECH2009、Buerger & Hogan T-RO2007、Ficuciello T-RO2015、Kronander & Billard RA-L2016、Buchli RSS2010 / IJRR2011、Jung TCST2004、He 等 TSMC2016、Luo ICRA2019、Gribovskaya ICRA2011 |
| 近年强论文 | Jin TMECH2023、Li T-RO2025、Hammoud RA-L2021、Dyck RA-L2022、Haninger RAS2023、R13 T-RO2023、Xue IMA、Geiger T-RO2026、Reuss RSS2022 |
| 应用型序列（TUM 机器人超声）* | Virga IROS2016 → Jiang ICRA2021（Jiang RA-L2020、MedIA2023 综述未下载，缺失不影响开始） |

带 * 的已由用户下载到 [sources/pdfs/](sources/pdfs/)（2026-10-28，7 篇）。

**对照样本，约 4 篇**：同主题普通期刊或写法较弱的论文，如 Cao IEEE Access 2019（动态自适应混合阻抗）、R22 TSMC2017 等。

**留出检验集，约 8–10 篇（检验前不读、不交给 Codex）**：Roveda RA-L2016、Abu-Dakka RAS2018、Raiola RA-L2018、Li TIE2017、Fu TIM2024、Kronander T-RO2016、Pan 复合学习 VIC、Xue RAS2025、Anand RAS2023、Caldarelli RA-L2022。

各论文的本地路径见 [sources/index.json](sources/index.json)。

## 步骤与检查点

| 步骤 | 内容 | 检查点 |
|---|---|---|
| P0 | 建框架；迁入原项目的通用内容并去掉项目细节；样本清单 | **已完成框架与迁移**；样本清单待用户确认 |
| P1 | 试点：亲自完整分析 3 篇（理论型、应用型、序列论文各一） | 用户认可模板与深度后再批量 |
| P2 | 批量纵向分析：Codex 只读提取文本做第一遍（每批约 4 篇并行），Claude 对照 PDF 原页核对并补全决策点 | — |
| P3 | 横向与序列分析，写 sections/、topics/、lineages/ | — |
| P4 | 据此重写 workflow/ 与 README | 用户审阅 |
| P5 | 检验（见 [evals/](evals/README.md)），按差距回补 | 用户评判 |

## 分工

- **Codex**：第一遍单篇画像（必须给页码依据）；对综合出的规则做对抗式挑错。
- **Claude**：核对原文（进入最终文件的决策点全部对照 PDF 原页）；跨论文综合；检验。

## 待用户确认

1. 样本清单的增减。
2. 文件语言：现有规则层为中文；新的参考资料用中文还是英文。
3. 是否需要推送到一个新的私有 GitHub 仓库（目前只有本地 Git）。
4. 额度：P1 消耗小；24 篇全量分析消耗较大，Claude 与 Codex 两边额度都会用到。
