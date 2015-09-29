def blue_duck():
p = "lambda x, y:" + random.choice(math_sin) + random.choice(num_list) + random.choice(math_op) + random.choice(math_sin) + random.choice(pi_e) + random.choice(math_op) + random.choice(math_sin) + random.choice(num_list) + random.choice(math_op) + random.choice(math_sin) + random.choice(pi_e) + random.choice(math_op) + random.choice(math_sin) + random.choice(pi_e) + random.choice(math_op) + random.choice(x_y) + ")" + random.choice(math_op) + random.choice(x_y) + "))" + random.choice(math_op) + random.choice(math_sin) + random.choice(pi_e) + random.choice(math_op) + random.choice(x_y) + ")))"
q = "lambda x, y:" + random.choice(math_sin) + random.choice(e_pi) + random.choice(math_op) + random.choice(math_sin) + random.choice(pi_e) + random.choice(math_op) + random.choice(math_sin) + random.choice(e_pi) + random.choice(math_op) + random.choice(math_sin) + random.choice(pi_e) + random.choice(math_op) + random.choice(math_sin) + random.choice(pi_e) + random.choice(math_op) + random.choice(x_y) + ")" + random.choice(math_op) + random.choice(x_y) + "))" + random.choice(math_op) + random.choice(math_sin) + random.choice(pi_e) + random.choice(math_op) + random.choice(x_y) + ")))"
r = "lambda x, y: abs(" + random.choice(math_sin) + random.choice(num_list) + random.choice(math_op) + random.choice(X_Y) + "))"
s = "lambda x, y: x * y" + random.choice(["+", "-", "*"]) + "abs(y) ** abs(x)"
t = "lambda x, y: abs(" + random.choice(["math.cos(", "math.sin(", "math.tan("]) + "x)" + random.choice(["+", "-", "*"]) + random.choice(["(math.cos(", "(math.sin(", "(math.tan("]) + "y)))"
u = "lambda x, y: abs(" + random.choice(["math.cos(", "math.sin(", "math.tan("]) + random.choice(["x", "y"]) + random.choice(["+", "-", "*"]) + random.choice(["x)", "y)"]) + "**" + "abs(" + random.choice(["x", "y"]) +"))"
v = "lambda x, y: abs(abs(x) ** abs(math.sin(random.random())) + (abs(y) ** abs(math.sin(x * random.random()))))"
w = "lambda x, y: abs(math.cos(x * math.sin(y * math.tan(x * math.pi + math.cos(random.random())))))"
x = "lambda x, y: abs(math.cos(math.sin(math.tan(x + y))))"
y = "lambda x, y: abs(abs(x + y * math.cos(x + y)) ** abs(math.sin(x + y)))"
z = "lambda x, y: abs((abs(x) ** abs(y + math.tan(x))) * math.sin(abs(x) ** abs(math.cos(y))))"
  return eval(random.choice([a, b, c, d, e, f, g, h]))

random.choice(["math.cos(", "math.sin(", "math.tan("])
random.choice(["+", "-", "*"])
random.choice(["x", "y"])
