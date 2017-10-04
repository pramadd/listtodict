name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

#(this print as key and value of given data)

#  new_dict= dict(zip(name,favorite_animal))
#  print new_dict
#  return new_dict

#make_dict(name,favorite_animal)
  
def make_dict(arr1, arr2):
  new_dict = {}
  arrLen = len(arr1)
  for i in range(0,arrLen):
    key_list = arr1[i]
    value_list = arr2[i]
    new_dict[key_list] = value_list
  print new_dict
  return new_dict

make_dict(name,favorite_animal)