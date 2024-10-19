import re
import signal

EXAMPLES = ["M1 1AA", "M60 1NW", "CR2 6XH", "DN55 1PT", "W1A 1HQ", "EC1A 1BB", "ST7 9HV"]


def postcode_validator(postcode):
    '''Checks the inputted postcode and 
    returns True if it matches the regex.'''
    
    if len(postcode) > 10:
        return False
    
    # regex pattern provided by Kris(2008) in https://shorturl.at/NHRDd    
    pattern = re.compile(r"[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][ABD-HJLNP-UW-Z]{2}")     
    return bool(pattern.search(postcode))

# signal_handler function provided by rik.the.vik(2008)
def signal_handler(signum, frame):
    raise Exception("Timed out!")

signal.signal(signal.SIGALRM, signal_handler)
signal.alarm(5)   # Five seconds

try:

    for postcode in EXAMPLES:
        print(postcode_validator(postcode))
    
except Exception:
    print("Timed out!")
    
# References
# Kris(2008) in https://shorturl.at/NHRDd
# rik.the.vik(2008) in https://shorturl.at/vVsGn    