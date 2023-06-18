import itertools

class FunctionalDependency:
    def __init__(self, left,right):
        self.left = ''.join(sorted(str(left)))
        self.right = ''.join(sorted(str(right)))
    def __str__(self):
     return self.left + '->' + self.right

class Relation:
    def __init__(self, attributes, listOfFO):
        self.attributes = attributes
        self.listOfFO = listOfFO
        self.keys = findPrimaryKeys(listOfFO, attributes)
    def __str__(self):
        output = "Attributes : "
        output += str(self.attributes)
        output += "\nFunctional Dependencies :  "

        for element in self.listOfFO:
            output += str(element) + " "

        output += "\nKeys : "
        for element in self.keys:
            output += str(element) + " "
        return output

def isFunctionalDependencyInList(functionalDependency, list):
    for element in list:
        if element.left == functionalDependency.left and (functionalDependency.right in element.right):
            return True

    return False 

def isKeyInList(key, list):

    key = ''.join(sorted(str(key)))
    for element in list:
        temp = element.left + element.right
        temp = ''.join(sorted(str(temp)))

        if key in str(temp):
            return True

    return False

def has_all_chars(bigger, smaller):
    return all(char in bigger for char in smaller)

def isSuperKey(keys,FO):
    for key in keys:
        key = ''.join(sorted(str(key)))
        if has_all_chars(FO.left, key):
            return True
    return False

def remove_chars(base, string2):
    for char in string2:
        base = base.replace(char, '')
    return base

##############################################

def findPrimaryKeys(listOfFO, attributes):
    st = [] # all possible combinations
    candidates = [] # stores primary key candidates

    # stores all possible combinations in st
    for i in range(1, len(attributes)):
        temp = itertools.combinations(attributes, i)
        st += temp

    for tup in st:
        tup = ''.join(tup)
        # break if there is smaller tup in candidate list
        if(candidates and len(candidates[0]) < len(tup)):
            break

        tup_set = set() # create temp set
        for fo in listOfFO: 
            if set(fo.left).issubset(set(tup)): # add right side if left side is in the key
                tup_set = tup_set.union(set(fo.right)) # makes union between two right sides
        tup_str = ''.join(sorted(tup_set)) # values of the right side getted using list of FD

        if tup_str == "": # if empty skip other code
            continue
        tup_str2 = tup_str + tup # adding left side to the right
        tup_str2 = ''.join(set(tup_str2)) # removes duplicates from str
        count = 0

        # while count < 100:
        for fo in listOfFO:
                if set(fo.left).issubset(set(tup_str2)):
                    tup_str2 = tup_str2 + fo.right
                    tup_str2 = ''.join(set(tup_str2))
            #count += 1

        if set(attributes).issubset(set(tup_str2)) and len(attributes) == len(tup_str2): # if this is primary key, add it to list candidates
            candidates.append(tup)

    return candidates






