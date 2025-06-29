# Monte Carlo Pi Approximation

This is a small project created to practice working with the `matplotlib` library, particularly focusing on animations and basic data visualization.

## Purpose

The main goals of this project are:
- To visualize the Monte Carlo method for approximating π (pi)
- To gain hands-on experience with `matplotlib`, especially with `animation.FuncAnimation`
- To demonstrate a simple probabilistic approach to estimating π

## How It Works

1. The program randomly generates points within a square from `[-1, 1] x [-1, 1]`
2. It checks whether each point falls inside the unit circle
3. The approximation of π is calculated using the formula:

   π ≈ 4 × (points inside circle / total points)

4. Points inside the circle are shown in green, those outside in red
5. The live π approximation is updated and displayed in the plot title

## Requirements

- Python 3.x
- `matplotlib` library


Install project dependencies using the `requirements.txt` file:

```bash
  pip install -r requirements.txt
````

## Running the Project
Simply run:
```bash
  python monte_carlo_pi.py
```
An animated window will open, showing the approximation improving in real time.

## License
This project is licensed under the MIT License
