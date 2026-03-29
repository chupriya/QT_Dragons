from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

def show_bloch(state):
    fig = plot_bloch_multivector(state)
    plt.show()