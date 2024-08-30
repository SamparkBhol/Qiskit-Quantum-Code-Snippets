from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_multivector, plot_histogram
import matplotlib.pyplot as plt

def create_circuit():
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure_all()
    return qc

# Create a quantum circuit
qc = create_circuit()

# Visualize the circuit
qc.draw('mpl')
plt.show()
