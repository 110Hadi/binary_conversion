
##Input
denary = int(input("Enter a number: "))
binary = ''

while denary > 0:
  binary += str(denary % 2)
  denary = denary // 2
          
##Reversing String
binary = binary[::-1]

##Output For Overflow Error
if len(binary) > 8:
  print('''Error Type: Overflow 
   Register Limit: 8-Bits''')
else: ##Always Output In An *-Bit Format
  binary = '{:>08}'.format(binary)

print(binary)