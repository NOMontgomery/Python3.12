# STRINGS1:
# S1. Think of 3 variables and assign (in one line or separate lines) string values to them, each not less
#   than 8 characters long. Display their values.
# S2. Assign to the fourth variable the portion of the first variable from the second character to the one character
#   before the last character. Display the result.
# S3. Add two single quotes and two double quotes to the end of the second variable. Display the resultant value.
# S4. Display the result of comparison of the 3rd character in third variable to the 7th character in the
#   second variable.
# S5. Run in Debug (Shift-F9), trace this program step by step (F8). Watch how variable
#   values change in the Variables panel.
# S6. Modify all your print function calls to show description of the value. E.g.:
#   print(xyz) should become print(“xyz=\”“ + xyz + “\””)
str1, str2, str3, = 'raekwon!!', 'nyals678+', 'montgomery'

print("all my allias: \"" + str1, str2, str3 + "\"!")
# s2
str4 = str1[1:-1]
print("this is the fourth", str4)
print("str1[1:7] + fourth = \"" + str1[1:7] + "\"")
# s3
# print("all my allias: \"" + str2 + "\"!", \'' + str2 +'\')
# str2 = str2 + "\'\'\"\""
str2 += "\'\'\"\""
print(str2)
# print('nyals678'''"")
# print("this is double = \"" + str2 + "\"")
# print('this is single = \'' + str2 + '\'')
# print('this is both = \'')
# print(''\'str2'\'')
# s4
print("comparing character", str3[2] == str2[6], str3[2], str2[6])
print('this is test', "\"" + str1 + '\'')
