#Regular expressions---------
#match,search,find ----------all
#match----------
import re
pattern = r"color"
if re.match(pattern,"color red is  color, I love red Color"):
    print("Match")
else:
    print("Not Match")

#search---------
import re

pattern = r"Arif"
if re.search(pattern,"who is a student,Arif learn python programming language"):
    print("Match")
else:
    print("Not Match")

#Find all-----

import re
pattern = r"color"
print(re.findall(pattern,"This red is  red color, I love red color"))

#More on search fuction----------

import re
pattern = r"color"
text = "This red is red color, I love red color"
match = re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())
