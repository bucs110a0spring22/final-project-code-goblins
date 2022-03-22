import pygame
#import your controller

def main():
    pygame.init()
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()

mylist = []
for i in range(4):
  listnum = int(input("Please enter a number: "))
  mylist.append(listnum)
for i in range(4):
  print(mylist[i])
mylist[0], mylist[3] = mylist[3], mylist[0]
print("")
for i in range(4):
  print(mylist[i])