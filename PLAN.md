# 逆向分析计划

2026-10-28 与用户确认。

## 目标

**最终目标：** agent 读完本文件夹后，和用户一起做科研时，能像顶会顶刊作者一样思考、判断和处理问题。研究现状怎么看，问题怎么定，方法怎样从问题中自然长出来并准确解决它，实验怎样设计，贡献怎样定位，都要达到顶刊水平。

**本轮任务：** 科研流程（[README](README.md) 与 [workflow/](workflow/)）已与用户讨论形成，基本正确，是规则层。它的不足在于来自个人理解，缺少真实顶刊的支撑。本轮逆向分析真实顶会顶刊，作为参考层，逐个阶段深化和校正规则层，让 agent 真正知道三件事：

- 顶刊在每一步实际做到什么程度；
- 作者是怎样做出这些决定的；
- 普通论文差在哪里。

有了这些，agent 才能按真实顶刊标准去做研究，也能用这个标准判断和改进 idea。写作另有 skill，不在这里；这里只涉及属于科研判断的贡献定位与论证。

## 结构：怎样做成可复用的 skill

参照 skill 的渐进披露：

| 层 | 文件 | 作用 |
|---|---|---|
| 入口 | `README.md` | 目标、阶段表、总原则；每次都读 |
| 规则层 | `workflow/01–05` | 每个阶段怎么判断、怎么做；进入该阶段时读 |
| 参考层 | `references/stages/01–05` | 与规则层一一对应：顶刊在这一阶段实际怎么做、变化范围多大、作者怎样决定、普通论文差在哪里，并附锚点论文；规则层在需要处链接过来 |
| 素材 | `references/papers/`、`references/comparisons/` | 单篇画像与两两对比，参考层每条结论的出处 |

**用于新 idea 时：** agent 在当前阶段读规则和对应的 `stages/` 文件，按 idea 的类型和目标期刊选 2–3 篇锚点论文，把自己的研究现状、问题、方法、实验逐项与锚点对照，找出差距，并参照顶刊通常的补足方式改进。论文类型只粗分**理论/方法型**和**应用/问题驱动型**，作为适用条件；同一篇工作只按一套类型标准走，避免四不像。

**扩展到新领域时：** 补该领域的单篇画像和对比，更新 `stages/` 中的范围和锚点。规则层只在证据推翻或补充它时修改。

## 起点：已有材料

以下作为素材吸收，不作为框架：

| 材料 | 怎样用 |
|---|---|
| [README](README.md) §一–§四（十月的判断准则、方法实际尺度、实验约定） | 这就是规则层本身，是逆向分析要验证和细化的对象 |
| [2026-10-18 可执行的顶刊标准](references/prior_standards/2026-10-18_executable_top_journal_standard.md) | 比 README 更具体的六条标准，压缩时丢掉的细节在这里 |
| [2026-09-07 方法标尺 v1.1](references/prior_standards/2026-09-07_method_reference_distribution_v1_1.txt) | 吸收其中的认识：11 篇方法画像（需对照原文复核）、同一研究线前后版本的对比、作者自称贡献与实际增量的区分、复杂度应与问题匹配。其中的评审装置（期刊画像、强制对照协议、否决条件）不照搬 |
| [examples/](references/examples/README.md) | 首轮 R 系列分析、36 篇实验设置分析 |

## 分析方法

### 单篇画像（纵向，重点）

每篇读透全文，按阶段记录，写入 `references/papers/`，模板见 [references/README.md](references/README.md)：

- 全文逻辑链；
- 研究现状、研究问题、方法、实验验证、贡献定位；
- 关键决策点：当时有哪些选项、选了什么、放弃了什么、理由（[原文] 或 [推断]）、对后文的影响；
- 对规则层的支持、修正或反例。

### 按阶段横向比较

把多篇论文在同一阶段的做法放在一起比较：共性是什么，随论文类型和期刊怎样变化，好论文和普通论文差在哪里。写入 `references/stages/`。

### 两两对比

看"差多少才到顶刊"，以及作者升级论文时补了什么。写入 `references/comparisons/`。对比有三类：

- 同一研究线的前后版本：Jin ICRA2022 → Jin TMECH2023；Fu TIM2024 → Fu T-RO2025；Beber ICRA2024 与 Fu T-RO2025；课题组序列；
- 顶刊与强但非顶刊；
- 同一期刊中形态不同的论文，如 Pollayil 与 Wijayarathne。

## 样本

选择优先级（用户定）：高引论文（按年均引用）→ Yanan Li、Chenguang Yang 课题组 → 近年强论文 → 对照样本。

- 当下的顶刊水平主要以近几年的 T-RO / IJRR / RSS / ICRA 校准；老的高引论文体现长期价值，作为补充参照。
- 控制理论文化的高引论文（如 He 等 TSMC2016）按其类型条件学习。

