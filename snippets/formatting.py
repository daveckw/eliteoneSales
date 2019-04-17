# Python format() function example  
# Variable declaration  
val = 10  
# Calling function  
print("decimal: {0:d}".format(val)); # display decimal result  
print("hex: {0:x}".format(val));     # display hexadecimal result  
print("octal: {0:o}".format(val));   # display octal result  
print("binary: {0:b}".format(val));  # display binary result  

val = 100000000  
# Calling function  
print("decimal: {:,.2f}".format(val)); # formatting float value  
print("decimal: {:.2%}".format(56/9)); # formatting percentile value  