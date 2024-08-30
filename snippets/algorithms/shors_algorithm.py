from qiskit import Aer, execute
from qiskit.algorithms import Shor
from qiskit.utils import QuantumInstance

# Shor's algorithm to factorize 15
N = 15

# Initialize Shor's algorithm
shor = Shor()

# Run the algorithm
quantum_instance = QuantumInstance(Aer.get_backend('aer_simulator'))
result = shor.factor(N, quantum_instance=quantum_instance)

# Display results
print("Factors found:", result.factors)
