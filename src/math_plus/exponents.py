class Exponent:

    def __init__(self, base, exponent) -> None:
        self.base = base
        self.exponent = exponent

    def calculate(self) -> float:
        return self.base ** self.exponent

    def __str__(self) -> str:
        return f"{self.base}^{self.exponent}"
    
def product(*args) -> float:
    """Calculate the product multiplying exponents. (limited to 2 exponents atm)\n
    Formulas:\n
    a^m * a^n = a^(m+n)\n
    a^m * b^m = (a*b)^m\n
    a^m * b^n = a^m * b^n\n
    Parameters:\n
    args (str): Exponents in the form of base^exponent.\n
    Returns: The product multiplying two exponents\n
    """

    bases = []
    exponents = []

    if len(args) != 2:
        raise ValueError("This function only supports 2 exponents.")

    for exponent in args:

        components = str(exponent).split("^")

        if len(components) == 2:
            base = float(components[0])
            exp = float(components[1])
        
        bases.append(base)
        exponents.append(exp)
    
    if bases[0] == bases[1]:
        # If the bases are the same, add the exponents a^m * a^n = a^(m+n)
        result = bases[0] ** (exponents[0] + exponents[1])
    elif exponents[0] == exponents[1]:
        # Otherwise, multiply the bases and raise to the common exponent a^m * b^m = (a*b)^m
        result = (bases[0] * bases[1]) ** exponents[0]
    else:
        # If the bases and exponents are different, return the product of the bases raised to their respective exponents
        result = (bases[0] ** exponents[0]) * (bases[1] ** exponents[1])    

    return result
