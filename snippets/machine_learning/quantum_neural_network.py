from qiskit import Aer
from qiskit.algorithms import VQE
from qiskit.circuit.library import EfficientSU2
from qiskit.opflow import Z, I
from qiskit.utils import QuantumInstance

# Define a simple Hamiltonian
H = (I ^ Z) + (Z ^ I)

# Define the ansatz (variational form)
ansatz = EfficientSU2(2)

# Set up VQE as a QNN
vqe = VQE(ansatz, quantum_instance=QuantumInstance(Aer.get_backend('aer_simulator')))

# Execute VQE
result = vqe.compute_minimum_eigenvalue(operator=H)

# Display results
print("Quantum Neural Network Result:", result.eigenvalue.real)
