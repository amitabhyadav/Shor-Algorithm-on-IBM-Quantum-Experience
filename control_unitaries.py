#--------------------------------------------------------------------------------------------------------------
# This module contains control unitaries that can be used while developing circuits on IBM QExperience 
#--------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------
# Import necessary modules 
#--------------------------------------------------------------------------------------------------------------
from qiskit import QuantumProgram
import Qconfig
import Basic_gates
# TODO make it more generalized
#--------------------------------------------------------------------------------------------------------------
# The control unitary for 2mod15 on 4 quantum qubits
# Input : Quantum program object, the Circuit name and the quantum register name, and the 
#         control bit number where the connections are supposed to be made 
# Output : Quantum_program_object with the relevant connections
# Circuit implemented - CSwap(Q[3],Q[2])->CSwap(Q[2],Q[1])->CSwap(Q[1],Q[0])
#--------------------------------------------------------------------------------------------------------------
def C_2mod15(Quantum_program_object,Circuit_name,Quantum_register_name,Control_bit_number):
	
	# Get the circuit and the quantum register by name
	qc = Quantum_program_object.get_circuit(Circuit_name)
	qr = Quantum_program_object.get_quantum_register(Quantum_register_name)
	
	Control_bit_number = Control_bit_number
	
	# Implement controlled swap on qr[3] and qr[2] 
	Basic_gates.CSWAP(Quantum_program_object,Circuit_name,Quantum_register_name,Control_bit_number,[3,2])
	
	# Implement controlled swap on qr[2] and qr[1] 
	Basic_gates.CSWAP(Quantum_program_object,Circuit_name,Quantum_register_name,Control_bit_number,[2,1])
	
	# Implement controlled swap on qr[1] and qr[0] 
	Basic_gates.CSWAP(Quantum_program_object,Circuit_name,Quantum_register_name,Control_bit_number,[1,0])
	
	# Return the program object 
	return Quantum_program_object

#--------------------------------------------------------------------------------------------------------------
# The control unitary for 7mod15 on 4 quantum qubits
# Input : Quantum program object, the Circuit name and the quantum register name, and the 
#         control bit number where the connections are supposed to be made 
# Output : Quantum_program_object with the relevant connections
# Circuit implemented - CSwap(Q[1],Q[0])->CSwap(Q[1],Q[2])->CSwap(Q[2],Q[3])->CX on all 4 qubits
#--------------------------------------------------------------------------------------------------------------
def C_7mod15(Quantum_program_object,Circuit_name,Quantum_register_name,Control_bit_number):
	
	# Get the circuit and the quantum register by name
	qc = Quantum_program_object.get_circuit(Circuit_name)
	qr = Quantum_program_object.get_quantum_register(Quantum_register_name)

	Control_bit_number = Control_bit_number
	
	# Implement controlled swap on qr[1] and qr[0] 
	Basic_gates.CSWAP(Quantum_program_object,Circuit_name,Quantum_register_name,Control_bit_number,[1,0])
	
	# Implement controlled swap on qr[2] and qr[1] 
	Basic_gates.CSWAP(Quantum_program_object,Circuit_name,Quantum_register_name,Control_bit_number,[2,1])
	
	# Implement controlled swap on qr[3] and qr[2] 
	Basic_gates.CSWAP(Quantum_program_object,Circuit_name,Quantum_register_name,Control_bit_number,[3,2])
	
	# Implement CX on all four qubits
	qc.cx(Control_bit_number,qr[3])
	qc.cx(Control_bit_number,qr[2])
	qc.cx(Control_bit_number,qr[1])
	qc.cx(Control_bit_number,qr[0])
	
	# Return the program object 
	return Quantum_program_object

