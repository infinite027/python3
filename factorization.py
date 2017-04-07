import _thread
result = []

def factorization(number, *args):
      i = number
      print("Number is "+str(i))
      while i>1:
            i-=1
            if number%i == 0 and i !=1:
                  factorization(i)
                  factorization(number/i)
                  break
            elif number%i==0 and i ==1:
                  result.append(number)
      return result

def main():
      try:
            inputed = int(input("Input a number"))
            factorization(inputed)
      except ValueError:
            print("Input type wrong. Please  check again.")

if __name__ == "__main__":
      main()
      print(result)            
