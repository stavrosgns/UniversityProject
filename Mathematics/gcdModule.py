"""
This module calculate with different ways the Greatest Common Divisor (gcd).
"""

"""
@Author: Stavros Gkounis
@Date: 17/10/17
@Project: gcd [Discrete Mathematics]
"""

"""
|Theorem 1| :
According to the theorem:
Let a,b be integers and a >= b >= 0 (without loss of generality).
Using the division with remaider, we define the integer numbers r0, r1, ... , rl+1 and
                                                                q1, q2, ... , ql ,
where l >=0, According to:

             r0 = a
             r1 = b
             r0 = r1 q1 + r2     (1) [i=1]
             r1 = r2 q2 + r3     (2) [i=2]
             r2 = r3 q3 + r4     (3) [i=3]
             r3 = r4 q4 + r5     (4) [i=4]
                .
                .
                .
                .
            ri-1 = ri qi + ri+1
                .
                .
                .
            rl-2 = rl-1 ql-1 + rl
            rl-1 = rl ql          [rl+1 = 0]

qi = floor(ri-1 / ri)
"""

"""
|Theorem 2|:
Consider the integers a,b, (r0, r1, ... , rl-1) and (q1, q2, ... , ql) in the theorem 1.
We also define the integers (s0, s1, ... , sl+1) and (t1, t2, ... , tl+1) as:
                            s0 := 1,  t0 := 0
                            s1 := 0,  t1 := 1
and for i = 1, ... , l,
                            si+1 := si-1 - si qi
                            ti+1 := ti-1 - ti qi
"""



def gcdIterative(a,b):
    """
    This function implements the gcd iterative algorithm (Euclidean algorithm).
    It is easy to understand the algorithm if you observe the (1),(2),(3),(4) in the theorem 1.
    """
    r0 = a
    r1 = b
    d = None # this variable contains the answer we want. The gcd(a,b).
    while(r1 != 0):
        r2 = r0 % r1
        r0,r1 = r1,r2
        d = r0
    return d


def gcdRecercive(a,b):
    """
    This function implements the gcd recercive algorithm (Euclidean algorithm).
    """

    if(b == 0 ):
        return a
    else:
        aux = a % b
        return gcdRecercive(b, aux)

def  xgcdIterative(a,b):
    """
    This is the implementation of the extended Euclidean iterative Algorithm according to the theorem 2.
    """
    r0 = a ; r1 = b
    s0 = 1 ; t0 = 0
    s1 = 0 ; t1 = 1
    d = None

    while(r1 != 0):
        q  = r0 // r1
        r2 = r0 % r1
        nextS = s0 - (s1 * q)
        nextT = t0 - (t1 * q)
        r0, r1, s0, s1, t0, t1 = r1, r2, s1, nextS, t1, nextT  #  this line of code will be understandable, if we observe the formulas of the theorem 2.
        d = r0
    return d,s0,t0

def xgcdRecercive(a,b):
    """
    This is the implementation of the extended Euclidean recercive algorithm.
    """
    if(b == 0):
        return (a,1,0)

    d, x ,y = xgcdRecercive(b, a % b)
    aux = x - ((a // b) * y)
    return d, y, aux



if __name__ == "__main__":
    print("The gcd(100,35) in iterative mode is: {}".format(gcdIterative(100,35)))
    print("The gcd(100,35) in recercive mode is: {}".format(gcdRecercive(100,35)))
    print("The xgcd(1281,243) in iterative mode is: {}".format(xgcdIterative(1281,243)))
    print("The xgcd(1281,243) in recercive mode is: {}".format(xgcdRecercive(1281,243)))
else:
    print("The gcdModule is imported successfully.")
