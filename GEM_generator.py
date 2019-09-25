#!/usr/bin/env python3

print("\n", "\t", "Welcome!", "\n")

print("The GEM model has up to three types of interacting variables.")
print("These variables include genotype 'G', environment 'E', and microbiome 'M'")
print("The model may be expanded to include any number of interactions")
print("To generate your own GEM model, please follow the prompts below","\n")

# input("Press Enter to continue...")
num_variables = None

if num_variables is None:
 print("\nWarning: Please limit the model to 10 or less total variables")
 G = int(input("\nEnter the number of interacting genotypes: "))
 E = int(input("\nEnter the number of interacting environments: "))
 M = int(input("\nEnter the number of interacting microbiomes: "))
 num_variables = G + E + M
while num_variables > 10:
 print("\nWarning: You have entered ",num_variables," variables.")
 print("A model with this many variables would have",2**num_variables,"terms.")
 print("Please limit the model to 10 or less total variables")
 G = int(input("\nEnter the number of interacting genotypes: "))
 E = int(input("\nEnter the number of interacting environments: "))
 M = int(input("\nEnter the number of interacting microbiomes: "))
 num_variables = G + E + M
 
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
	
print("\n", "Below are the interacting variables that will be in your model:", "\n")
print("Genotype: ", G_variables)
print("Environment: ", E_variables)
print("Microbiome : ", M_variables, "\n")
print("In total:", 2**num_variables, "terms are in your model\n")

# Add all variables into a single list
all_variables = list(G_variables) + list(E_variables) + list(M_variables)

# Create the output name
output_name = '_'.join(all_variables) + ".txt"

print("Your output is found in the following file : ", output_name, "\n")

from itertools import combinations 
  
# Get all combinations of [G, E, M] 
for i in range(1,len(all_variables)+1):
	comb = combinations(all_variables, i)
# Print the obtained combinations 
	if i < len(all_variables):
		for j in list(comb): 
			print((''.join(j)), end = " + ", file=open(output_name, "a"))
		print("\n", end = "", file=open(output_name, "a"))
	else:
		for j in list(comb): 
			print((''.join(j)), end = " \n ", file=open(output_name, "a"))

print("\n", file=open(output_name, "a"))


