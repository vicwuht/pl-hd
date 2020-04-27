print("Let's practice everything.")
print('You\'d need to konw \'bout escaps with \\ that do:',end='')
print("\n newline and \t tabs.")

peom = """
    The loverly world
with loginc so firmly planted
cannot discer5n
    the needs of love
nor comprehend passion from intuition
and requires an explanation

             where there is none.
"""
print("-"*12)
print(peom)
print("-"*12)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, ctates = secret_formula(start_point)
print("with a starting point of : {}".format(start_point))
print(f"we'd have {beans} beans, {jars} jars, and {ctates} crates.")

start_point = start_point / 10
formula = secret_formula(start_point)
print(type(formula))
print("we'd have {} beans, {} jars, and {} crates.".format(*formula))
