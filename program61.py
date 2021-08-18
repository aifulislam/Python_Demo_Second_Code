#Search And Replace--------

import re
pattern = r"colour"
text1 = "My favorite colour is red.I love blue colour as well."
text2 = re.sub(pattern,"color",text1)
print(text2)

import re
pettern = r"Ariful Islam"
text1 = "My name is Ariful Islam.I am a student"
text2 = re.sub(pettern,"Tamim Iqbal",text1)
print(text2)

import re
pettern = r"student"
text1 = "I am ariful Islam and I am a student."
text2 = re.sub(pettern,"Teacher",text1)
print(text2)
