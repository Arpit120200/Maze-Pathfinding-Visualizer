# 🧭 Maze Pathfinding Visualizer

A Python-based GUI application that visualizes how different **graph search algorithms** explore a maze to find a path from a starting point to a treasure.

Built using **Python Turtle Graphics and Tkinter**, this project helps users understand algorithm behavior through **real-time visualization**.

---

# 🚀 Features

- **Interactive GUI**
  - Built using Python's `turtle` and `tkinter` modules
  - Simple and intuitive interface

- **Algorithm Visualization**
  - Watch algorithms explore the maze step-by-step in real time

- **Game & Explore Modes**
  - **Explore Mode** – Place treasure anywhere and watch the algorithm find it
  - **Game Mode** – See how the selected algorithm reaches the random treasure

- **Multiple Maze Layouts**
  - Choose from different maze structures using `.txt` files

---

# 🧠 Algorithms Implemented

The algorithms are implemented in `algorithms.py`.

## Depth First Search (DFS)

- Uses a **stack (LIFO)** data structure
- Explores as far as possible along a branch before backtracking
- Does not always guarantee the shortest path

**Strategy:** Go deep first, then backtrack

---

## Breadth First Search (BFS)

- Uses a **queue (FIFO)** data structure
- Explores all nodes at the current depth before moving deeper
- Guarantees the **shortest path in an unweighted graph**

**Strategy:** Explore layer by layer

---

## A* Search

- Uses a **heuristic-based search**
- Combines:
  - Actual cost from start `g(n)`
  - Estimated cost to goal `h(n)`
- Uses **Manhattan Distance** as the heuristic

Formula used:

```
f(n) = g(n) + h(n)
```

A* efficiently finds the **optimal path**.

---

# 🛠️ Installation

## Clone the Repository

```bash
git clone https://github.com/yourusername/maze-pathfinding-visualizer.git
cd maze-pathfinding-visualizer
```

## Python Requirements

Ensure you have **Python 3.8+** installed.

Check with:

```bash
python --version
```

This project only uses **built-in Python libraries**, so no additional installations are required.

---

# ⚙️ Configuration

To choose which maze to load, open:

```
config.py
```

Uncomment the maze file you want.

Example:

```python
MAZE_FILE = "gui_mazes/pacman_maze.txt"
```

---

# ▶️ Running the Application

## Explore Mode

Allows you to experiment with algorithms and visualize pathfinding.

```bash
python maze_gui_explore.py
```

---

## Game Mode

See the selected algorithm collect treasure.

```bash
python maze_gui_game.py
```

---

# 📁 Project Structure

```
maze-pathfinding-visualizer
├── algorithms.py
├── config.py
├── helper.py
├── maze_gui_explore.py
├── maze_gui_game.py
├── gui_mazes
└── README.md
```

---

# 🎯 Learning Outcomes

This project demonstrates:

- Graph traversal algorithms
- Heuristic search techniques
- Visualization of algorithm behavior
- Python GUI development
- Maze representation using text files