#--------------------------------------------------------------------------------------------------------------
# The control unitary for 8mod15 on 4 quantum qubits
# Input : Quantum program object, the Circuit name and the quantum register name, and the 
#         control bit number where the connections are supposed to be made
# Output : Quantum_program_object with the relevant connections
# Circuit implemented - CSwap(Q[1],Q[0])->CSwap(Q[1],Q[2])->CSwap(Q[2],Q[3])
#--------------------------------------------------------------------------------------------------------------
def C_8mod15(Quantum_program_object,Circuit_name,Quantum_register_name,Control_bit_number):
	
	# Get the circuit and the quantum register by name
	qc = Quantum_program_object.get_circuit(Circuit_name)
	qr = Quantum_program_object.get_quantum_register(Quantum_register_name)
	
	Control_bit_number = Control_bit_number
	
	# Implement controlled swap on qr[1] and qr[0] 
	Basic_gates.CSWAP(Quantum_program_object,Circuit_name,Quantum_register_name,Control_bit_number,[1,0])
	
	# Implement controlled swap on qr[2] and qr[1] 
	Basic_gates.CSWAP(Quantum_program_object,Circuit_name,Quantum_register_name,Control_bit_number,[2,1])
	
	# Implement controlled swap on qr[3] and qr[2] 
	Basic_gates.CSWAP(Quantum_program_object,Circuit_name,Quantum_register_name,Control_bit_number,[3,2])
	
	# Return the program object 
	return Quantum_program_object

#--------------------------------------------------------------------------------------------------------------
# The control unitary for 11mod15 on 4 quantum qubits
# Input : Quantum program object, the Circuit name and the quantum register name, and the 
#         control bit number where the connections are supposed to be made
# Output : Quantum_program_object with the relevant connections
# Circuit implemented - CSwap(Q[2],Q[0])->CSwap(Q[3],Q[1])->CX on all 4 qubits
#--------------------------------------------------------------------------------------------------------------
def C_11mod15(Quantum_program_object,Circuit_name,Quantum_register_name,Control_bit_number):
	
	# Get the circuit and the quantum register by name
	qc = Quantum_program_object.get_circuit(Circuit_name)
	qr = Quantum_program_object.get_quantum_register(Quantum_register_name)
	
	Control_bit_number = Control_bit_number
	
	# Implement controlled swap on qr[2] and qr[0] 
	Basic_gates.CSWAP(Quantum_program_object,Circuit_name,Quantum_register_name,Control_bit_number,[2,0])
	
	# Implement controlled swap on qr[3] and qr[1] 
	Basic_gates.CSWAP(Quantum_program_object,Circuit_name,Quantum_register_name,Control_bit_number,[3,1])
	
	# Implement CX on all four qubits
	qc.cx(Control_bit_number,qr[3])
	qc.cx(Control_bit_number,qr[2])
	qc.cx(Control_bit_number,qr[1])
	qc.cx(Control_bit_number,qr[0])
	
	# Return the program object 
	return Quantum_program_object

#--------------------------------------------------------------------------------------------------------------
# The control unitary for 13mod15 on 4 quantum qubits
# Input : Quantum program object, the Circuit name and the quantum register name, and the 
#         control bit number where the connections are supposed to be made
# Output : Quantum_program_object with the relevant connections
# Circuit implemented - CSwap(Q[3],Q[2])->CSwap(Q[2],Q[1])->CSwap(Q[1],Q[0])->CX on all 4 qubits
#--------------------------------------------------------------------------------------------------------------
def C_13mod15(Quantum_program_object,Circuit_name,Quantum_register_name,Control_bit_number):
	
	# Get the circuit and the quantum register by name
	qc = Quantum_program_object.get_circuit(Circuit_name)
	qr = Quantum_program_object.get_quantum_register(Quantum_register_name)
	
	Control_bit_number = Control_bit_number
	
	# Implement controlled swap on qr[3] and qr[2] 
	Basic_gates.CSWAP(Quantum_program_object,Circuit_name,Quantum_register_name,Control_bit_number,[3,2])
	
	# Implement controlled swap on qr[2] and qr[1] 
	Basic_gates.CSWAP(Quantum_program_object,Circuit_name,Quantum_register_name,Control_bit_number,[2,1])
	
	# Implement controlled swap on qr[1] and qr[0] 
	Basic_gates.CSWAP(Quantum_program_object,Circuit_name,Quantum_register_name,Control_bit_number,[1,0])

	# Implement CX on all four qubits
	qc.cx(Control_bit_number,qr[3])
	qc.cx(Control_bit_number,qr[2])
	qc.cx(Control_bit_number,qr[1])
	qc.cx(Control_bit_number,qr[0])
	
	# Return the program object 
	return Quantum_program_object
