# Program to write
# read file 


def read():
    dic={}
    f = open('friends.txt','r')
    lines = f.readlines()
    for i in range (len(lines)):
        lines[i] = lines[i].split('|')
        for j in range(len(lines[i])):
            lines[i][j] = lines[i][j].strip()
            
        
    for friends in lines:
        if friends[0] not in dic:
            dic[(friends[0])] = []
        dic[(friends[0])].append(friends[1])
    return dic
    

dic = read()
print (dic)

# fun person with most number of friends
def most(d):
    m = ['',0]
    for person in d:
        if len(d[person]) > m[1]:
            m = [person, len(d[person])]
    return m

print(most(dic))

# fun average number of friends
def average(d):
    count = 0
    for person in d:
        count += len(d[person])
    return count/ len(d)
print(average(dic))
        

# fun accepts two names and determines if the 2nd is a friend of the 1st
def friends(dictionary, friend1, friend2):
    return friend2 in dictionary[friend1]
print(friends(dic, 'Sammy Riggs', 'Melodie Tomson'))

