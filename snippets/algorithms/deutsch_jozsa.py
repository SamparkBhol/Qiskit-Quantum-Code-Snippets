from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def deutsch_jozsa_algorithm(oracle):
    n = oracle.num_qubits - 1  # Number of input qubits

    # Create the quantum circuit
    qc = QuantumCircuit(n + 1, n)

    # Initialize the last qubit to |1>
    qc.x(n)
    qc.h(n)

    # Apply Hadamard gates to input qubits
    qc.h(range(n))

    # Apply the oracle
    qc.append(oracle, range(n + 1))

    # Apply Hadamard gates again
    qc.h(range(n))

    # Measure the input qubits
    qc.measure(range(n), range(n))

    # Run the circuit
    aer_sim = Aer.get_backend('aer_simulator')
    qobj = assemble(transpile(qc, aer_sim))
    result = aer_sim.run(qobj).result()
    counts = result.get_counts()

    return counts

# Example: Creating a constant oracle (always returns 0)
constant_oracle = QuantumCircuit(3)
constant_oracle.i(0)
constant_oracle.i(1)
constant_oracle.i(2)
constant_oracle = constant_oracle.to_gate()
constant_oracle.name = "Constant Oracle"

# Run the algorithm
result = deutsch_jozsa_algorithm(constant_oracle)
print("Deutsch-Jozsa Result:", result)

# Plot the result
plot_histogram(result)
plt.show()
