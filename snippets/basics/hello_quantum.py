from qiskit import QuantumCircuit

# Create a Quantum Circuit with 1 qubit
qc = QuantumCircuit(1)

# Apply a Hadamard gate to the qubit to create a superposition
qc.h(0)

# Display the circuit
print(qc)

# Output:
#      ┌───┐
# q_0: ┤ H ├
#      └───┘
