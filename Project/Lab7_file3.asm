# Simple Loop Operation
# This creates an infinte loop

	# Declare main as a global function
	.globl main 

	# All program code is placed after the
	# .text assembler directive
	.text 		

# The label 'main' represents the starting point
main:
	
	#Load the address of the array of integers  
	#into a register 
	la $t0, Integers 
	
	#Set $s0 as my count variable and intialize it to zero
	li $s0, 0

	#Store the ending value in $s1
	li $s1, 13

Loop:
	#Invoke print integer function:
	li $v0, 1
	lw $a0, 0($t0)
	syscall

	#Print a tab space in between numbers:
	li $v0, 4
	la $a0, TabSpace
	syscall

	addi $t0, $t0, 4	#increment address by 4 (i.e. shift 4-bytes)
	addi $s0, $s0, 1	#increment counter by 1

	beq $s0, $s1, Exit	#Check if counter == end value
	j Loop			#Perfom an unconditional jump to above address
	

Exit:	li $v0, 10
	syscall	


	.data

Integers: .word 0,5,10,15,20,25,30,35,40,45,50,55,60
TabSpace: .asciiz "\t"

