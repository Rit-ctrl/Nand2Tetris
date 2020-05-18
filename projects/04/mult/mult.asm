// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
@0
D=M
@div
M=D
@prod
M=0

(LOOP)
@1
D=M
@END
D;JLE
@div
D=M
@prod
M=M+D
@1
M=M-1
@LOOP
0;JMP
 
(END)
@END
@prod
D=M
@2
M=D

(TERMINATE)
@TERMINATE
0;JMP
	
