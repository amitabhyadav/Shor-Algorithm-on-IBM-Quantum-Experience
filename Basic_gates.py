#--------------------------------------------------------------------------------------------------------------
# This module contains basic gates that can be used while developing circuits on IBM QExperience 
#--------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------
# Import necessary modules 
#--------------------------------------------------------------------------------------------------------------
from qiskit import QuantumProgram
import Qconfig

#--------------------------------------------------------------------------------------------------------------
# The CSWAP gate
# Input : Quantum program object, the Circuit name, the quantum register name, control bit number and target
#         bit numbers.
# Output : Quantum_program_object with the relevant connections
# Circuit implemented - CSWAP
#--------------------------------------------------------------------------------------------------------------
def CSWAP(Quantum_program_object,Circuit_name,Quantum_register_name,Control_bit_number,Target_bit_numbers):
	
	# Get the circuit and the quantum register by name
	qc = Quantum_program_object.get_circuit(Circuit_name)
	qr = Quantum_program_object.get_quantum_register(Quantum_register_name)
	
	# Get control bit numbers and the target bit number for the addressing the qubits
	Control = Control_bit_number
	Target_1 = Target_bit_numbers[0]
	Target_2 = Target_bit_numbers[1]
	
	# Implement CSWAP using 3 CCNOT implementations
	
	# Implement CCNOT on Control,Target_1 and Target_2 using decomposition given by Nelson and Chuang
	qc.h(qr[Target_2])
	qc.cx(qr[Target_1],qr[Target_2])
	qc.tdg(qr[Target_2])
	qc.cx(qr[Control],qr[Target_2])
	qc.t(qr[Target_2])
	qc.cx(qr[Target_1],qr[Target_2])
	qc.tdg(qr[Target_2])
	qc.cx(qr[Control],qr[Target_2])
	qc.tdg(qr[Target_1])
	qc.t(qr[Target_2])
	qc.h(qr[Target_2])
	qc.cx(qr[Control],qr[Target_1])
	qc.tdg(qr[Target_1])
	qc.cx(qr[Control],qr[Target_1])
	qc.t(qr[Control])
	qc.s(qr[Target_1])
	
	# Implement CCNOT on Control,Target_2 and Target_1 using decomposition given by Nelson and Chuang
	qc.h(qr[Target_1])
	qc.cx(qr[Target_2],qr[Target_1])
	qc.tdg(qr[Target_1])
	qc.cx(qr[Control],qr[Target_1])
	qc.t(qr[Target_1])
	qc.cx(qr[Target_2],qr[Target_1])
	qc.tdg(qr[Target_1])
	qc.cx(qr[Control],qr[Target_1])
	qc.tdg(qr[Target_2])
	qc.t(qr[Target_1])
	qc.h(qr[Target_1])
	qc.cx(qr[Control],qr[Target_2])
	qc.tdg(qr[Target_2])
	qc.cx(qr[Control],qr[Target_2])
	qc.t(qr[Control])
	qc.s(qr[Target_2])
	
	# Implement CCNOT on Control,Target_1 and Target_2 using decomposition given by Nelson and Chuang
	qc.h(qr[Target_2])
	qc.cx(qr[Target_1],qr[Target_2])
	qc.tdg(qr[Target_2])
	qc.cx(qr[Control],qr[Target_2])
	qc.t(qr[Target_2])
	qc.cx(qr[Target_1],qr[Target_2])
	qc.tdg(qr[Target_2])
	qc.cx(qr[Control],qr[Target_2])
	qc.tdg(qr[Target_1])
	qc.t(qr[Target_2])
	qc.h(qr[Target_2])
	qc.cx(qr[Control],qr[Target_1])
	qc.tdg(qr[Target_1])
	qc.cx(qr[Control],qr[Target_1])
	qc.t(qr[Control])
	qc.s(qr[Target_1])
	
	# Return the program object 
	return Quantum_program_object


#--------------------------------------------------------------------------------------------------------------
# The CCNOT gate
# Input : Quantum program object, the Circuit name, the quantum register name, control bit numbers and target
#         bit number.
# Output : Quantum_program_object with the relevant connections
# Circuit implemented - CCNOT
#--------------------------------------------------------------------------------------------------------------
def CCNOT(Quantum_program_object,Circuit_name,Quantum_register_name,Control_bit_numbers,Target_bit_number):
	
	# Get the circuit and the quantum register by name
	qc = Quantum_program_object.get_circuit(Circuit_name)
	qr = Quantum_program_object.get_quantum_register(Quantum_register_name)
	
	# Get control bit numbers and the target bit number for the addressing the qubits
	Control_1 = Control_bit_numbers[0]
	Control_2 = Control_bit_numbers[1]
	Target = Target_bit_number
	
	# Implement Hadamard on target qubits
	qc.h(qr[Target])
	
	# Implement CNOT between Control_2 and Target
	qc.cx(qr[Control_2],qr[Target])
	
	# Implement T (dagger) on target qubits
	qc.tdg(qr[Target])
	
	# Implement CNOT between Control_1 and Target
	qc.cx(qr[Control_1],qr[Target])
	
	# Implement T on target qubits
	qc.t(qr[Target])
	
	# Implement CNOT between Control_2 and Target
	qc.cx(qr[Control_2],qr[Target])
	
	# Implement T (dagger) on target qubits
	qc.tdg(qr[Target])
	
	# Implement CNOT between Control_1 and Target
	qc.cx(qr[Control_1],qr[Target])
	
	# Implement T (dagger) on Control_2, T and H on Target
	qc.tdg(qr[Control_2])
	qc.t(qr[Target])
	qc.h(qr[Target])
	
	# Implement CNOT from Control_1 to Control_2 followed by T (dagger) on Control_2
	qc.cx(qr[Control_1],qr[Control_2])
	qc.tdg(qr[Control_2])
	
	# Implement CNOT from Control_1 to Control_2 followed by T on Control_1 and S on Control_2
	qc.cx(qr[Control_1],qr[Control_2])
	qc.t(qr[Control_1])
	qc.s(qr[Control_2])
	
	# Return the program object 
	return Quantum_program_object
