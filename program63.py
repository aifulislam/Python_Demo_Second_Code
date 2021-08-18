#Character Class--------------

import re
pettern = r"[aeiou]"
if re.match(pettern,"astudent"):
    print("Matched1")

import re
pettern = r"[A-Z][a-z][0-9]"
if re.match(pettern,"Ya8student"):
    print("Matched2")

