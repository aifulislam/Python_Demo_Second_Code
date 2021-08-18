#Meta Characters-----------
'''
. = dot any character
^& = ^ $
* = 0 or more
+ = 1 or more
? = o or 1
{and}
'''
import re
pettern = r"stud..nt"
if re.match(pettern,"studeint"):
    print("Matched1")

import re
pettern = r"t.ach..r"
if re.match(pettern,"teachier"):
    print("Matched2")

import re
pettern = r"^stud..t$"
if re.match(pettern,"student"):
    print("Matched3")

import re
pettern = r"a*"
if re.match(pettern,"satudetnt"):
    print("Matched4")

import re
pettern = r"a*"
if re.match(pettern,"arifa"):
    print("Matched5")

import re
pettern = r"(ab)*"
if re.match(pettern,"arifb"):
    print("Matched6")

import re
pettern = r"a*b"
if re.match(pettern,"abrifa"):
    print("Matched7")

import re
pettern = r"a+"
if re.match(pettern,"arifa"):
    print("Matched8")

import re
pettern = r"a+b"
if re.match(pettern,"abrifa"):
    print("Matched9")

import re
pettern = r"Ar(-)?if"
if re.match(pettern,"Arif"):
    print("Matched10")

import re
pettern = r"a{1,3}$"
if re.match(pettern,"aaa"):
    print("Matched11")

