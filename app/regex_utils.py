#Regex & Luhn check utils
#Created By: Deepak Singh 
#Created on: 05-Oct-2025
#Modified On: 07-Oct-2025
#Version: 1.0.0.0
#---------------------------------------------

import re

REGEX_PATTERNS = {
    "Email": (re.compile(r"\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b"),0.98),
    "Phone": (re.compile(r"\b(?:\+?91[-\s]?|0)?[6-9]\d{9}\b"),0.95),
    "Account": (re.compile(r"\b\d{12,18}\b"),0.90),
    "CreditCard": (re.compile(r"\b(?:\d[ -]*?){13,19}\b"),0.95),
    "Amount": (re.compile(r"(?:₹|\$|USD|INR|GBP|EUR|€|£)\s?[\d,]+(?:\.\d+)?",re.I),0.94),
    #Add this new one:
    "SSN": (re.compile(r"\b\d{3}-\d{2}-\d{4}\b"), 0.96)
}

def luhn_check(num):
    s = re.sub(r"[^\d]", "", num)
    if not (13 <= len(s) <= 19): return False
    digits = list(map(int, s))
    odd = digits[-1::-2]
    even = digits[-2::-2]
    total = sum(odd) + sum(sum(divmod(2*d,10)) for d in even)
    return total % 10 == 0
