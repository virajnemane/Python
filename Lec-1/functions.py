name="Nilesh"
age=37
weight=65.2
skill=["Linux","Python","Ansible"]
detail={"Name" : "Nilesh", "age" : 37, "Skill" : skill }

#type function to check datatype
print(type(name))
print(type(age))
print(type(weight))
print(type(skill))
print(type(detail))

#Mathamatical function with int and float
x1 = 2
x2 = 90
 
print(x1+x2)    #addition for int/float is arithmatic addition
print(x1-x2) 
print(x1*x2)
print(x1/x2)    #division, in python 3 the o/p is always a float number
print(x1//x2)   #python 2 equivalent division, only intger part is returned
print(x1**x2)   #exponent
print(x1%x2)    #module/reminder

x1 = x1 + 9     #self addition
x1 += 9         #self addition, same as above expression

#Functions with String 
z = 'my 2nd python class, and it was too long.'

z           #print the whole string

#slicing formula is z[start_pos:end_pos+1:stepsize]
#index in python starts with 0.
z[5:10]      #print subpart of the string, the end-pos is exlcuded!!, 10th position is exluded
z[3:]       #read all the way through from position 3
z[:6]       #read first 6 characters
z[1:10:2]   #skip one character in between
z[::-1]     #to reverse the string

len(z)      #length of the string

z.find('2',4)  #return the position where the substring is found, returns -1 if not found
z.index('2',4) #return the position where the substring is found, throws exception if not found

z.startswith('my 2nd')  #True   - checks whether the string starts with substring
z.startswith('my 2ndd') #False
z.endswith('.')         #True   - checks whether the string ends with substring

z.upper()       #convert to upper case
z.lower()       #convert to lower case
z.count(' ')    #count how many times substring appears in the origional string
print("No of words are : " + str((z.count(" ") + 1)))   #how many words there in the string
z.replace('it','that')  #replaces the old string with new string, here 'it' is replaced by 'that'


z = '#####   my 2nd python class, and it was too long.'
z = z.strip('#').strip(' ').strip('my')     #removes the leading and trailing spaces(default)/the character you specified


#print()    - single line comment, anything after # is ignored

''' block comment/multiline comment
print("asdfsdfsdf","safasdf","24234",sep=",",end="")
print("uwirwueirow")
print("shfjasdhfjsdh")
'''

#make sure you follow the indentation, there is no choice. All statements must start from column 1.
#to define the block use tab/spaces for indentation like below example

if z.startswith('#'):
                i = 1
                j = 0
                k = True


