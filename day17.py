# Import required modules
import math
import random
import sys
import platform
import collections
import itertools
from datetime import datetime, date, timedelta

#Math module
print('------------Math Module----------------')
print('Square root of 25:', math.sqrt(25))
print('Power (2^3):', math.pow(2, 3))
print('Value of PI:', math.pi)
print('Ceiling of 4.3:', math.ceil(4.3))
print('Ceiling of -4.3:', math.ceil(-4.3))
print('Floor of 4.8:', math.floor(4.8))
print('Floor of -4.8:', math.floor(-4.8))
print('Factorial of 5:', math.factorial(5))
print('GCD of 12 and 18:', math.gcd(12, 18))
print('LCM of 12 and 18:', math.lcm(12,18))
print('Sine of 45 radians:', math.sin(45))
print('Cosine of 45 radians:', math.cos(45))
print('Tangent of 45 radians:', math.tan(45))
print('Degrees of 45 radians:', math.degrees(45))
print('Radians of 45 degrees:', math.radians(45))
print()
print()

# Random Module
print('-------------Random Module--------------')
print('Random float between 0 and 1 including:', random.random())
# print(random.random(1,10))    #random will not take any argument
print('Random float from x to y including:', random.uniform(1,10))
print('Random integer from x to y including:', random.randint(1, 100))
print('Random integer from 1 to 20 insteps of 2:', random.randrange(1,21,2))
#random with list
numbers = [10, 20, 30, 40, 50]
print('Random choice:', random.choice(numbers))
random.shuffle(numbers)
print('Shuffled list:', numbers)
print('Random sample:', random.sample(numbers, 3))
print()
print()


# Sys module
print('----------------Sys Module----------------')
print('Python version:', sys.version)
print('Python executable:', sys.executable)
print('Number of command-line arguments:', len(sys.argv))
print()
print()

# Platform Module
print('--------------Platform Module--------------')
print('Operating system:', platform.system())
print('Machine:', platform.machine())
print('Processor:', platform.processor())
print('Python implementation:', platform.python_implementation())
print()
print()

# Collections Module
print('---------------Collections Module----------------')
# Counter
words = ['rakesh', 'adhithya', 'rakesh', 'charan', 'adhithya', 'rakesh']
counter = collections.Counter(words)
print('Word count:', counter)
# Most common item
print('Most common:', counter.most_common(1))
print('Most common:', counter.most_common(2))
print()
# # DefaultDict
student_marks = collections.defaultdict(list)
student_marks['Alice'].append(90)
student_marks['Alice'].append(85)
student_marks['Bob'].append(78)
print('Student marks:', dict(student_marks))
print()
# # NamedTuple
Student = collections.namedtuple('Student', ['name', 'age', 'course'])
student = Student('John', 20, 'Python')
print('Student tuple:', student)
print('Student name:', student.name)
print('Student age:', student.age)
print('Student course:', student.course)
print()
print()

# Itertools module
print('--------------Itertools Module--------------')
items = ['A', 'B', 'C']
# Permutations
print('Permutations:')
permutations = itertools.permutations(items)
print(list(permutations))
# Combinations
print('Combinations:')
combinations = itertools.combinations(items, 2)
print(list(combinations))
# Product
print('Cartesian product:')
cproduct = itertools.product([1, 2], ['A', 'B'])
print(list(cproduct))
print()
print()

# Datetime Module
print('------------------Datetime Module-------------------')
# Current date and time
now = datetime.now()
print('Current date and time:', now)
# Current date
today = date.today()
print('Today\'s date:', today)
# Format date and time
print('Formatted date:', now.strftime('%d-%m-%Y'))
print('Formatted time:', now.strftime('%H:%M:%S'))
# Create a specific date time
birthday = datetime(2000, 5, 15, 19, 50, 50)
print('Example birthday:', birthday)
# Add days
future_date = today + timedelta(days=7)
print('Date after 7 days:', future_date)
# Subtract days
past_date = today - timedelta(days=7)
print('Date 7 days ago:', past_date)