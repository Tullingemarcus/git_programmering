
def missingnumber():
    number = [1,7,9,3]
    number.sort()
    x = number[-1]
    y = x * (x+1)/2
    z = y - sum(number)
    print(z)



if __name__ == "__main__":
    missingnumber()