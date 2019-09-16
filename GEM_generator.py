#!/usr/bin/env python3

print("\n", "\t", "Welcome!", "\n")

print("The GEM model has up to three types of interacting variables.")
print("These variables include genotype 'G', environment 'E', and the microbiome 'M'")
print("The model may be expanded to include any number of interactions")
print("To generate your own GEM model, please follow the prompts below","\n")

# input("Press Enter to continue...")

# How many (interacting) Genotype treatments (this could be used for intercropping )
G = input("Enter the number of interacting genotypes: ")

# How many (interacting) Environment treatments
E = input("\nEnter the number of interacting environments: ")

# How many (interacting) Microbiom treatments
M = input("\nEnter the number of interacting microbiomes: ")

G = int(G)
E = int(E)
M = int(M)

# First enter the number of 
if(G > 1):
	G_variables = ["G" + str(i) for i in range(1,(G+1))]
else:
	G_variables = "G"

if(E > 1):
	E_variables = ["E" + str(i) for i in range(1,(E+1))]
else:
	E_variables = "E"

if(M > 1):
	M_variables = ["M" + str(i) for i in range(1,(M+1))]
else:
	M_variables = "M"
	
print("\n", "Below are your interacting variables:", "\n")
print("Genotype: ", G_variables)
print("Environment: ", E_variables)
print("Microbiome : ", M_variables)

print("\n\n", input("Press ENTER to view your model."), "\n")
# 

# print(type(M_variables))
# All the variables must be in a list form in order to work in the combinations function

all_variables = list(G_variables) + list(E_variables) + list(M_variables)

# print(type(all_variables))

# print(M_variables.split(M_variables,-1))

from itertools import combinations 
  
# Get all combinations of [G, E, M] 

for i in range(1,len(all_variables)+1):
	comb = combinations(all_variables, i)
# Print the obtained combinations 
	for i in list(comb): 
		print(i) 


