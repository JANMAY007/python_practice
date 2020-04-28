# and, or, not are having same meaning as of english dictionary
good_credits = True
good_income = False
if(good_credits and good_income):
    print("eligible")
else:
    print("not eligible")
if(good_credits or good_income):
    print("eligible")
else:
    print("not eligible")
if(good_credits and not good_income):
    print("eligible")
else:
    print("not eligible")