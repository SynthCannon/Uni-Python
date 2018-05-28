class Y:
    """
    Mathematical function for the vertical motion of a ball.
    4 Methods:
    constructor (v0): set initial velocity v0.
    value(t): compute the height as function of t.
    formula ( ) : p r i nt out the formula f o r the he i ght .
    Attributes:
    v0: the initial velocity of the ball (time 0).
    g: acceleration of gravity (fixed).
    Usage:
    >>> y = Y( 3 )
    >>> position1 = y.value(0.1)
    >>> position2 = y.value(0.3)
    >>> print y.formula()
    v0*t-0.5*g*t**2; v0=3
    """
    def __init__(self,v0):
        self.v0 = v0
        self.g = 9.81
    def value(self,t):
        return self.v0*t-0.5*self.g*t**2
    def formula(self):
        return 'v0*t-0.5*g*t**2; v0 = %g' % self.v0

instance=Y(2)
print instance.formula()
print instance.value(2)
