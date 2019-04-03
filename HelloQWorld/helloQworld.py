import qiskit
from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit, BasicAer
from qiskit.tools.visualization import plot_histogram


#
# Implements a simple XOR gate as hello world to quantum computing
#


def main():
    # Declare our registers
    q_reg = QuantumRegister(2)
    c_reg = ClassicalRegister(2)
    circuit = QuantumCircuit(q_reg, c_reg)
    # Build our circuit
    circuit.x(q_reg[0])  # invert qubit(0) |0> to |1>
    circuit.x(q_reg[1])  # invert qubit(1) |0> to |1>
    circuit.barrier()
    circuit.h(q_reg[0])  # bring qubit(0) into superposition
    circuit.cx(q_reg[1], q_reg[0])  # entangle qubit(0) with qubit(1) with result same as XORing
    circuit.barrier()
    circuit.measure(q_reg, c_reg)  # measure the results
    # Draw it
    schem = circuit.draw(output='mpl')
    schem.savefig("Qcircuit_schem.png")
    # Run it
    back = BasicAer.get_backend('qasm_simulator')
    job_sim = qiskit.execute(circuit, back)
    sim_result = job_sim.result()
    print(sim_result.get_counts(circuit))
    # Plot it
    fig = plot_histogram(sim_result.get_counts(circuit))
    fig.savefig("Qcircuit_hist.png")


if __name__ == '__main__':
    main()
