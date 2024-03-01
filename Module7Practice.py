webUrl = 'https://my.otc.edu'

#Get the middle part of a url
#the first number is inclusive. The first number is nonincludive.
print(webUrl[8:14])

#negative indexes allow you to count from the end of the string aswell
print(webUrl[8:-4])

#Set up data for pretty string output.
dog_1 = ['Richard','mutt', '15','Large']
dog_2 = ['Scraps', 'Golden', '2', 'Medium']
dog_3 = ['Rowdy', 'Lab/Boxer','8','Medium']


#Setup headings for output
headings = ['Name','Bread','Age','Size'] #7-9-3-6
dog_list = [headings,dog_1, dog_2, dog_3]

#Setup the output for our data
#print(f'{dog_1[0]:8}{dog_1[1]:10}{dog_1[2]:4}{dog_1[3]}:7')

#Another string trick
print('-'*28)

#Set up the output for our data using loop
for list in dog_list:
    print(f'{list[0]:8}{list[1]:10}{list[2]:4}{list[3]:6}')

print('-'*28)

#Better method
#New list example

# length_list = []

# for list in dog_list:
#     temp_list = []


#Replace an item in a string
myString = 'apple corn hotDog pizza apple corn apple apple pizza hotDog'
print(myString)

print(myString.replace('apple','donut'))

print(myString.replace('apple','donut',1))

#replaces all of them still
print(myString.replace('apple','donut',-1))

#Find an item in a string
print(myString.find('corn',1))
print(myString.find('corn',10,20))
#^ will return an error value as a -1

#Gets the ammount a substring appears in a string
print(myString.count('apple'))