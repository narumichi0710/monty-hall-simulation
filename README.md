# Monty Hall Simulation

Python Journal Project - モンテホール問題のシミュレーション

## 概要

確率論における有名な「モンテホール問題」をPythonでシミュレートし、「選択を変更する戦略」と「選択を変更しない戦略」のどちらが数学的に有利かを統計的に検証するプログラムです。

## プロジェクト構成

```
monty-hall-simulation/
├── README.md                 # プロジェクト概要
├── journal/
│   ├── part1_problem.md      # PART 1: 問題定義
│   ├── part2_examples.md     # PART 2: 具体例
│   ├── part3_pseudocode.md   # PART 3: 疑似コード
│   ├── part4_testing.md      # PART 4: テスト記録
│   └── part5_comments.md     # PART 5: コメント説明
├── src/
│   ├── main.py               # メインプログラム
│   ├── game.py               # Gameクラス
│   └── door.py               # Doorクラス
└── log.txt                   # シミュレーション結果ログ
```

## モンテホール問題とは

1. 3つのドアがあり、1つに賞品、2つにハズレ（ヤギ）がある
2. プレイヤーが1つのドアを選ぶ
3. 司会者（モンティ）がハズレのドアを1つ開ける
4. プレイヤーは選択を変更するか、そのままにするかを決める
5. 最終的に選んだドアを開け、賞品があれば勝ち

**直感に反する結果**: 選択を変更した方が勝率が高い（約66.7% vs 約33.3%）

## 実行方法

```bash
cd src
python main.py
```

## 開発プロセス

このプロジェクトはPython Journal Templateに沿って開発されています。
各PARTの詳細は`journal/`ディレクトリを参照してください。
