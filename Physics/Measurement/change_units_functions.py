def get_help():
    print ('\nWelcome to HELP of this simple calculator.\nTo use it as intended follow the instructions and input only valid values\nInput:\n\tvalue (float) - scalar that is multiplier of unit\n\tprefix (string) - is something like kilo, mini, nano, giga\n\tunit (string) - its just a string you can make something up')

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
