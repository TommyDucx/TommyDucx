# GitHub Profile README Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a bilingual GitHub Profile README for `TommyDucx/TommyDucx` and a safe local workflow for refreshing its research-results section from `MLForTommy`.

**Architecture:** `README.md` is the hand-authored GitHub Profile README and contains stable markers around the generated research-results block. `scripts/update_research_results.py` reads selected local `MLForTommy` files, rewrites only the marked block, and leaves review/commit/push decisions to the user.

**Tech Stack:** Markdown, Python 3 standard library, Git.

---

## File Structure

- Create `README.md`: bilingual GitHub Profile README displayed by a repository named `TommyDucx`.
- Create `scripts/update_research_results.py`: deterministic local updater for the bounded research-results block.
- Keep existing `index.html` and `style.css` unchanged.

## Implementation Tasks

### Task 1: Create GitHub Profile README

**Files:**
- Create: `README.md`

- [ ] **Step 1: Write a failing README presence/content check**

Run:

```bash
test -f README.md && rg -n "TommyDucx|Chengxuan Du|杜承轩|MLForTommy|content_24272757|RESEARCH-RESULTS:START|RESEARCH-RESULTS:END" README.md
```

Expected: command fails because `README.md` does not exist yet.

- [ ] **Step 2: Create `README.md`**

Create `README.md` with this exact content:

```markdown
<div align="center">

# Hi, I'm Chengxuan Du / 杜承轩

**High school student exploring AI, machine learning, federated learning, robotics, and interdisciplinary research.**  
**一名关注 AI、机器学习、联邦学习、机器人与跨学科研究的高中生。**

Learning by building. Building to explain.  
在动手实践中学习，也用项目把抽象原理讲清楚。

[![GitHub](https://img.shields.io/badge/GitHub-TommyDucx-181717?style=flat-square&logo=github)](https://github.com/TommyDucx)
![Python](https://img.shields.io/badge/Python-learning%20%26%20building-3776AB?style=flat-square&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-experiments-0E7490?style=flat-square)
![Federated Learning](https://img.shields.io/badge/Federated%20Learning-simulation-047857?style=flat-square)
![Robotics](https://img.shields.io/badge/Robotics-innovation-2563EB?style=flat-square)

</div>

---

## About Me / 关于我

I am a high school student and interdisciplinary explorer. My path started with robotics and invention projects, and it is now expanding toward AI, machine learning, federated learning, and education-friendly research tools.

我是一名高中生，也是一名跨学科探索者。我的探索从机器人和创新发明开始，现在逐步延伸到 AI、机器学习、联邦学习，以及面向学习和讲解的研究工具。

- I care about making complex ideas understandable through code, diagrams, experiments, and reports.
- 我关注如何用代码、图表、实验和报告，把复杂概念解释得更清楚。
- I prefer honest experiments over polished claims: small datasets, unstable results, and limitations are all part of learning.
- 我更重视真实的实验过程，而不是包装过度的结论：小数据集、波动结果和局限性本身也是学习的一部分。

---

## Featured Research Project / 研究项目

### MLForTommy: Machine Learning + Federated Learning Simulation Framework

`MLForTommy` is a beginner-friendly machine learning and federated learning simulation framework. It is designed for high school classroom-style explanation: the goal is to understand principles, not to chase industrial-level accuracy.

`MLForTommy` 是一个面向零基础学习者的机器学习 + 联邦学习仿真框架。它适合高中课堂式演示，核心目标是“看懂原理”，而不是追求工业级精度。

**What it includes / 项目内容：**

- Modular framework: datasets, models, trainers, analysis tools, and visualization.
- 模块化框架：数据集、模型、训练器、分析工具和可视化。
- Experiments for Iris, MNIST, iWildCam, and breast cancer classification.
- 包含 Iris、MNIST、iWildCam、乳腺癌分类等实验脚本。
- Automatic outputs: CSV data, loss curves, accuracy curves, comparison charts, experiment reports, and principle summaries.
- 自动生成 CSV 数据、损失曲线、准确率曲线、对比图、实验报告和原理总结。

<!-- RESEARCH-RESULTS:START -->
**Current experiment highlights / 当前实验摘要：**

- Single-machine vs federated learning comparison:
  - Single-machine accuracy: `92.12%`
  - Federated learning accuracy: `88.58%`
  - Single-machine final loss: `0.2866`
  - Federated learning final loss: `0.4895`
- iWildCam federated simulation:
  - 5 clients, 20 federated rounds
  - Local image classification setup
  - Final test accuracy in the small-data simulation: `50.00%`

These results are treated as learning records. Lower or fluctuating federated accuracy is useful here because it makes the trade-offs of distributed learning visible.

这些结果会被当作学习记录来看待。联邦学习在小数据仿真中准确率较低或波动明显，反而能帮助观察分布式学习的限制和取舍。
<!-- RESEARCH-RESULTS:END -->

> Repository link will be added here after `MLForTommy` is published on GitHub.  
> `MLForTommy` 发布到 GitHub 后，这里会补充仓库链接。

---

## Recognition / 成就与认可

According to a Shenzhen News article from 创新南山, I was recognized as Guangdong Province "Innovation Good Youngster" and had earlier been recognized in 2019 as "深圳市南山区少年创新院小院士" and "中国少年科学院小院士".

据深圳新闻网转载创新南山报道，我曾获评广东省“创新好少年”，并于 2019 年先后获评“深圳市南山区少年创新院小院士”和“中国少年科学院小院士”。

Publicly reported highlights / 公开报道中的经历：

- 2 national championships in World Robot Contest education-ministry competition projects.
- 2 次“世界机器人大赛全国冠军（教育部竞赛项目）”。
- 2 championships in Guangdong Youth Robot Design Contest.
- 2 次“广东省青少年机器人设计大赛冠军”。
- 1 third place in World Robot Contest Youth Design Contest Shenzhen station.
- 1 次“世界机器人大赛青少年设计大赛（深圳站）季军”。
- Invented an intelligent backpack for improving load balance, with one utility model patent.
- 发明改善背负平衡的智能背包，并获得一项实用新型专利。

Source / 来源：[深圳新闻网：两名南山学子上榜广东省“最美南粤少年”](https://www.sznews.com/news/content/2021-06/04/content_24272757.htm)

---

## Tech Stack / 技术方向

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-0E7490?style=flat-square)
![Federated Learning](https://img.shields.io/badge/Federated%20Learning-047857?style=flat-square)
![Data Visualization](https://img.shields.io/badge/Data%20Visualization-2563EB?style=flat-square)
![Robotics](https://img.shields.io/badge/Robotics-1D4ED8?style=flat-square)

---

## GitHub Stats / GitHub 数据

<div align="center">

![TommyDucx's GitHub stats](https://github-readme-stats.vercel.app/api?username=TommyDucx&show_icons=true&theme=transparent&hide_border=true)

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=TommyDucx&layout=compact&theme=transparent&hide_border=true)

</div>

---

## Learning Direction / 正在探索

- AI and machine learning fundamentals / AI 与机器学习基础
- Federated learning and privacy-preserving computation / 联邦学习与隐私保护计算
- Robotics and intelligent systems / 机器人与智能系统
- Interdisciplinary research and science communication / 跨学科研究与科学表达
- Education-friendly tools for explaining abstract concepts / 面向学习和讲解的工具

---

## Links / 链接

- GitHub: [TommyDucx](https://github.com/TommyDucx)
- Personal site source in this workspace: [`index.html`](./index.html)
- Verified recognition source: [Shenzhen News / 创新南山](https://www.sznews.com/news/content/2021-06/04/content_24272757.htm)

---

<div align="center">

**Build small experiments. Ask better questions. Explain what I learn.**  
**做小实验，提出更好的问题，把学到的东西讲清楚。**

</div>
```

