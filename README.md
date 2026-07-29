# AI Course Projects

Assignments from the Artificial Intelligence course at the University of Tehran — covering classic search algorithms, genetic algorithms, machine learning from scratch, deep learning with PyTorch, and NLP.

## Overview

| # | Project | Topic | Stack |
|---|---------|-------|-------|
| 1 | [project-1](project-1) | Pacman AI: uninformed & informed search (BFS, DFS, IDS, A\*, Weighted A\*) | Python, Pygame |
| 2 | [project-2](project-2) | Genetic algorithm applied to a game-playing agent | Python, Jupyter |
| 3 | [project-3](project-3) | Machine learning: Decision Tree from scratch vs. library implementation, classification/regression | Python, Jupyter, scikit-learn |
| 4 | [project-4](project-4) | Introduction to PyTorch and a text classification task | Python, PyTorch, Jupyter |
| 5 | [project-5](project-5) | NLP preprocessing and feature extraction on review data | Python, Jupyter |

## Project 1 — Pacman Search Algorithms

A Pacman-style game where an AI agent finds its way through the maze using classic search algorithms.

- `main.py`, `menu.py`, `config.py`, `tester.py` — entry points and game setup
- `entities/` — player, ghost, fruit, and wall game objects
- `core/environment/` — the game engine used by the AI mode (map loading, game state)
- `core/solvers/` — the search algorithms: BFS, DFS, IDS, A\*, and Weighted A\*, plus heuristics
- `maps/` — text-based maze layouts used by the solvers
- `assignment.pdf` — the original assignment description
- `report.docx` — project report (in Persian)

> Note: game assets (sprites, menu background, music) are not included in this repo to keep it lightweight — only the source code, maps, and documents are tracked.

## Project 2 — Genetic Algorithm

A genetic algorithm applied to a game-playing task, evolving a population of candidate solutions across generations.

- `CA2.ipynb` — full implementation and experiments
- `assignment.pdf` — the original assignment description

## Project 3 — Machine Learning

Implementing a Decision Tree classifier from scratch and comparing it against a standard library implementation, plus additional classification/regression experiments.

- `CA3.ipynb` — full implementation and experiments
- `assignment.pdf` — the original assignment description

> Note: the datasets used in this notebook are not included in this repo — only the code and assignment description are tracked.

## Project 4 — Introduction to PyTorch

A hands-on introduction to PyTorch fundamentals, followed by a text classification task built on top of it.

- `Introduction_to_PyTorch.ipynb` — full implementation and experiments
- `assignment.pdf` — the original assignment description

> Note: the training/test datasets used in this notebook are not included in this repo — only the code and assignment description are tracked.

## Project 5 — NLP Preprocessing & Feature Extraction

Text preprocessing and feature extraction techniques applied to review data, comparing different preprocessing pipelines.

- `ca5.ipynb` — full implementation and experiments

> Note: the review dataset used in this notebook is not included in this repo — only the code is tracked.

## Author

Fatima Borhani — Computer Engineering student, University of Tehran
# ai-course-projects
AI course assignments: search algorithms, genetic algorithms, machine learning, and NLP (University of Tehran)
