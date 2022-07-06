"""
"metropolisa" -> "m(e(t(r(o(p)o)l)i)s)a"
"metropolis"  -> "m(e(t(r(op)o)l)i)s"
"""

def set_brackets(text: str) -> str:
    if len(text) < 3:
        return text
    return text[0] + "("+ set_brackets(text[1:-1]) + ")" + text[-1]

print(set_brackets("metropolisa"))

# *********************************************************************************************************







