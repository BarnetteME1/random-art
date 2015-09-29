import random
import math

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.

num_list = ["42.94011220646039", "5.646665186128161", "36.181321872403686",
"73.588459320803684", "47.46616486634289", "9.28960463563688", "92.13071170982583",
"67.2557323771716", "32.13986413171649", "23.053905506440437"]
math_sin = ["math.cos(", "math.sin(", "math.tan("]
math_op = ["+", "-", "*"]
x_y = ["x", "y"]
pi_e = ["math.pi", "math.e"]
def sven():
    z = math.tan((x**2 + y**2)*randint())
    return eval(z)

def ramona():
    w = "lambda x, y: abs(" + random.choice(math_sin) + random.choice(x_y) + random.choice(math_op) + random.choice(num_list) + ")" + random.choice(math_op) + "abs(" + random.choice(x_y) + ")" + "** abs(" + random.choice(x_y) + "))"
    x = "lambda x, y: abs(" + random.choice(math_sin) + random.choice(x_y) + random.choice(math_op) + "(" + random.choice(math_sin) + random.choice(num_list) + "))))"
    y = "lambda x, y: abs(" + random.choice(math_sin) + random.choice(x_y) + random.choice(math_op) + random.choice(x_y) + "**" + "abs(" + random.choice(num_list) +")))"
    z = "lambda x, y: abs(" + random.choice(math_sin) + random.choice(num_list) + random.choice(math_op) + random.choice(x_y) + "))"
    return eval(sven())

def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    expr = sven()
    return expr


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)
