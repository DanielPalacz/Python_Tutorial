# Float, a floating point number.
# Example: 3.14

# 1. PI up to 65 significant digits is:
#    3.14159265358979323846264338327950288419716939937510582097494459230
#    How many floating point positions can python handle?

# 2. There are 60 gold coins and 19 people.
#
#    If we divide it in python, we get:
#    $ python3 -c "print(60 / 19)"
#    3.1578947368421053

#    If we divides it in node js, we get:
#    $ node -pe "60 / 19"
#    3.1578947368421053

#    If we divides it using "bc" command in unix/linux, we get:
#
#    $ echo "100 / 19" | bc -l
#    3.15789473684210526315
#
#    If we try the same division in Perl:
#    $ perl -e "print 60 / 19"
#    3.15789473684211

#    Which one is right?
