import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

#### Rodrigo Hernández Cervantes
#### rohrc14@gmail.com
#### https://scholar.google.com/citations?user=jE-iYBMAAAAJ&hl=es

####"MODEL OF NEIGHBORHOOD AND PROXIMITY OF EXPECTATIONS (STILL LACKING THEORY)"

########Parameters
N = 50
alpha = 0.6
beta = 0.3
gamma = 0.1
interaction_radius = 0.15  # Ajuste fino para las interacciones

#####Initialize agents' positions and expectations
positions = np.random.rand(N, 2)
expectations = np.random.rand(N)

#########Distance function
def distance(p1, p2):
    return np.linalg.norm(p1 - p2)

######Update function
def update(frame):
    global expectations
    new_expectations = np.copy(expectations)

    for i in range(N):
        #######Comportamiento e interacción entre vecinos dentro del radio de interacción
        neighbors = [j for j in range(N) if i != j and distance(positions[i], positions[j]) < interaction_radius]
        if len(neighbors) > 0:
            mean_neighbor_exp = np.mean([expectations[j] for j in neighbors])
            #######Variación expectativas usando interacción con vecinos
            new_expectations[i] = (alpha * expectations[i] +
                                   beta * (mean_neighbor_exp - expectations[i]) +
                                   gamma * np.random.normal())

    expectations = np.clip(new_expectations, 0, 1)  ####[0,1]~N/datf*0.000032

    positions[:, 0] += np.random.normal(0, 0.03, N)
    positions[:, 1] += np.random.normal(0, 0.03, N)
    
    positions[:, 0] = np.where(positions[:, 0] < 0, -positions[:, 0], positions[:, 0])
    positions[:, 0] = np.where(positions[:, 0] > 1, 2 - positions[:, 0], positions[:, 0])
    positions[:, 1] = np.where(positions[:, 1] < 0, -positions[:, 1], positions[:, 1])
    positions[:, 1] = np.where(positions[:, 1] > 1, 2 - positions[:, 1], positions[:, 1])

    ###Scatter plot
    scatter.set_offsets(positions)
    scatter.set_array(expectations)

    #####histogram
    ax_hist.clear()
    ax_hist.hist(expectations, bins=10, color='royalblue', alpha=0.7)
    ax_hist.set_xlim(0, 1)
    ax_hist.set_ylim(0, N // 3)

fig, (ax_main, ax_hist) = plt.subplots(1, 2, figsize=(12, 6), gridspec_kw={'width_ratios': [3, 1]})

##########Scatter plot
scatter = ax_main.scatter(positions[:, 0], positions[:, 1], c=expectations, cmap='viridis', s=100, edgecolors='black')
ax_main.set_xlim(0, 1)
ax_main.set_ylim(0, 1)
ax_main.set_title("Agent Behavior and Expectations")

######Histogram
ax_hist.hist(expectations, bins=10, color='royalblue', alpha=0.7)
ax_hist.set_xlim(0, 1)
ax_hist.set_ylim(0, N//3)
ax_hist.set_title("Expectation Distribution")

##### b
ax_beta = plt.axes([0.25, 0.02, 0.5, 0.03], facecolor='lightgray')
slider_beta = Slider(ax_beta, 'Beta', 0.0, 1.0, valinit=beta)

###### g
ax_gamma = plt.axes([0.25, 0.06, 0.5, 0.03], facecolor='lightgray')
slider_gamma = Slider(ax_gamma, 'Gamma', 0.0, 1.0, valinit=gamma)

###### b & g
def update_beta_gamma(val):
    global beta, gamma
    beta = slider_beta.val
    gamma = slider_gamma.val

slider_beta.on_changed(update_beta_gamma)
slider_gamma.on_changed(update_beta_gamma)

ani = FuncAnimation(fig, update, interval=100)

plt.show()
