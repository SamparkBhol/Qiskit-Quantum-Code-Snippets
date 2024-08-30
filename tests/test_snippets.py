import unittest
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import io

class TestQuantumSnippets(unittest.TestCase):

    def test_bit_flip_code(self):
        from snippets.error_correction.bit_flip_code import bit_flip_code
        result = bit_flip_code()
        self.assertTrue('000' in result or '111' in result)

    def test_phase_flip_code(self):
        from snippets.error_correction.phase_flip_code import phase_flip_code
        result = phase_flip_code()
        self.assertTrue('000' in result or '111' in result)

    def test_shor_code(self):
        from snippets.error_correction.shor_code import shor_code
        result = shor_code()
        self.assertTrue('000000000' in result or '111111111' in result)

    def test_circuit_visualization(self):
        from snippets.visualization.circuit_visualization import create_circuit
        qc = create_circuit()
        with io.StringIO() as buf, self.assertRaises(SystemExit):
            qc.draw('mpl', file=buf)
            buf.seek(0)
            output = buf.getvalue()
            self.assertTrue('QuantumCircuit' in output)

    def test_bloch_sphere(self):
        from snippets.visualization.bloch_sphere import bloch_sphere_example
        with io.StringIO() as buf, self.assertRaises(SystemExit):
            bloch_sphere_example()
            buf.seek(0)
            output = buf.getvalue()
            self.assertTrue('Bloch sphere' in output)

    def test_density_matrix_visualization(self):
        from snippets.visualization.density_matrix_visualization import density_matrix_example
        with io.StringIO() as buf, self.assertRaises(SystemExit):
            density_matrix_example()
            buf.seek(0)
            output = buf.getvalue()
            self.assertTrue('Density matrix' in output)

if __name__ == '__main__':
    unittest.main()
