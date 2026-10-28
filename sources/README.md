# 样本来源

- `pdfs/`：用户新下载的论文（本地已有的不复制，只在索引中记路径）。
- `index.json`：所有候选论文的去重清单（按 SHA-256），含文件名、所有本地路径和检索时的引用数（如有记录）。由 `build_index.py` 生成，重新运行即可更新。

扫描的文件夹：

1. `D:\桌面\正文writing skill\文献资料`（R01–R22）
2. `D:\桌面\科研Agent Harness设计\impedance-control-e2e\source-materials`（含 user-batch-v2）
3. `E:\github_project\scan-impedance-update\literature`（原项目文献库）
4. 本目录的 `pdfs/`

引用数来自 `impedance-control-e2e/FULLTEXT_DOWNLOAD_BATCH_V2.md`（Google Scholar 检索时记录），只覆盖其中 64 篇；比较时按年均引用看。

几处文件名不直观：Geiger T-RO2026 = `E17.pdf`；Li T-RO2025 = `E27.pdf`；Anand RAS2023 = `imoj6X2imAgJ.pdf`；Peng/Yang TNNLS2022 = `G15.pdf`（`pdfs/` 另有一份）；Dyck RA-L2022 = `Impedance_Control_on_Arbitrary_Surfaces…`（另有 `RA-L-2022-3184800.pdf`）。

`index.json` 的引用匹配有误：Buchli IJRR2011（`Learning Variable Impedance Control.pdf`）被标成 258 次、2020 年，那是 Roveda JIRS2020 的记录。
