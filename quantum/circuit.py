from qiskit import QuantumCircuit

def create_entangled_circuit(n_qubits=3):
    qc = QuantumCircuit(n_qubits)

    # Create entanglement (GHZ state)
    qc.h(0)
    for i in range(n_qubits - 1):
        qc.cx(i, i + 1)

    return qc