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
    iwildcam_accuracy = extract_first(r"最终测试准确率: [0-9.]+ \(([0-9.]+%)\)", iwildcam, "not recorded")

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
