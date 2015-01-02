##1. Write a function to print the keys of an input dictionary.
mydic1= dict()

mydic1['sandra']=12
mydic1['paolo']=56
mydic1['asmaa']=17
mydic1['torta']=7

def func1 (mydic):
    for key in mydic:
        print ("the key name is", key)


##2. Write a function to print the values in a dictionary.
       
def func2 (mydic):
    for key in mydic:			# use key to create a loop in the dictionary 
        print ("the value is", mydic[key])  # print the value of the key
       

##3. Write a function that accepts a dictionary of people as name, age, and
##returns the average age of the people.

def funcaverage(mydic):
    average=0
    for key in mydic:
        average+= mydic[key]/ len(mydic) # add every value of the dictionary and divide by the lenght of it
    return average
    
    
##4. dictionary of months as month name, number of days
##and prints a nicely formatted calendar of all the days of the months of the year.

dicyear= {
    'January': 31, 'February': 28,'Mars': 31, 'April': 30, 'May': 31, 'June': 30,
    'July': 31, 'August': 31,'September': 30, 'October': 31,'November': 30,'December': 31 # dictionary of number of day 
    }
months = [
    'January', 'February', 'Mars', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December' ] # create a list, because dicitonary are not iterable in sequence


days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] # list of the day to use in the printing 

def show (dic, m , d):
    count = 0 
    for i in months:            # because the dictionary work with key, I need a list to pick th
                                # element in order.                               
        for month in dic:   # search in the dictionary.
            if i == month:
                print( month, end='\n') # print month and return line
                for i in d:   # read the days in sequence
                    print ( i, end='\t') # print days with space
                print(end='\n')			 #return line 
                print('\t'*(count%len(d)), end='') # put empty spaces before the first day for months 
                for i in range(dic[month]):
                                                                     #if the month before not end on Sunday. 
                    print ( i+1, '\t', end= '\n' *((count%len(d)+1)//len(d))) # empty space after last day
                    count+= 1  #+1 because if not begin with 0

                print(2 *'\n')
               

#show(dicyear, months, days)
 

##5. Write a function that given a value and a dictionary, returns the key associated with
##that value in the dictionary (this is called inverse lookup).
def func5(searchvalue, mydic):
    for key in mydic:         # do a loop to search in the dictionary
        if mydic[key] == searchvalue: # confront value of the dicitonary withe the value given
            return key

#func5(12, mydic1)

##6. Write a function that given a value and a dictionary, returns the number of times that
##value occurs in the dictionary.
def func6(value, dic):
    count =0
    for key in dic:                   
         if dic[key] == value:  # like in the func5 but we add count to count every time it occurs
            count += 1
    return count

#func6(31, dicyear)       
    
##7. Write a function that prints the keys of a dictionary in increasing order of the associated
##values in the dictionary (Assume key, value for the dictionary where value is integer.)


def func7 (dic):
    lisst=[]
    for key in dic:
        a = d[key]
        lisst.append(a)
    lisst.sort()  # using list sort.
    for i in range (len(lisst)):
        for k in dic:
            if dic[k] == lisst[i]:
                print (k)
               

        
##8. An inventory dictionary countains as key the name of an item as a string (e.g. laptop model), and as value a
##list in the format [Number, Price].
##Write a function to update number of the inventory items, based on the user input that requests one or more items.

inventory= { 'laptop': [1, 800], 'tomatos': [ 23, 2], 'shirt': [10, 99], 'oranges':[100, 3],
             'potatos' : [34, 5]                                                                               
    }

def func8 (inv):
    while ('end'):
        name= input('pick an object from the inventory:')
        if name in inv:
                # to pick the number of the object in the inventory
            a = inv[name]
            if name in inv:
                
                # to tell the user how many of the object is currently there
                print("there are %s " % (a[0]))
            newnumber = input('type the new number of the object:')

            # to change the number of the object
            while not newnumber.isdigit():
                print('Invalid entry. Please try again')
                newnumber = input('type the new number of the object:')
            a[0] = newnumber
        elif name == 'end':
            print('Bye, see you an other time')
            return inv
        else:
            print('Error, Try Again')
            
        
            

##9. Populate dictionary from a file. Each line of the file contains a (key, value) pair separated
##by space.
def func9 (text):
    f=open(text,'r')
    lines = f.readlines() # read the lines in the file 
    dic = {}
    for i in lines:
        a = i.strip().split(' ')  # delete space , and split when we have a space
        print (a)
        dic[(a[0])] = a[1]
    print(dic)

#func9('introtext7.txt')   
##10. Use a dictionary to represent a one-week agenda. The dictionary should support events
##being scheduled
##for days of the week, starting time, and duration.

event = [['start','duration'], ['start','duration'], ['start','duration'], ['start','duration']]

week  = {'Mon':event[0], 'Tue':event[2], 'Wed':event[0], 'Thu':event[1],
     'Fri':event[2], 'Sat':event[1], 'Sun':event[1]}


 
##11. Given the dictionary in the previous question, write a function to detect conflicting
##events.
we ={'Mon':[[8, 2],[14, 4]], 'Tue':[[12, 2],[15, 6]],
     'Wed':[[13, 4]], 'Thu':[[3, 8],[14, 4]],
     'Fri':[[15, 5]], 'Sat':[[12, 8]], 'Sun':[[13, 3]]
     }

def func11 (we, d):
    nest = we[d]
    count= 0
    print (nest)
        # since the times are stored as a nested list in the agenda:
    for event in nest:
        if event[0] < count:
            return('Conflicting events exist')
        count = event[0] + event[1]
    return ('No conflicts between events')

##12. Create a dictionary to represent a sample of the iTunes music database.

play ={'Relief Next to Me': ['3:02','Tegan and Sara', 'The Con', 'Rock','4 stars','32'],
       'The Con': ['3:31','Tegan and Sara', 'The Con', 'Rock','5 stars','45'],
       'Hop a Plane': ['1:52','Tegan and Sara', 'The Con', 'Rock','4.5 stars','34'],
       }

##13. Create a dictionary to represent a people database.

person = {'Name': ['Gender','Age','Nationality',
                   'Eye color','Weight','Work',
                   'Marital Status','Country of Residence']}

