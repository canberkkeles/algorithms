def karatsubaMultiplication(x, y):

    """
    x*y = (10 ^ n)*ac + (10^(n/2) * (ad+bc)) + bd
    where
    x = (10 ^ (n/2)*a) + b
    y = (10 ^ (n/2)*c) + d
    """

    if (x < 10) or (y < 10): # base case is if one of the numbers is single digit
        return x*y


    """
    Use string manipulation to split the numbers
    into two parts
    """
    num1 = str(x)
    num2 = str(y)

    n = max(len(num1), len(num2))
    nHalf = int(n / 2)

    # numbers are divided from least significant digit, as proposed by aes in stackoverflow
    # You get x = 46 and y = 152 so n_2 = 1 and str_x[:n_2] = '4' 
    # and str_y[:n_2] = '1'. These are not offset by the same amount!

    a, b= int(num1[:-nHalf]), int(num1[-nHalf:]) # divide the numbers into parts
    c, d= int(num2[:-nHalf]), int(num2[-nHalf:]) # divide the numbers into parts

    ac = karatsubaMultiplication(a,c) # calculate a*c in equation
    bd = karatsubaMultiplication(b,d) # calculate b*d in equation
    step3 = karatsubaMultiplication((a+b),(c+d)) # calculate (a+b)*(c+d), to avoid recursive calls
    gaussTrick = step3 - ac - bd # use a trick to get (ad+bc)

    return (ac*10**(2*nHalf)) + (gaussTrick*10**(nHalf))+bd # return the equation.