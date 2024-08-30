from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_circuit_layout, plot_bloch_multivector
import matplotlib.pyplot as plt

def optimize_circuit():
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    qc.rz(1.0, 0)
    qc.ry(0.5, 1)
    qc.measure_all()
    
    # Optimize the circuit
    optimized_qc = transpile(qc, optimization_level=3)
    
    # Plot optimized circuit
    optimized_qc.draw('mpl')
    plt.show()

optimize_circuit()
