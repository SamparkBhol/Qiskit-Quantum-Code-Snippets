from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.circuit.library import QFT
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Define the number of qubits
n_qubits = 3

# Create the Quantum Fourier Transform circuit
qft_circuit = QuantumCircuit(n_qubits)
qft_circuit.h(0)
qft_circuit.h(1)
qft_circuit.h(2)
qft_circuit.append(QFT(num_qubits=n_qubits, do_swaps=False), range(n_qubits))
qft_circuit.measure_all()

# Simulate the circuit
aer_sim = Aer.get_backend('aer_simulator')
qobj = assemble(transpile(qft_circuit, aer_sim))
result = aer_sim.run(qobj).result()
counts = result.get_counts()

print("QFT result:", counts)

# Plot the result
plot_histogram(counts)
plt.show()
