# in python we don't need to declare data type
# just enter variable name , then equal sign and then value of variable

roll = 33
firstName = "Mujahid" #can be double quotation
lastName = 'Emon' #or can be single quotation
isPresent = True #bool value start with capital letter either True or False
presentRate = 87.5


print(roll)
print(firstName)
print(lastName)
print(isPresent)
print(presentRate)


"""
if we want to know the dataType of a variable then syntax is 'print(type(variableNAme))'

 """

print(firstName + lastName)  #concat

text = f"This is {lastName} with ID {roll} has present rate {presentRate}%" #this is called f string
print(text)