- [ ] **Step 3: Run README content check**

Run:

```bash
test -f README.md && rg -n "TommyDucx|Chengxuan Du|杜承轩|MLForTommy|content_24272757|RESEARCH-RESULTS:START|RESEARCH-RESULTS:END" README.md
```

Expected: output includes all required strings and command exits with status `0`.

- [ ] **Step 4: Commit README**

Run:

```bash
git add README.md
git commit -m "Add GitHub profile README"
```

Expected: commit succeeds.

### Task 2: Add Safe Research Results Updater

**Files:**
- Create: `scripts/update_research_results.py`

- [ ] **Step 1: Write a failing script presence check**

Run:

```bash
test -f scripts/update_research_results.py && python3 scripts/update_research_results.py --help
```

Expected: command fails because the script does not exist yet.

- [ ] **Step 2: Create updater script**

Create `scripts/update_research_results.py` with this exact content:

```python
#!/usr/bin/env python3
"""Refresh the bounded MLForTommy research section in the profile README.

The script is intentionally conservative: it rewrites only the text between
RESEARCH-RESULTS markers and never commits or pushes changes.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


START = "<!-- RESEARCH-RESULTS:START -->"
END = "<!-- RESEARCH-RESULTS:END -->"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_first(pattern: str, text: str, fallback: str) -> str:
    match = re.search(pattern, text)
    return match.group(1).strip() if match else fallback


def build_research_block(ml_dir: Path) -> str:
    comparison = read_text(ml_dir / "outputs" / "result_comparison_report.txt")
    iwildcam = read_text(ml_dir / "outputs" / "iwildcam_federated_report.txt")

    single_accuracy = extract_first(r"单机机器学习准确率：([0-9.]+%)", comparison, "not recorded")
    federated_accuracy = extract_first(r"联邦学习准确率：([0-9.]+%)", comparison, "not recorded")
    single_loss = extract_first(r"单机机器学习最终损失：([0-9.]+)", comparison, "not recorded")
    federated_loss = extract_first(r"联邦学习最终损失：([0-9.]+)", comparison, "not recorded")
    clients = extract_first(r"客户端数: ([0-9]+)", iwildcam, "not recorded")
    rounds = extract_first(r"联邦轮数: ([0-9]+)", iwildcam, "not recorded")
    iwildcam_accuracy = extract_first(r"最终测试准确率: [0-9.]+ \\(([0-9.]+%)\\)", iwildcam, "not recorded")

    return f"""{START}
**Current experiment highlights / 当前实验摘要：**

- Single-machine vs federated learning comparison:
  - Single-machine accuracy: `{single_accuracy}`
  - Federated learning accuracy: `{federated_accuracy}`
  - Single-machine final loss: `{single_loss}`
  - Federated learning final loss: `{federated_loss}`
- iWildCam federated simulation:
  - {clients} clients, {rounds} federated rounds
  - Local image classification setup
  - Final test accuracy in the small-data simulation: `{iwildcam_accuracy}`

These results are treated as learning records. Lower or fluctuating federated accuracy is useful here because it makes the trade-offs of distributed learning visible.

这些结果会被当作学习记录来看待。联邦学习在小数据仿真中准确率较低或波动明显，反而能帮助观察分布式学习的限制和取舍。
{END}"""


def replace_block(readme_text: str, new_block: str) -> str:
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    updated, count = pattern.subn(new_block, readme_text)
    if count != 1:
        raise ValueError("README.md must contain exactly one research-results block")
    return updated


def main() -> int:
    parser = argparse.ArgumentParser(description="Refresh MLForTommy research results in README.md")
    parser.add_argument("--readme", type=Path, default=Path("README.md"), help="Profile README path")
    parser.add_argument(
        "--ml-dir",
        type=Path,
        default=Path("/Users/tommydu/Desktop/MLForTommy"),
        help="Local MLForTommy project directory",
    )
    parser.add_argument("--check", action="store_true", help="Exit non-zero if README.md would change")
    args = parser.parse_args()

    readme_text = read_text(args.readme)
    new_block = build_research_block(args.ml_dir)
    updated = replace_block(readme_text, new_block)

    if args.check:
        if updated != readme_text:
            print("README.md research results are out of date")
            return 1
        print("README.md research results are up to date")
        return 0

    if updated == readme_text:
        print("README.md research results are already up to date")
        return 0

    args.readme.write_text(updated, encoding="utf-8")
    print("Updated README.md research results. Review git diff before committing or pushing.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 3: Run script help**

Run:

```bash
python3 scripts/update_research_results.py --help
```

Expected: output includes `Refresh MLForTommy research results in README.md`.

- [ ] **Step 4: Run updater in check mode**

Run:

```bash
python3 scripts/update_research_results.py --check
```

Expected: output is `README.md research results are up to date` and exit status is `0`.

- [ ] **Step 5: Commit updater script**

Run:

```bash
git add scripts/update_research_results.py
git commit -m "Add research results README updater"
```

Expected: commit succeeds.

### Task 3: Verify Profile README Deliverable

**Files:**
- Verify: `README.md`
- Verify: `scripts/update_research_results.py`

- [ ] **Step 1: Verify no unresolved marker words**

Run:

```bash
grep -RIn 'T[B]D\|TO[D]O\|FIX[M]E' README.md scripts/update_research_results.py docs/superpowers/specs docs/superpowers/plans
```

Expected: no output and exit status `1`.

- [ ] **Step 2: Verify no fake email or fake repository link**

Run:

```bash
rg -n 'hello@example.com|github.com/.*/MLForTommy' README.md
```

Expected: no output and exit status `1`.

- [ ] **Step 3: Verify required README content**

Run:

```bash
rg -n 'TommyDucx|Chengxuan Du|杜承轩|MLForTommy|广东省“创新好少年”|content_24272757|github-readme-stats|RESEARCH-RESULTS:START|RESEARCH-RESULTS:END' README.md
```

Expected: output includes all searched topics and command exits with status `0`.

- [ ] **Step 4: Verify updater remains idempotent**

Run:

```bash
python3 scripts/update_research_results.py --check
```

Expected: output is `README.md research results are up to date` and exit status is `0`.

- [ ] **Step 5: Inspect git status**

Run:

```bash
git status --short
```

Expected: no output.

## Final Delivery

Report:

- Created `README.md` for the `TommyDucx/TommyDucx` profile repository.
- Created `scripts/update_research_results.py` for safe local updates from `/Users/tommydu/Desktop/MLForTommy`.
- Mention that the README must be pushed to a GitHub repository named exactly `TommyDucx` to appear on `https://github.com/TommyDucx`.
- Mention that the updater never commits or pushes automatically; it only rewrites the bounded research-results block and asks the user to review the diff.
