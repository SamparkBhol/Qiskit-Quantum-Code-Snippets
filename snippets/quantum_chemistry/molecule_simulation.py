from qiskit import Aer
from qiskit.algorithms import VQE
from qiskit.circuit.library import EfficientSU2
from qiskit.opflow import Z, I, I, Z
from qiskit.utils import QuantumInstance
from qiskit_nature import (QiskitNature, Molecule)
from qiskit_nature.transformers import (ActiveSpaceTransformer, FreezeCoreTransformer)
from qiskit_nature.drivers import PySCFDriver

# Set up the molecule
molecule = Molecule("H2", basis='sto-3g')
driver = PySCFDriver(molecule)
transformer = FreezeCoreTransformer(driver)
active_space = ActiveSpaceTransformer(transformer)
quantum_instance = QuantumInstance(Aer.get_backend('aer_simulator'))

# Define the Hamiltonian
hamiltonian = active_space.get_hamiltonian()

# Define the ansatz (variational form)
ansatz = EfficientSU2(hamiltonian.num_qubits)

# Set up VQE
vqe = VQE(ansatz, quantum_instance=quantum_instance)

# Execute VQE
result = vqe.compute_minimum_eigenvalue(operator=hamiltonian)

# Display results
print("Molecule Energy:", result.eigenvalue.real)
