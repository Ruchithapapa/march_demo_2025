#---> Symbol or keyword that performs an  operation on one or more operands.
#---> Value or bariable acted upon by an operator to produce a result.

num_1 = 15
num_2 = 15
result = num_1+num_2
print(result)


# Subtraction: Subtracts the right operand from the left operand.
num_1 = 10
num_2 = 5
result = num_1-num_2
print(result)

num_1 = 10
num_2 = 5
result = num_1*num_2
print(result)


# Exponentiation(**): Raises the base (left operand) to the power of the exponent(right operand)
num_1 = 4
num_2 = 3
result = num_1 ** num_2
print(f"base is {num_2} and expo is {num_1} final result {result}")
print(result)

# Division(/): Divides the left operand by the right operand.
num_1 = 10
num_2 = 3
result = num_1/num_2
print(result)

# Floor Division(//): returns the quotient of the division, discarding the fractional part.
num_1=10
num_2=3
result=num_1//num_2
print(result)


# Modules(%): Returns the remainder of the division of the left operand by the right operand.
num_1=10
num_2=5
result=num_1%num_2
print(result)
print(f"num_1 value is {num_1} and num_2 value is {num_2} and result is {result}")

num_1 = 10
num_1 +=5
num_1=num_1+5
print(num_1)

num_1 = 10
num_1 *= 5
num_1=num_1*5
print(num_1)


#product_cost = 5000
#product_cost_2 = 5000
#print(product_cost == product_cost_2)
#print(product_cost < product_cost_2)
#print(product_cost > product_cost_2)
#print(product_cost <= product_cost_2)
#print(product_cost >= product_cost_2)
#print(product_cost != product_cost_2)


sample = True
print(not(sample))

sample =[1,2,3]
print(id(sample))
a = sample
print(id(a))
sample_2 = [1,2,3]
print(id(sample_2))
print(sample is a)
print(sample is sample_2)
print(sample is not sample_2)


fruits = ["apples", "banana", "oranges","grapes"]
print("guava" in fruits)
print("guava" not in fruits)



# Discount:
product_cost = 10000
discount = 5
result = product_cost * (discount/100)
product_cost -= result  #eg---> prod = prod-result
print(f"discount given {discount}% and final discount {result} and total cost after discount {product_cost}")
print(5<3 or 2==2)


user = "pythonlife"
print("p" in user)
num_1 = int(input("enter something"))
num_2 = int(input("enter something"))
print(num_1+num_2)
    