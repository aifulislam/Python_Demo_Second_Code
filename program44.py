#Exception Handling (part-2)-----------

try:
    num1 = int(input("Enter First number : "))
    num2 = int(input("Enter Second number : "))

    result = num1/num2
    print(result)
except (ValueError,IndexError,ZeroDivisionError):
    print("Any where have Erorr")
finally:
    print("Thanks!!!")
print("Successful")

#Exception Handling (part-2)-----------

def vote(age):
    if age < 18:
        raise ValueError("Invalid Voter")
    return "You are allowed to vote"

try:
    print(vote(19))
    print(vote(17))

except ValueError as e:
    print(e)

#Exception Handling (part-2)-----------
def vote(age):
    if age < 18:
        raise ValueError("Invalid Voter")
    return "You are allowed to vote"

try:
    print(vote(19))
    print(vote(17))

except ValueError as e:
    print(e)
