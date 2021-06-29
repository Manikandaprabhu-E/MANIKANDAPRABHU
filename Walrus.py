# heros= list()
# while True:
#  getinput = input('Enter the hero names: ')
#  if getinput == "q":
#      break
#  heros.append(getinput)

myheros=list()

while (getinput := input("Enter the superheros name: ") ) != "q":
    myheros.append(getinput)
print(myheros)