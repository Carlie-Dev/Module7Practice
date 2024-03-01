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