from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.circuit.library import GroverOperator, PhaseOracle
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Define the oracle for a simple problem
oracle = PhaseOracle("a & b")

# Create Grover's algorithm circuit
grover_op = GroverOperator(oracle)
grover_circuit = QuantumCircuit(grover_op.num_qubits)
grover_circuit.h(range(grover_op.num_qubits - 1))
grover_circuit.append(grover_op, range(grover_op.num_qubits))
grover_circuit.measure_all()

# Simulate the circuit
aer_sim = Aer.get_backend('aer_simulator')
qobj = assemble(transpile(grover_circuit, aer_sim))
result = aer_sim.run(qobj).result()
counts = result.get_counts()

print("Grover's algorithm result:", counts)

# Plot the result
plot_histogram(counts)
plt.show()
