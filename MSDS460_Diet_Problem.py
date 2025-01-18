#!/usr/bin/env python
# coding: utf-8

# In[23]:


from pulp import LpVariable, LpProblem, LpStatus, value, LpMinimize

#I chose bananas, chicken breasts, cheerios (dry), string cheese, and green peas as the five foods.
Bananas = LpVariable("Bananas", 0, None)
CBS = LpVariable("Chicken Breasts", 0, None)
CO = LpVariable("Cheerios", 0, None)
SC = LpVariable("String Cheeses", 0, None)
GPeas = LpVariable("Green Peas", 0, None)

#This is a minimization probem.
#The goal is to minimize cost while satisfying nutritional constraints.
prob = LpProblem("problem", LpMinimize)

#Seven constraints come from the U.S. Food and Drug Administration.
#I added an 8th constraint so that I limit calories and do not gain weight.
prob += 1*Bananas + 50*CBS + 100*CO + 190*SC + 300*GPeas >= 35000 #(mg) - sodium
prob += 90*Bananas + 130*CBS + 70*CO + 90*SC + 60*GPeas >= 14000 #(calories) - energy
prob += 90*Bananas + 130*CBS + 70*CO + 90*SC + 60*GPeas <= 21000 #(calories) - energy
prob += 1.1*Bananas + 25*CBS + 2*CO + 7*SC + 3*GPeas >= 350 #(grams) - protein
prob += 0*Bananas + 0*CBS + 2*CO + 0.1*SC + 0*GPeas >= 140 #(mcg) - vitamin d
prob += 5*Bananas + 10*CBS + 60*CO + 210*SC + 20*GPeas >= 9100 #(mg) - calcium
prob += 0.26*Bananas + 0.4*CBS + 6.3*CO + 0.1*SC + 0.7*GPeas >= 126 #(mg) - iron
prob += 362*Bananas + 370*CBS + 130*CO + 50*SC + 130*GPeas >= 32900 #(mg) - potassium

#The total cost of food eaten is the sum of all price per servings of each food multiplied by the servings consumed.
prob += 0.26*Bananas + 1.92*CBS + 0.47*CO + 0.42*SC + 0.68*GPeas

#Solve Problem
status = prob.solve()
print(f"Problem 1: Partial servings allowed")
print(f"status={LpStatus[status]}")
print(f"----------------------------")

#Print results
for variable in prob.variables():
    print(f"{variable.name} = {variable.varValue}")

print(f"Total Cost = {value(prob.objective)}")
print(f"")
print(f"")
print(f"")
print(f"")
print(f"")
print(f"")

#Same code as above, but I altered the lower bounds of the variables so that each food must be eaten once.
Bananas = LpVariable("Bananas", 1, None)
CBS = LpVariable("Chicken Breasts", 1, None)
CO = LpVariable("Cheerios", 1, None)
SC = LpVariable("String Cheeses", 1, None)
GPeas = LpVariable("Green Peas", 1, None)

#This is a minimization probem.
#The goal is to minimize cost while satisfying nutritional constraints.
prob = LpProblem("problem", LpMinimize)

#Seven constraints come from the U.S. Food and Drug Administration.
#I added an 8th constraint so that I limit calories and do not gain weight.
prob += 1*Bananas + 50*CBS + 100*CO + 190*SC + 300*GPeas >= 35000 #(mg) - sodium
prob += 90*Bananas + 130*CBS + 70*CO + 90*SC + 60*GPeas >= 14000 #(calories) - energy
prob += 90*Bananas + 130*CBS + 70*CO + 90*SC + 60*GPeas <= 21000 #(calories) - energy
prob += 1.1*Bananas + 25*CBS + 2*CO + 7*SC + 3*GPeas >= 350 #(grams) - protein
prob += 0*Bananas + 0*CBS + 2*CO + 0.1*SC + 0*GPeas >= 140 #(mcg) - vitamin d
prob += 5*Bananas + 10*CBS + 60*CO + 210*SC + 20*GPeas >= 9100 #(mg) - calcium
prob += 0.26*Bananas + 0.4*CBS + 6.3*CO + 0.1*SC + 0.7*GPeas >= 126 #(mg) - iron
prob += 362*Bananas + 370*CBS + 130*CO + 50*SC + 130*GPeas >= 32900 #(mg) - potassium

#The total cost of food eaten is the sum of all price per servings of each food multiplied by the servings consumed.
prob += 0.26*Bananas + 1.92*CBS + 0.47*CO + 0.42*SC + 0.68*GPeas

#Solve Problem
status = prob.solve()
print(f"Problem 2: Partial servings allowed and all foods must be eaten once")
print(f"status={LpStatus[status]}")
print(f"----------------------------")

#Print results
for variable in prob.variables():
    print(f"{variable.name} = {variable.varValue}")

print(f"Total Cost = {value(prob.objective)}")
print(f"Additional money spent = ${round(value(prob.objective) - 104.731607,2)}")
print(f"")
print(f"")
print(f"")
print(f"")
print(f"")
print(f"")

#Same code as above, but the servings must be a whole number.
Bananas = LpVariable("Bananas", 1, None, "Integer")
CBS = LpVariable("Chicken Breasts", 1, None, "Integer")
CO = LpVariable("Cheerios", 1, None, "Integer")
SC = LpVariable("String Cheeses", 1, None, "Integer")
GPeas = LpVariable("Green Peas", 1, None, "Integer")

#This is a minimization probem.
#The goal is to minimize cost while satisfying nutritional constraints.
prob = LpProblem("problem", LpMinimize)

#Seven constraints come from the U.S. Food and Drug Administration.
#I added an 8th constraint so that I limit calories and do not gain weight.
prob += 1*Bananas + 50*CBS + 100*CO + 190*SC + 300*GPeas >= 35000 #(mg) - sodium
prob += 90*Bananas + 130*CBS + 70*CO + 90*SC + 60*GPeas >= 14000 #(calories) - energy
prob += 90*Bananas + 130*CBS + 70*CO + 90*SC + 60*GPeas <= 21000 #(calories) - energy
prob += 1.1*Bananas + 25*CBS + 2*CO + 7*SC + 3*GPeas >= 350 #(grams) - protein
prob += 0*Bananas + 0*CBS + 2*CO + 0.1*SC + 0*GPeas >= 140 #(mcg) - vitamin d
prob += 5*Bananas + 10*CBS + 60*CO + 210*SC + 20*GPeas >= 9100 #(mg) - calcium
prob += 0.26*Bananas + 0.4*CBS + 6.3*CO + 0.1*SC + 0.7*GPeas >= 126 #(mg) - iron
prob += 362*Bananas + 370*CBS + 130*CO + 50*SC + 130*GPeas >= 32900 #(mg) - potassium

#The total cost of food eaten is the sum of all price per servings of each food multiplied by the servings consumed.
prob += 0.26*Bananas + 1.92*CBS + 0.47*CO + 0.42*SC + 0.68*GPeas

#Solve Problem
status = prob.solve()
print(f"Problem 3: Servings must be whole number and all foods must be eaten once")
print(f"status={LpStatus[status]}")
print(f"----------------------------")

#Print results
for variable in prob.variables():
    print(f"{variable.name} = {variable.varValue}")

print(f"Total Cost = {value(prob.objective)}")
print(f"Additional money spent compared to problem 1 = ${round(value(prob.objective) - 104.731607,2)}")
print(f"Additional money spent compared to problem 2 = ${round(value(prob.objective) - 106.28995,2)}")
print(f"")
print(f"")
print(f"")
print(f"")
print(f"")
print(f"")

