from qiskit import Aer
from qiskit.algorithms import VQE
from qiskit.circuit.library import EfficientSU2
from qiskit.opflow import I, Z, X
from qiskit.utils import QuantumInstance

# Define Hamiltonian for a simple problem: H = Z ^ Z
H = (I ^ I) + (Z ^ Z)

# Define the ansatz (variational form)
ansatz = EfficientSU2(2)

# Set up VQE
vqe = VQE(ansatz, quantum_instance=QuantumInstance(Aer.get_backend('aer_simulator')))

# Execute VQE
result = vqe.compute_minimum_eigenvalue(operator=H)

# Display results
print("VQE Result:", result.eigenvalue.real)
