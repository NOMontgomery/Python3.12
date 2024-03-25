# NUMBERS1
# N1. Think of 3 variables and assign (in one line or separate lines) 3 integer numbers to  them. Display their values.
# N2. Do the same for 3 float-point variables with unique names and assign floating-point values to them.
#   Display their values.
# N3. Change values of the variables like this and then display their values:
#   N3.1. The first variable:
#     INT - should equal to the sum of the second and the third
#     FLOATING - negate the value meaning: subtract to equal 0
#   N3.2. The second variable:
#     INT - should be reduced by 100;
#     FLOAT - should equal to twice the value of the third variable, minus the value of the first:
#   N3.3. The third variable:
#     INT - increment its value (means  “add 1”);
#     FLOAT - divide its value by 3
# N4. Run in Debug (Shift-F9), trace this program step by step (F8). Watch how variable values change
#   in the Variables panel.
# 1
a = 1
b = 2
c = 3
# 2
var1, var2, vae3, = 10, -13, 37
# print("values are", var1, var2, vae3)
# print('second Values are', a, b, c)
# n2
var1 = var2 + vae3
print('Values at 3.1 are:', var1, var2, vae3)
# n1 floating point
print('floating point  negate', var1 - var1, var2 - var2, vae3 - vae3)
# n3
var2 = var2 - 100
# floating 2
print("floating point 2:", var2 * vae3 - var1)
# print("values are", var1, var2, vae3)
# # var2 -= 100
print("values are", var1, var2, vae3)
# n4
vae3 += 1
print("values are4:", var1, var2, vae3)
# floating 4
vae3 /= 3
print("values are floating point", var1, var2, vae3)
