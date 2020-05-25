# -*- coding: utf-8 -*-
"""
Created on Wed May 20 19:49:44 2020

@author: RITHIC
"""

C_ins_0={
       "0" : 	"101010",
"1" :	"111111",
"-1" 	:"111010",
"D" 	:"001100",
"A" 	:"110000",
"!D" 	:"001101",
"!A" 	:"110001",
"-D" 	:"001111",
"-A"	:"110011",
"D+1" 	:"011111",
"A+1" 	:"110111", 
"D-1" 	:"001110",
"A-1" 	:"110010", 
"D+A" 	:"000010", 
"D-A" 	:"010011", 
"A-D" 	:"000111", 
"D&A" 	:"000000", 
"D|A" :"010101",     
       }

C_ins_1={
        "M"	:"110000",
"!M"	:"110001",
"-M"	:"110011",
"M+1"	:"110111",
"M-1"	:"110010",
"D+M"	:"000010",
"D-M"	:"010011",
"M-D"	:"000111",
"D&M"	:"000000",
"D|M"	:"010101",
        }

Dest={
      
"null" :"000",
"M" :"001",
"D" :"010",
"MD" :"011",
"A" :"100",
"AM" :"101",
"AD" :"110",
"AMD" :"111",
      }

Jump={
      
"null" :"000",
"JGT" :"001",
"JEQ" :"010",
"JGE" :"011",
"JLT" :"100",
"JNE" :"101",
"JLE" :"110",
"JMP":"111",
        
      }
Symbols={ 
    "SP": "0",
    "LCL": "1",
"ARG": "2", 
"THIS": "3", 
"THAT": "4",
"R0":"0",
"R1":"1",
"R2":"2",
"R3":"3",
"R4":"4",
"R5":"5",
"R6":"6",
"R7":"7",
"R8":"8",
"R9":"9",
"R10":"10",
"R11":"11",
"R12":"12",
"R13":"13",
"R14":"14",
"R15":"15",
"SCREEN":"16384",
"KBD":"24576",

        }
from parse import *
f=open("./pong/Pong.asm","r")
w=open("op.txt","w")
List=[]

for line in f:
    if line[0] != '\n' and line[0] !=  '/' :
        #print(line.strip())
        List.append(line.strip())

n=16                           
line=0  
Dup=List.copy()
for l in Dup:                   #handling loop variables ie pseudocommands
    if l[0]=='(':
        Symbols[l[1:-1]]=str(line)
        print(l[1:-1])
    else:
        line=line+1

for index,l in enumerate(Dup):            #handling variables
    if l[0]=="@":
        if(l[1:] in Symbols):           #check if it is already defined in symbols
            #print("yes")
            Dup[index]="@"+Symbols.get(l[1:])
        elif l[1:].isnumeric()!=True :      #if not add to symbols
           # print("Not")
            Symbols[l[1:]]=str(n)
            n=n+1
            
for index,l in enumerate(Dup):            #handling variables
    if l[0]=="@":
        if(l[1:] in Symbols):           #check if it is already defined in symbols
            #print("yes")
            Dup[index]="@"+Symbols.get(l[1:])            

for index,l in enumerate(Dup):          #removing pseudocommands
    if l[0]=="(":
        del Dup[index]           

for index,l in enumerate(Dup):
     if l[0]=='@':
         num=0        
         for x in l[1:] :
             a=ord(x)
             a=a-48
             num=num*10+a    
         #print(format(num,'016b'))
         w.write((format(num,'016b'))+"\n")
     else:
         #print(index)
         if(l.find('=')!=-1 and l.find(';')==-1) :         #d=c
             r=parse("{}={}",l)
             if r[1] in C_ins_0:
                 #print(C_ins_0.get(r[1]))
                 t="1110"+C_ins_0.get(r[1])
             if r[1] in C_ins_1:
                 #print(C_ins_1.get(r[1]))
                 t="1111"+C_ins_1.get(r[1])
             if r[0] in Dest:
                 #print(Dest.get(r[0]))
                 t=t+Dest.get(r[0])+"000"
             w.write(t+"\n")
         elif (l.find(';')!=-1 and l.find('=')==-1):                #c;j
             r=parse("{};{}",l)
             if r[0] in C_ins_0:
                 #print(r[0])
                 #print(C_ins_0.get(r[0]))
                 t="1110"+C_ins_0.get(r[0])
             if r[0] in C_ins_1:
                 #print(C_ins_1.get(r[0]))
                 t="1111"+C_ins_1.get(r[0])
             if r[1] in Jump:
                 t=t+"000"+Jump.get(r[1])
             w.write(t+"\n")
         else :                         #d=c;j
             r=parse("{}={};{}",l) 
             if r[1] in C_ins_0:
                 #print(C_ins_0.get(r[1]))
                 t="1110"+C_ins_0.get(r[1])
             if r[1] in C_ins_1:
                 #print(C_ins_1.get(r[1]))
                 t="1111"+C_ins_1.get(r[1])
             if r[0] in Dest:
                 t=t+Dest.get(r[0])
             if r[2] in Jump:
                 t=t+Jump.get(r[2])
             w.write(t+"\n")

w.close()