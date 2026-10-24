
"""
Python Modules and Imports
Codgnan Class Practice
"""

import sys
import types

# Create example modules inside this single file
biology = types.ModuleType("biology")
physics = types.ModuleType("physics")
calculator = types.ModuleType("calculator")


# ==================== BIOLOGY MODULE ====================

def dna():
    return "DNA: Carries genetic information."


def genes():
    return "Genes: Units of heredity that control traits."


class Biology:
    pass


biology.dna = dna
biology.genes = genes
biology.Biology = Biology
biology.b1 = "DNA"
biology.b2 = "Protein"
biology.__all__ = ["dna", "genes", "Biology", "b1", "b2"]


# ==================== PHYSICS MODULE ====================

def newtonsfirst():
    return (
        "First Law (Inertia): Objects remain at rest or in "
        "uniform motion unless acted on by an external force."
    )


def newtonssecond():
    return "Second Law (F = ma): Force equals mass multiplied by acceleration."


def newtonsthird():
    return "Third Law: Every action has an equal and opposite reaction."


class Physics:
    pass


physics.newtonsfirst = newtonsfirst
physics.newtonssecond = newtonssecond
physics.newtonsthird = newtonsthird
physics.Physics = Physics
physics.p1 = "Einstein"
physics.p2 = "Nikola Tesla"
physics.__all__ = [
    "newtonsfirst", "newtonssecond", "newtonsthird",
    "Physics", "p1", "p2"
]


# ==================== CALCULATOR MODULE ====================

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


class Calculator:
    pass


calculator.add = add
calculator.sub = sub
calculator.mul = mul
calculator.div = div
calculator.Calculator = Calculator
calculator.c1 = 101
calculator.c2 = 201

# Names available through: from calculator import *
calculator.__all__ = ["add", "c1"]


# Register modules for import statements in this file
sys.modules["biology"] = biology
sys.modules["physics"] = physics
sys.modules["calculator"] = calculator


# ==================== 1. SINGLE IMPORT ====================

print("\n--- Single Import ---")

import calculator

print(calculator.add(20, 10))
print(calculator.sub(20, 10))
print(calculator.mul(20, 10))
print(calculator.div(20, 10))

c = calculator.Calculator()
print(calculator.c1)
print(calculator.c2)


# ==================== 2. MULTIPLE IMPORT ====================

print("\n--- Multiple Import ---")

import biology, physics, calculator

print(biology.dna())
b = biology.Biology()
print(biology.b1)

print(calculator.add(20, 10))
c = calculator.Calculator()
print(calculator.c1)

print(physics.newtonsfirst())
p = physics.Physics()
print(physics.p1)


# ==================== 3. MODULE ALIAS ====================

print("\n--- Module Alias ---")

import biology as bio
import physics as phy
import calculator as calc

print(bio.genes())
print(bio.b1)

print(phy.newtonsfirst())
print(phy.p1)

print(calc.add(20, 10))
print(calc.c1)


# ==================== 4. SINGLE MEMBER IMPORT ====================

print("\n--- Single Member Import ---")

from calculator import add
from biology import genes
from physics import newtonsfirst

print(add(20, 10))
print(genes())
print(newtonsfirst())


# ==================== 5. MULTIPLE MEMBER IMPORT ====================

print("\n--- Multiple Member Import ---")

from calculator import add, sub
from physics import newtonsfirst, newtonssecond
from biology import dna

print(add(20, 10))
print(sub(20, 10))

print(newtonsfirst())
print(newtonssecond())

print(dna())


# ==================== 6. MEMBER ALIAS ====================

print("\n--- Member Alias ---")

from calculator import add as a
from physics import newtonsfirst as nf
from biology import genes as g

print(a(20, 10))
print(nf())
print(g())


# ==================== 7. STAR IMPORT AND __all__ ====================

print("\n--- Star Import ---")

from physics import *
from calculator import *
from biology import *

# Biology members
print(dna())
print(genes())

b = Biology()
print(b1)
print(b2)

# Physics members
print(newtonsfirst())
print(newtonssecond())
print(newtonsthird())

p = Physics()
print(p1)
print(p2)

# Calculator members selected by __all__
print(add(20, 10))
print(c1)

# Try changing calculator.__all__ to:
# calculator.__all__ = ["add", "c1"]
# Then test the star import again.


# ==================== 8. __name__ STATEMENT ====================

if __name__ == "__main__":
    print("\nHi")
    print("Welcome to Python Modules and Imports practice.")


# ==================== 9. IMPORT ERROR ====================

# Uncomment these lines one at a time to study import errors.
# from chemistry import periodictable
# from calculator import power
