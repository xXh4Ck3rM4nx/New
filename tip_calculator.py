def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    #replaces the $ from the number
    d = d.replace('$', '')
    #return the float
    return float(d)
    
def percent_to_float(p):
    #replaces the percent sign from the number with ''
    p = p.replace('%', '')
    #returns the float
    return float(p) * 0.01

#splits too literaly
main()
    