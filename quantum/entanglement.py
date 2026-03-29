import numpy as np
from qiskit.quantum_info import Statevector, partial_trace, entropy

def compute_entanglement(qc):
    state = Statevector.from_instruction(qc)
    n = qc.num_qubits

    entanglement_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(i+1, n):
            reduced = partial_trace(state, [k for k in range(n) if k not in [i, j]])
            ent = entropy(reduced)
            entanglement_matrix[i][j] = ent
            entanglement_matrix[j][i] = ent

    return entanglement_matrix, state