**核心精读**（不要求读完，标准稳定即停；P2 先做成对论文和近年顶刊）

| 来源 | 论文 |
|---|---|
| 近年顶刊 | Wijayarathne T-RO2023、Pollayil T-RO2023、Li T-RO2025、Fu T-RO2025、Xue IJRR（IMA）、R13 T-RO2023、Geiger T-RO2026、Jin ICRA2022、Beber ICRA2024、Reuss RSS2022 |
| 课题组序列（Burdet / Yang / Li） | Ganesh ICRA2010 → Yang T-RO2011（R11）→ Li & Ge TCST2014 → Ge 等 IJC2014 → Li T-RO2015 → Yang TMECH2018（R01）→ Li T-RO2018 → Li NMI2019 → Peng/Yang 等 TNNLS2022 → Xing T-RO2023（R12） |
| 高引经典 | Kang TMECH2009、Kronander & Billard RA-L2016、Buchli RSS2010 / IJRR2011、Jung TCST2004、He 等 TSMC2016、Luo ICRA2019、Gribovskaya ICRA2011 |
| 其他近年强论文 | Jin TMECH2023、Hammoud RA-L2021、Dyck RA-L2022、Haninger RAS2023 |
| 应用型序列（TUM 机器人超声） | Virga IROS2016 → Jiang RA-L2020 → Jiang ICRA2021；Jiang MedIA2023 综述作为背景 |

本地没有、需要用户下载的：UFIC IJRR2024、Lachner IJRR、Piedra IJRR2026、Angelini IROS2019、Ficuciello T-RO2015、Buerger & Hogan T-RO2007。没有下载就不读，不影响开始。各论文的路径见 [sources/](sources/README.md)。

**对照样本（强但非顶刊，或写法较弱）**：Cao IEEE Access 2019、R22 TSMC2017、Fu TIM2024、Xue RAS2025。

**留出检验集（检验前不读、不交给 Codex）**：

- 顶刊：Kronander T-RO2016；
- 强但非顶刊：Roveda RA-L2016、Abu-Dakka RAS2018、Li TIE2017、Pan 复合学习 VIC、Anand RAS2023、Caldarelli RA-L2022。

已在本文件夹中分析过的论文，不能作为留出论文。

## 步骤与检查点

每完成一个检查点，先更新本表的"状态"列。

| 步骤 | 内容 | 检查点 | 状态 |
|---|---|---|---|
| P0 | 建框架、迁入通用内容、确定样本、恢复已有标准 | — | 已完成（2026-10-28） |
| P1 | 试点：R13 T-RO2023（理论/方法型）、Dyck RA-L2022（应用/问题驱动型）两篇单篇画像，加上 Jin ICRA2022 → TMECH2023 一组对比；据此写出 `stages/` 中两个阶段（如 02 问题、03 方法）的初稿片段，并示范对应的 workflow 文件会怎样细化 | 交用户审阅；**用户认可后再进入 P2** | 未开始 |
| P2 | 批量单篇画像与两两对比：Codex 读按页标注的提取文本（放在 `sources/text/`，不纳入 Git）做第一遍，Claude 对照 PDF 原页核对 | 开始前向用户说明预计额度 | — |
| P3 | 汇总成 `stages/01–05`，标出各类型的锚点论文 | 用户审阅 | — |
| P4 | 按 `stages/` 细化 workflow/ 各阶段：补上具体做法和判断，链接到参考层 | 修改前给用户看 | — |
| P5 | 轻量检验：一篇留出论文加一个真实 idea（见 [evals/](evals/README.md)），按差距回补 | 用户评判 | — |
| P6 | 打包为可安装的 skill：入口改为带 frontmatter 的 `SKILL.md`，只含 README、workflow、references；`sources/`、`evals/`、PLAN 不随 skill 分发 | 用户决定 | — |

**停止条件**：新读的论文已不再改变 `stages/` 的结论（连续几篇只增加实例），而不是读满固定篇数。

## 分工

- **Codex**：第一遍单篇画像（必须给页码依据）；对参考层和规则层做对抗式挑错。
- **Claude**：核对原文（进入最终文件的判断全部对照 PDF 原页）；按阶段综合、两两对比；检验。

## 形成过程的推断依据

成稿不能反映真实的发现顺序。分析决策点时，尽量补充成稿以外的材料：同组前后论文、作者博士论文、arXiv 版本差异、公开审稿意见与 rebuttal（OpenReview 等）、代码仓库。网页阅读可以直接进行；下载文件需要用户同意。

## 已定事项

- 新参考资料用中文（与规则层一致），用户另有要求时再改。
- 目前只用本地 Git；是否推送到私有 GitHub 仓库由用户决定。
- 额度：P1 消耗小；P2 批量阶段开始前先向用户说明预计消耗。
