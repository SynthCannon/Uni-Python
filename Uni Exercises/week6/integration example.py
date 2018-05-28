from scipy.integrate import quad

# syntax
#scipy.integrate.quad ( func , a , b , args=() )

#func: function A Python function or method to integrate.
# a : Lower l imi t o f i n t e g r a t i o n ( use ??s c ipy . i n t e g r a t e . I n f f o r ??i n f i n i t y ) .
# b : Upper l imi t o f i n t e g r a t i o n ( use s c ipy . i n t e g r a t e . I n f f o r +i n f i n i t y ) .
# args : tuple , opt i ona l ext r a arguments to pas s

def func(x , n ,w):
    return n*x**w

iprod, err = quad( func , 0 , 1 , args=(2,3) )
print iprod # the evaluation of the integral of 2*x**3 between x=0 and x=1
print err #pr in t e r r # the nume r i cal unc e r t a inty in the i n t e g r a l