from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

def bloch_sphere_example():
    qc = QuantumCircuit(1)
    qc.h(0)
    qc.measure_all()
    
    # Simulate the circuit
    aer_sim = Aer.get_backend('aer_simulator')
    qobj = assemble(transpile(qc, aer_sim))
    result = aer_sim.run(qobj).result()
    statevector = result.get_statevector()
    
    # Visualize Bloch sphere
    plot_bloch_multivector(statevector)
    plt.show()

bloch_sphere_example()
