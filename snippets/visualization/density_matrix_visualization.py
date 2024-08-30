from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_density_matrix
import matplotlib.pyplot as plt

def density_matrix_example():
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure_all()
    
    # Simulate the circuit
    aer_sim = Aer.get_backend('aer_simulator')
    qobj = assemble(transpile(qc, aer_sim))
    result = aer_sim.run(qobj).result()
    density_matrix = result.get_density_matrix()
    
    # Visualize density matrix
    plot_density_matrix(density_matrix)
    plt.show()

density_matrix_example()
