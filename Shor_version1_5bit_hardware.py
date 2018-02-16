#--------------------------------------------------------------------------------------------------------------
# Import necessary modules 
#--------------------------------------------------------------------------------------------------------------
import sys
from qiskit import QuantumProgram
import Qconfig
import Basic_gates
import math
from random import randint
import control_unitaries

#--------------------------------------------------------------------------------------------------------------
# global variables  
#--------------------------------------------------------------------------------------------------------------
Counts = 0
#--------------------------------------------------------------------------------------------------------------
# The function to compute GCD using Euclid's method
# Input : Two number to X and Y for which a GCD is to be computed
# Output : GCD of two given numbers
#--------------------------------------------------------------------------------------------------------------	
def gcd(x,y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

#--------------------------------------------------------------------------------------------------------------
# The function to compute QFT
# Input : Circuit, quantum bits, and number of quantum bits
# Output : None. Circuit is created and saved
#--------------------------------------------------------------------------------------------------------------	
def qft(Quantum_program_object,Circuit_name,Quantum_register_name,Smallest_Quantum_register_number,Size_of_QFT):
	# Get the circuit and the quantum register by name
	qc = Quantum_program_object.get_circuit(Circuit_name)
	qr = Quantum_program_object.get_quantum_register(Quantum_register_name)
	s = Smallest_Quantum_register_number
	for j in range(Size_of_QFT):
		for k in range(j):
			qc.cu1(math.pi/float(2**(j-k)), qr[s+j], qr[s+k])
		qc.h(qr[s+j])

#--------------------------------------------------------------------------------------------------------------
# The function to find period using the Quantum computer
# Input : a and N for which the period is to be computed.
# Output : period r of the function a^x mod N
#--------------------------------------------------------------------------------------------------------------	
def period(a,N):
# Create the first QuantumProgram object instance.
	qp = QuantumProgram()
	qp.set_api(Qconfig.APItoken, Qconfig.config["url"])
# TO DO : generalize the number of qubits and give proper security against rogue input.
# Create the first Quantum Register called "qr" with 12 qubits 
	qr = qp.create_quantum_register('qr', 5)
# Create your first Classical Register  called "cr" with 12 bits
	cr = qp.create_classical_register('cr', 3)

# Create the first Quantum Circuit called "qc" involving your Quantum Register "qr"
# and the Classical Register "cr"
	qc = qp.create_circuit('Period_Finding', [qr], [cr])

# Get the circuit and the registers by name 
	Shor1 = qp.get_circuit('Period_Finding')
	Q_reg = qp.get_quantum_register('qr')
	C_reg = qp.get_classical_register('cr')

# Create the circuit for period finding
# Initialize qr[0] to |1> and create a superposition on the top 8 qubits
	Shor1.x(Q_reg[0])

# Step one : apply 11**4 mod 15
	Shor1.h(Q_reg[2])
# Controlled Identity to remaining gates which is equivalent to doing nothing
	Shor1.h(Q_reg[2])
	Shor1.measure(Q_reg[2],C_reg[0])
# Reinitialize to |0>
	Shor1.reset(Q_reg[2])

# Step two : apply 11**2 mod 15
	Shor1.h(Q_reg[2])
# Controlled Identity to remaining gates which is equivalent to doing nothing
	if C_reg[0] == 1 :
		Shor1.u1(pi/2.0,Q_reg[2])
	Shor1.h(Q_reg[2])
	Shor1.measure(Q_reg[2],C_reg[1])	
# Reinitialize to |0>
	Shor1.reset(Q_reg[2])

# Step three : apply 11 mod 15
	Shor1.h(Q_reg[2])
# Controlled nots in between to remaining gates which is equivalent to doing nothing
	Shor1.cx(Q_reg[2],Q_reg[1])
	Shor1.cx(Q_reg[2],Q_reg[4])
# Feed forward and measure
	if C_reg[1] == 1 :
		Shor1.u1(pi/2.0,Q_reg[2])
	if C_reg[0] == 1 :
		Shor1.u1(pi/4.0,Q_reg[2])
	Shor1.h(Q_reg[2])
	Shor1.measure(Q_reg[2],C_reg[2])	
	
	# Run the circuit
	while True:
		global Counts
		Counts = Counts + 1
		qp.set_api(Qconfig.APItoken, Qconfig.config['url']) # set the APIToken and API url
		simulate = qp.execute(["Period_Finding"], backend="ibmqx4", shots=1,timeout=500)
		simulate.get_counts("Period_Finding")
		#print(simulate)
		data = simulate.get_counts("Period_Finding") 
		#print(data)
		data = list(data.keys())
		#print(data)
		r = int(data[0])
		#print(r)
		l = gcd(2**3,r)
		#print(l)
		r = int((2**3)/l)
		#print(r)
		if (r%2 == 0) and (((a**(r/2))+1)%N != 0) and (r != 0) and (r != 8):
			break
	return r

#--------------------------------------------------------------------------------------------------------------
# The main function to compute factors
# Input : The number to be factored, N
# Output : Factors of the number
#--------------------------------------------------------------------------------------------------------------	
def Factorize_N(N):
	factors = [0,0]
#--------------------------------------------------------------------------------------------------------------
# Step 1 : Determine the number of bits based on N; n = [log2(N)]
#--------------------------------------------------------------------------------------------------------------
	n = math.ceil(math.log(N,2))
#--------------------------------------------------------------------------------------------------------------
# Step 2 : Check if N is even. In that case return 2 and the remaining number as factors
#--------------------------------------------------------------------------------------------------------------
	if N % 2 == 0:
		factors = [2,N/2]
		return factors
#--------------------------------------------------------------------------------------------------------------
# Step 3 : Check if N is of the form P^(k), where P is some prime factor. In that case return P and k.
#--------------------------------------------------------------------------------------------------------------
	
#--------------------------------------------------------------------------------------------------------------
# Step 4 : Choose a random number between 2...(N-1).
#--------------------------------------------------------------------------------------------------------------
	a = randint(2,N-1)
	a = 11
#--------------------------------------------------------------------------------------------------------------
# Step 5 : Take GCD of a and N. t = GCD(a,N)
#--------------------------------------------------------------------------------------------------------------
	t = gcd(N,a)
	if t > 1:
		factors = [t,N/t]
		return factors
#--------------------------------------------------------------------------------------------------------------
# Step 6 : t = 1. Hence, no common period. Find Period using Shor's method
#--------------------------------------------------------------------------------------------------------------
	r = period(a,N)
	factor_1 = gcd((a**(r/2))+1,N)
	factor_2 = N/factor_1
	factors = [factor_1,factor_2]
	return factors

#--------------------------------------------------------------------------------------------------------------
# Running the Shor's algorithm version 1
#--------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------
# Step 0 : Take the input N
#--------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
	N = 15
	factors = Factorize_N(N)
	print("The Number being factorized is : 15 with a = 11")
	print("Factors are = ",factors)
	print("Number of times the circuit looped to find out the period = ",Counts)
