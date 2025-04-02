# Neighborhood and Proximity of Expectations Model

## Author
**Rodrigo Hernández Cervantes**  
📧 rohrc14@gmail.com  
🔗 [X Profile](https://x.com/rodroshc)

## Overview
This project implements a **Neighborhood and Proximity of Expectations Model**, simulating how agents' expectations evolve over time based on interactions with their neighbors. The model employs a **spatial interaction framework** where agents update their expectations according to predefined parameters and stochastic influences.

## Features
- **Agent-Based Modeling (ABM)**: Agents interact based on spatial proximity.
- **Expectation Dynamics**: Updates are based on a weighted function of their own expectation, neighboring expectations, and random noise.
- **Visual Representation**: 
  - **Scatter Plot**: Displays agents' positions and expectation levels using a color map.
  - **Histogram**: Shows the distribution of expectations across agents.
- **Interactive Sliders**: Allows real-time adjustment of `beta` (neighbor influence) and `gamma` (random variation).
- **Animation**: Simulates expectation evolution over time.

## Model Parameters
| Parameter         | Description                                      | Default Value |
|------------------|--------------------------------------------------|--------------|
| `N`             | Number of agents                                | 50           |
| `alpha`         | Self-influence weight                           | 0.6          |
| `beta`          | Influence from neighbors                        | 0.3          |
| `gamma`         | Random noise effect                            | 0.1          |
| `interaction_radius` | Maximum distance for neighbor interaction | 0.15         |

## How It Works
1. **Initialization**:
   - Agents are randomly placed within a unit square.
   - Each agent starts with a random expectation value between 0 and 1.

2. **Expectation Update**:
   - Each agent interacts with neighbors within the `interaction_radius`.
   - New expectation values are calculated using:
     \[ \text{new\_expectation}_i = \alpha \cdot \text{expectation}_i + \beta \cdot (\text{mean\_neighbor\_expectation} - \text{expectation}_i) + \gamma \cdot \text{random noise} \]
   - Expectation values are kept within the range \([0,1]\).

3. **Position Update**:
   - Agents move slightly in a random direction each step.
   - Positions are constrained within the unit square to prevent drift.

4. **Visualization**:
   - The scatter plot displays agents colored according to their expectations.
   - The histogram provides a real-time distribution of expectation values.

## Installation & Usage
### Prerequisites
Ensure you have Python installed along with the required libraries:
```bash
pip install numpy matplotlib
