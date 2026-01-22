"""
Legacy module for data processing - INTENTIONALLY MESSY!
This is for Week 4 refactoring exercise.

DO NOT use this code as an example! It's intentionally bad for educational purposes.
"""

import sys
import os
from datetime import datetime

# Global variables (anti-pattern!)
d = []
u = []
cache = {}

def p(x):
    """Process data - unclear name, unclear purpose"""
    r = []
    for i in x:
        if i:
            # Nested logic without clear purpose
            if type(i) == dict:
                if 'id' in i:
                    if i['id'] not in cache:
                        cache[i['id']] = i
                        r.append(i)
                    else:
                        # Update existing
                        cache[i['id']].update(i)
                        r.append(cache[i['id']])
            elif type(i) == str:
                r.append({'data': i, 'ts': datetime.now()})
            else:
                r.append(i)
    return r

def calc(a, b, op='add'):
    """Calculator with magic strings"""
    if op == 'add':
        return a + b
    elif op == 'sub':
        return a - b
    elif op == 'mul':
        return a * b
    elif op == 'div':
        # No error handling for division by zero!
        return a / b
    elif op == 'pow':
        return a ** b
    else:
        return None

# TODO: Refactor this function - it's doing too many things
def process_user_data(data):
    """This function does everything - loads, validates, transforms, saves"""
    # No input validation
    results = []
    errors = []
    
    # Deeply nested loops
    for item in data:
        if item:
            if 'user' in item:
                user = item['user']
                if 'name' in user:
                    if 'email' in user:
                        # Email validation (but wrong!)
                        if '@' in user['email']:
                            # More nesting
                            if 'age' in user:
                                if user['age'] > 0:
                                    if user['age'] < 150:
                                        # Transform data
                                        processed = {
                                            'n': user['name'].upper(),
                                            'e': user['email'].lower(),
                                            'a': user['age'],
                                            't': datetime.now().isoformat()
                                        }
                                        
                                        # Side effect - modifying global!
                                        u.append(processed)
                                        results.append(processed)
                                    else:
                                        errors.append('Age too high')
                                else:
                                    errors.append('Age must be positive')
                            else:
                                errors.append('Age missing')
                        else:
                            errors.append('Invalid email')
                    else:
                        errors.append('Email missing')
                else:
                    errors.append('Name missing')
            else:
                errors.append('User key missing')
        else:
            errors.append('Empty item')
    
    # Return multiple types (anti-pattern)
    if errors:
        return None, errors
    else:
        return results, None

# Duplicated code
def get_user_by_id(user_id):
    """Find user by ID"""
    for user in u:
        if 'id' in user:
            if user['id'] == user_id:
                return user
    return None

def get_user_by_email(email):
    """Find user by email - nearly identical to above!"""
    for user in u:
        if 'e' in user:
            if user['e'] == email:
                return user
    return None

def get_user_by_name(name):
    """Find user by name - more duplication!"""
    for user in u:
        if 'n' in user:
            if user['n'] == name.upper():  # Case sensitivity issue
                return user
    return None

# No error handling
def save_data(filename):
    """Save data to file"""
    f = open(filename, 'w')  # File not closed properly!
    f.write(str(u))
    f.write('\n')
    f.write(str(d))

def load_data(filename):
    """Load data from file"""
    f = open(filename, 'r')
    content = f.read()
    # Using eval is a security vulnerability!
    data = eval(content)
    return data

# Unused function
def obsolete_function():
    """This function is no longer used but wasn't removed"""
    pass

# Magic numbers everywhere
def calculate_price(base_price, quantity):
    """Calculate price with discounts"""
    if quantity > 100:
        discount = 0.15
    elif quantity > 50:
        discount = 0.10
    elif quantity > 20:
        discount = 0.05
    else:
        discount = 0
    
    price = base_price * quantity * (1 - discount)
    
    # Magic numbers for tax calculation
    if base_price > 1000:
        tax = price * 0.08
    else:
        tax = price * 0.06
    
    # More magic numbers
    shipping = 10 if price < 50 else 5 if price < 100 else 0
    
    total = price + tax + shipping
    
    return total

# Commented out code (should be removed)
# def old_process_data(x):
#     for i in x:
#         if i:
#             print(i)
#     return x

# TODO: Remove this debug code before production
def debug_print_all():
    """Debug function that shouldn't be in production"""
    print("Users:", u)
    print("Data:", d)
    print("Cache:", cache)
    print("System info:", sys.version)

# Inconsistent naming conventions
class DataProcessor:
    """Process data - but this class is barely used"""
    
    def __init__(self):
        self.Items = []  # PascalCase variable
        self.item_count = 0  # snake_case variable
        self.itemTotal = 0  # camelCase variable
    
    def AddItem(self, item):  # PascalCase method
        """Add item to processor"""
        self.Items.append(item)
        self.item_count += 1
        if 'value' in item:
            self.itemTotal += item['value']
    
    def getTotal(self):  # camelCase method
        """Get total"""
        return self.itemTotal
    
    def reset_all(self):  # snake_case method
        """Reset everything"""
        self.Items = []
        self.item_count = 0
        self.itemTotal = 0

# No documentation
def f(x, y, z=None):
    if z:
        return [i for i in x if i > y and i < z]
    return [i for i in x if i > y]

# SQL injection vulnerability (if this were connected to a DB)
def find_user_sql(username):
    """Find user using SQL - VULNERABLE!"""
    query = f"SELECT * FROM users WHERE username = '{username}'"
    # In real code, this would execute the query
    return query

# TODO: All of the above needs refactoring!
# Suggested improvements:
# 1. Meaningful variable and function names
# 2. Single Responsibility Principle
# 3. Proper error handling
# 4. Remove duplicated code
# 5. Remove magic numbers
# 6. Fix security vulnerabilities
# 7. Add type hints
# 8. Add comprehensive documentation
# 9. Remove unused code
# 10. Consistent naming conventions
