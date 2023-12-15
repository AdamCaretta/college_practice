import numexpr as ne

exp = "2 + 2"

output = ne.evaluate(exp).item()

print(output)
