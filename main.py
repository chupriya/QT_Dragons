from quantum.circuit import create_entangled_circuit
from quantum.entanglement import compute_entanglement
from visualization.bloch import show_bloch
from visualization.network import plot_entanglement_graph

def main():
    n_qubits = 4

    qc = create_entangled_circuit(n_qubits)

    ent_matrix, state = compute_entanglement(qc)

    print("Entanglement Matrix:")
    print(ent_matrix)

    # Bloch visualization
    show_bloch(state)

    # 3D graph
    plot_entanglement_graph(ent_matrix)

if __name__ == "__main__":
    main()