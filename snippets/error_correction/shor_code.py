from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def shor_code():
    # Create a quantum circuit with 9 qubits
    qc = QuantumCircuit(9, 9)

    # Encode a single qubit into a Shor code
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(0, 2)
    qc.cx(3, 4)
    qc.cx(3, 5)
    qc.cx(6, 7)
    qc.cx(6, 8)

    # Introduce errors
    qc.x(4)  # Bit-flip error
    qc.z(7)  # Phase-flip error

    # Error detection and correction
    qc.cx(1, 3)
    qc.cx(2, 3)
    qc.cx(4, 6)
    qc.cx(5, 6)
    qc.cx(7, 8)
    qc.cx(8, 6)

    # Measure the qubits
    qc.measure(range(9), range(9))

    # Run the circuit
    aer_sim = Aer.get_backend('aer_simulator')
    qobj = assemble(transpile(qc, aer_sim))
    result = aer_sim.run(qobj).result()
    counts = result.get_counts()

    return counts

# Execute and print results
result = shor_code()
print("Shor Code Result:", result)

# Plot the result
plot_histogram(result)
plt.show()
