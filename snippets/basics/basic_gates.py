from qiskit import QuantumCircuit

# Create a Quantum Circuit with 1 qubit
qc = QuantumCircuit(1)

# Apply some basic gates
qc.x(0)  # X gate (NOT gate)
qc.h(0)  # Hadamard gate
qc.z(0)  # Z gate (Phase flip gate)

# Display the circuit
print(qc)

# Output:
#      ┌───┐┌───┐┌───┐
# q_0: ┤ X ├┤ H ├┤ Z ├
#      └───┘└───┘└───┘
