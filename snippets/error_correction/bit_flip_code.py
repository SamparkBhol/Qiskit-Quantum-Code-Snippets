from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def bit_flip_code():
    # Create a quantum circuit with 3 qubits
    qc = QuantumCircuit(3, 3)

    # Encode the bit flip code (|0> → |000> and |1> → |111>)
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(0, 2)

    # Introduce a bit flip error on qubit 1
    qc.x(1)

    # Error detection and correction
    qc.cx(1, 0)
    qc.cx(2, 0)
    qc.cx(1, 2)

    # Measure the qubits
    qc.measure([0, 1, 2], [0, 1, 2])

    # Run the circuit
    aer_sim = Aer.get_backend('aer_simulator')
    qobj = assemble(transpile(qc, aer_sim))
    result = aer_sim.run(qobj).result()
    counts = result.get_counts()

    return counts

# Execute and print results
result = bit_flip_code()
print("Bit Flip Code Result:", result)

# Plot the result
plot_histogram(result)
plt.show()
