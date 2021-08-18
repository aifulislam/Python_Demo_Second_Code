#Exception Handling (part-1)-----------

try:
    list = [10,0,7]
    result = list[0]/list[1]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Dividing is not possible")

finally:
    print("program Ending here")
print("Successful")

#Exception Handling (part-1)-----------

try:
    list = [10,0,30]
    result = list[0] / list[3]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Dividing by zero is not possible")
except IndexError:
    print("Index Erorr")
finally:
    print("Successful")


