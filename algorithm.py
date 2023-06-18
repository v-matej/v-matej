import values

def doThirdNormalForm(relation):
    ro = []

    for tempFunctionDep in relation.listOfFO:
        if values.isFunctionalDependencyInList(tempFunctionDep, ro) is False:
            ro.append(tempFunctionDep)

    for tempKey in relation.keys:
        if values.isKeyInList(tempKey, ro) is True:
            return ro
        
    ro.append(relation.keys[0])

    return ro

def doBCNormalForm(relation):
    ro=''
    ro+=relation.attributes
    RO_FO=[]

    for tempFunctionDep in relation.listOfFO:
        if values.has_all_chars(ro,tempFunctionDep.left) and values.has_all_chars(ro,tempFunctionDep.right):
            if values.isSuperKey(relation.keys,tempFunctionDep) is False:
                for sign in tempFunctionDep.right:
                    ro=ro.replace(sign,'')
                RO_FO.append(tempFunctionDep)

    for element in relation.keys:
        if values.has_all_chars(ro,element) is True:
            ro=values.remove_chars(ro,element)
            
            tempFO = values.FunctionalDependency(element,ro)
            RO_FO.append(tempFO) 
            return RO_FO
    
    
    tempFO = values.FunctionalDependency(relation.keys[0],ro)   
    RO_FO.append(tempFO)
    return RO_FO

# TEST

tempFO = []
tempFO.append(values.FunctionalDependency("A","B"))
tempFO.append(values.FunctionalDependency("C","B"))
tempFO.append(values.FunctionalDependency("B","E"))
tempFO.append(values.FunctionalDependency("I","J"))
tempFO.append(values.FunctionalDependency("H","G")) 
tempFO.append(values.FunctionalDependency("A","D"))
tempFO.append(values.FunctionalDependency("D","F"))
tempFO.append(values.FunctionalDependency("A","H")) 


tempAttr = "ABCDEFGHIJ"


relacija1 = values.Relation(tempAttr, tempFO)

print(relacija1)
print()

print("3. N F : ")
ro = doThirdNormalForm(relacija1)
print("\nRO : ")
for element in ro:
    print(element)

print("\nBCNF N F : ")

RO_FO=doBCNormalForm(relacija1)
print("\nRO : ")
for element in RO_FO:
    print(element)



