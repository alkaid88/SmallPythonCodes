jotta = 1000000000000000000000000.0
zetta = 1000000000000000000000.0
eksa  = 1000000000000000000.0
peta  = 1000000000000000.0
tera  = 1000000000000.0
giga  = 1000000000.0
mega  = 1000000.0
kilo  = 1000.0
hekto = 100.0
deka  = 10.0
unit  = 1.0
decy  = 0.1
centy = 0.01
mili  = 0.001
mikro = 0.000001
nano  = 0.000000001
piko  = 0.000000000001
femto = 0.000000000000001
atto  = 0.000000000000000001
zepto = 0.000000000000000000001
jokto = 0.000000000000000000000001

def get_help():
    print ('Welcome to HELP of this simple calculator.\nTo use it as intended follow the instructions and input only valid values\nInput:\n\tvalue (float) - scalar that is multiplier of unit\n\tprefix (string) - is something like kilo, kilo, mini, nano, giga\n\tunit (string) - its just a string you can make something up')

def change_prefix_to_number(prefix):
    if prefix == 'yotta':
        return float(10**24)
    elif prefix == 'zetta':
        return float(10**21)
    elif prefix == 'exa':
        return float(10**18)
    elif prefix == 'peta':
        return float(10**15)
    elif prefix == 'tera':
        return float(10**12)    
    elif prefix == 'giga':
        return float(10**9)
    elif prefix == 'mega':
        return float(10**6)
    elif prefix == 'kilo':
        return float(10**3)
    elif prefix == 'hecto':
        return float(10**2)   
    elif prefix == 'deka':
        return float(10**1)
    elif prefix == 'deci':
        return float(10**(-1))
    elif prefix == 'centi':
        return float(10**(-2))
    elif prefix == 'mili':
        return float(10**(-3))
    elif prefix == 'micro':
        return float(10**(-6))
    elif prefix == 'nano':
        return float(10**(-9))   
    elif prefix == 'pico':
        return float(10**(-12))
    elif prefix == 'femto':
        return float(10**(-15))
    elif prefix == 'atto':
        return float(10**(-18))
    elif prefix == 'zepto':
        return float(10**(-21))
    elif prefix == 'yocto':
        return float(10**(-24))
    else:
        return 1.0


def change_prefix(value, prefix, to_prefix):
    return value * prefix / to_prefix
