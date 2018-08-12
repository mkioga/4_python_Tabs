
# ===========
# 4_Tabs.py:
# ===========

# Python indentation
# The indentation in python (where print starts) shows that the line is part of that code chunk

for i in range(1, 5):
    print("No# {:2} squared id {:3} and Cubed is {:4}".format(i, i**2, i**3))
    print("This line is also part of this code")
    print()

# We can change the indent tab width in intellij using
# File > Settings > Editor > Code Style > Python > Then select tab size and indent size.
# Defailt is 4 for each.


# To fix formatting errors, go to
# Code > Reformat code
