import os

def getSize():
      while True:
            input1 = input("input the size of the screen in format of x*y")
            size = input1.split("*")
            try:
                  sum = int(size[0])+int(size[1]);
            except ValueError:
                  nope = True;
            else:
                  nope = False;
            if len(size)==2 and nope == False:
                  return size
                  break
            else:
                  print("please double check the values")

def makeArray(dimension):
      result = []
      for ySize in range(dimension[1]):
            newLine = []
            for xSize in range(dimension[0]):
                  newLine.append("#")
            result.append(newLine)
      return result

def getInput(name):
      while True:
            userInput = input("please enter the "+name)
            try:
                  temp = int(userInput)
            except ValueError:
                  print("please try again")
            else:
                  return int(userInput)
                  break

def clr():
      os.system('cls')

def main():
      size = getSize()
      xPosition = getInput("x position")
      yPosition = getInput("y position")
      size[0] = int(size[0])
      size[1] = int(size[1])
      screen = makeArray(size)
      screen[yPosition][xPosition] = "~"
      output = ""
      clr()
      for column in screen:
            for element in column:
                  output = output+element
            os.system('echo '+output)
            output = ''
            os.system('echo:')
      main()
            
if __name__ == "__main__":
      main()
      os.system("@echo")
      clr()
            
      
