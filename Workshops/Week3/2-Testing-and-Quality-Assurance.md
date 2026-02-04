# Testing and Quality Assurance with GitHub Copilot

**Duration:** 30-45 minutes  
**Format:** Presentation with hands-on examples  
**Objective:** Master test generation, coverage improvement, and test optimisation techniques using GitHub Copilot.

---

## Session Overview

Testing is a critical part of software development where Copilot excels. From generating unit tests by analysing source code to converting tests between frameworks, Copilot can significantly accelerate your testing workflow.

**What you'll learn:**
- Generate comprehensive unit tests for new and existing code
- Ensure consistent test coverage across projects
- Optimise tests with parameterisation and data-driven approaches
- Convert tests between different frameworks

---

## 1. Unit Test Generation

### Why Use Copilot for Testing?

| Challenge | How Copilot Helps |
|-----------|-------------------|
| Writing boilerplate test code | Generates test structure, setup, and teardown |
| Identifying edge cases | Suggests test scenarios you might miss |
| Maintaining test coverage | Quickly generates tests for new code |
| Understanding testing patterns | Demonstrates framework-specific best practices |

### Test Generation Strategies

#### Strategy 1: Function-First Testing

Provide the function, ask for tests:

**Source Code:**
```javascript
function add(a, b) {
    return a + b;
}
module.exports = { add };
```

**Prompt:**
```text
Write Jest tests for the add function with different input scenarios including positive numbers, negative numbers, zero, and decimals.
```

**Expected Output:**
```javascript
const { add } = require('./math');

describe('add function', () => {
    describe('positive numbers', () => {
        test('adds two positive integers', () => {
            expect(add(2, 3)).toBe(5);
        });

        test('adds positive decimals', () => {
            expect(add(1.5, 2.5)).toBe(4);
        });
    });

    describe('negative numbers', () => {
        test('adds two negative numbers', () => {
            expect(add(-2, -3)).toBe(-5);
        });

        test('adds positive and negative numbers', () => {
            expect(add(5, -3)).toBe(2);
        });
    });

    describe('zero values', () => {
        test('adds zero to a number', () => {
            expect(add(5, 0)).toBe(5);
        });

        test('adds two zeros', () => {
            expect(add(0, 0)).toBe(0);
        });
    });

    describe('edge cases', () => {
        test('handles very large numbers', () => {
            expect(add(Number.MAX_SAFE_INTEGER, 0)).toBe(Number.MAX_SAFE_INTEGER);
        });

        test('handles floating point precision', () => {
            expect(add(0.1, 0.2)).toBeCloseTo(0.3);
        });
    });
});
```

---

#### Strategy 2: Behaviour-Driven Testing

Describe what you want to test, get comprehensive tests:

**Prompt:**
```text
Generate Jest tests for a UserService class that has methods:
- createUser(name, email) - creates a user and returns the user object
- findUserByEmail(email) - returns user or null if not found
- deleteUser(id) - returns true if deleted, throws if not found

Include tests for happy path, error cases, and edge cases.
```

**Expected Output:**
```javascript
const UserService = require('./UserService');

describe('UserService', () => {
    let userService;

    beforeEach(() => {
        userService = new UserService();
    });

    describe('createUser', () => {
        test('should create a user with valid data', () => {
            const user = userService.createUser('John Doe', 'john@example.com');
            
            expect(user).toHaveProperty('id');
            expect(user.name).toBe('John Doe');
            expect(user.email).toBe('john@example.com');
        });

        test('should throw error for invalid email', () => {
            expect(() => {
                userService.createUser('John Doe', 'invalid-email');
            }).toThrow('Invalid email format');
        });

        test('should throw error for empty name', () => {
            expect(() => {
                userService.createUser('', 'john@example.com');
            }).toThrow('Name is required');
        });

        test('should throw error for duplicate email', () => {
            userService.createUser('John Doe', 'john@example.com');
            
            expect(() => {
                userService.createUser('Jane Doe', 'john@example.com');
            }).toThrow('Email already exists');
        });
    });

    describe('findUserByEmail', () => {
        test('should return user when found', () => {
            userService.createUser('John Doe', 'john@example.com');
            
            const user = userService.findUserByEmail('john@example.com');
            
            expect(user.name).toBe('John Doe');
        });

        test('should return null when user not found', () => {
            const user = userService.findUserByEmail('notfound@example.com');
            
            expect(user).toBeNull();
        });

        test('should be case-insensitive', () => {
            userService.createUser('John Doe', 'John@Example.com');
            
            const user = userService.findUserByEmail('john@example.com');
            
            expect(user).not.toBeNull();
        });
    });

    describe('deleteUser', () => {
        test('should return true when user is deleted', () => {
            const user = userService.createUser('John Doe', 'john@example.com');
            
            const result = userService.deleteUser(user.id);
            
            expect(result).toBe(true);
        });

        test('should throw when user not found', () => {
            expect(() => {
                userService.deleteUser('non-existent-id');
            }).toThrow('User not found');
        });

        test('should not find user after deletion', () => {
            const user = userService.createUser('John Doe', 'john@example.com');
            userService.deleteUser(user.id);
            
            const found = userService.findUserByEmail('john@example.com');
            
            expect(found).toBeNull();
        });
    });
});
```

---

#### Strategy 3: Test from Comments

Add descriptive comments to your code, then ask for tests:

**Source Code with Comments:**
```javascript
/**
 * Calculates the factorial of a non-negative integer.
 * @param {number} n - The number to calculate factorial for
 * @returns {number} The factorial of n
 * @throws {Error} If n is negative or not an integer
 */
function factorial(n) {
    if (!Number.isInteger(n)) {
        throw new Error('Input must be an integer');
    }
    if (n < 0) {
        throw new Error('Factorial is not defined for negative numbers');
    }
    if (n === 0 || n === 1) {
        return 1;
    }
    let result = 1;
    for (let i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}
```

**Prompt:**
```text
Generate comprehensive tests for the factorial function based on its JSDoc documentation and implementation.
```

---

### Testing Different Scenarios

#### Async Function Testing

**Prompt:**
```text
Write Jest tests for an async function fetchUserData(userId) that:
- Fetches user data from an API
- Returns user object on success
- Throws 'User not found' for 404 responses
- Throws 'Network error' for connection failures

Include mocking of the fetch API.
```

**Expected Output:**
```javascript
const { fetchUserData } = require('./api');

// Mock the global fetch
global.fetch = jest.fn();

describe('fetchUserData', () => {
    beforeEach(() => {
        fetch.mockClear();
    });

    test('should return user data on success', async () => {
        const mockUser = { id: 1, name: 'John Doe' };
        fetch.mockResolvedValueOnce({
            ok: true,
            json: async () => mockUser
        });

        const result = await fetchUserData(1);

        expect(result).toEqual(mockUser);
        expect(fetch).toHaveBeenCalledWith('/api/users/1');
    });

    test('should throw "User not found" for 404', async () => {
        fetch.mockResolvedValueOnce({
            ok: false,
            status: 404
        });

        await expect(fetchUserData(999)).rejects.toThrow('User not found');
    });

    test('should throw "Network error" on connection failure', async () => {
        fetch.mockRejectedValueOnce(new Error('Failed to fetch'));

        await expect(fetchUserData(1)).rejects.toThrow('Network error');
    });

    test('should handle timeout', async () => {
        fetch.mockImplementationOnce(() => 
            new Promise((_, reject) => 
                setTimeout(() => reject(new Error('Timeout')), 5000)
            )
        );

        await expect(fetchUserData(1)).rejects.toThrow();
    }, 10000);
});
```

---

## 2. Ensuring Repeatable Test Coverage

### Test Coverage Goals

| Coverage Type | Description | Target |
|---------------|-------------|--------|
| **Statement** | Lines of code executed | 80%+ |
| **Branch** | Decision paths (if/else) | 80%+ |
| **Function** | Functions called | 90%+ |
| **Line** | Individual lines | 80%+ |

### Generating Tests for Coverage

**Prompt:**
```text
Analyse this function and generate tests to achieve 100% branch coverage:

function calculateDiscount(price, customerType, quantity) {
    if (price <= 0) {
        throw new Error('Invalid price');
    }
    
    let discount = 0;
    
    if (customerType === 'premium') {
        discount = 0.2;
    } else if (customerType === 'regular') {
        discount = 0.1;
    }
    
    if (quantity >= 10) {
        discount += 0.05;
    }
    
    return price * (1 - discount);
}
```

**Expected Output:**
```javascript
describe('calculateDiscount', () => {
    // Branch: price <= 0
    describe('invalid price', () => {
        test('throws for zero price', () => {
            expect(() => calculateDiscount(0, 'regular', 1))
                .toThrow('Invalid price');
        });

        test('throws for negative price', () => {
            expect(() => calculateDiscount(-10, 'regular', 1))
                .toThrow('Invalid price');
        });
    });

    // Branch: customerType === 'premium'
    describe('premium customer', () => {
        test('applies 20% discount', () => {
            expect(calculateDiscount(100, 'premium', 1)).toBe(80);
        });
    });

    // Branch: customerType === 'regular'
    describe('regular customer', () => {
        test('applies 10% discount', () => {
            expect(calculateDiscount(100, 'regular', 1)).toBe(90);
        });
    });

    // Branch: customerType is other
    describe('other customer type', () => {
        test('applies no customer discount', () => {
            expect(calculateDiscount(100, 'new', 1)).toBe(100);
        });
    });

    // Branch: quantity >= 10
    describe('bulk quantity discount', () => {
        test('adds 5% for quantity of 10', () => {
            expect(calculateDiscount(100, 'new', 10)).toBe(95);
        });

        test('adds 5% for quantity over 10', () => {
            expect(calculateDiscount(100, 'new', 15)).toBe(95);
        });
    });

    // Branch: quantity < 10
    describe('no bulk discount', () => {
        test('no extra discount for quantity under 10', () => {
            expect(calculateDiscount(100, 'new', 9)).toBe(100);
        });
    });

    // Combined branches
    describe('combined discounts', () => {
        test('premium customer with bulk order gets 25% off', () => {
            expect(calculateDiscount(100, 'premium', 10)).toBe(75);
        });

        test('regular customer with bulk order gets 15% off', () => {
            expect(calculateDiscount(100, 'regular', 10)).toBe(85);
        });
    });
});
```

---

### Testing Template Projects

For projects with consistent patterns, create test templates:

**Prompt:**
```text
Create a test template for Express.js route handlers that covers:
- Successful response with correct data
- Validation error handling
- Database error handling
- Authentication required scenarios

Use Jest and supertest.
```

**Expected Template:**
```javascript
const request = require('supertest');
const app = require('../app');

describe('{{ROUTE_NAME}} route', () => {
    describe('GET {{ENDPOINT}}', () => {
        describe('success cases', () => {
            test('returns 200 with data when authenticated', async () => {
                const response = await request(app)
                    .get('{{ENDPOINT}}')
                    .set('Authorization', 'Bearer valid-token');

                expect(response.status).toBe(200);
                expect(response.body).toHaveProperty('data');
            });
        });

        describe('authentication', () => {
            test('returns 401 without token', async () => {
                const response = await request(app)
                    .get('{{ENDPOINT}}');

                expect(response.status).toBe(401);
            });

            test('returns 401 with invalid token', async () => {
                const response = await request(app)
                    .get('{{ENDPOINT}}')
                    .set('Authorization', 'Bearer invalid-token');

                expect(response.status).toBe(401);
            });
        });

        describe('error handling', () => {
            test('returns 500 on database error', async () => {
                // Mock database to throw
                jest.spyOn(db, 'query').mockRejectedValueOnce(new Error('DB Error'));

                const response = await request(app)
                    .get('{{ENDPOINT}}')
                    .set('Authorization', 'Bearer valid-token');

                expect(response.status).toBe(500);
            });
        });
    });

    describe('POST {{ENDPOINT}}', () => {
        describe('validation', () => {
            test('returns 400 for missing required fields', async () => {
                const response = await request(app)
                    .post('{{ENDPOINT}}')
                    .set('Authorization', 'Bearer valid-token')
                    .send({});

                expect(response.status).toBe(400);
                expect(response.body).toHaveProperty('errors');
            });
        });
    });
});
```

---

## 3. Test Optimisation and Conversion

### Parameterised Testing

Convert repetitive tests to data-driven tests:

**Original Tests:**
```javascript
test('adds 2 and 3 to get 5', () => {
    expect(add(2, 3)).toBe(5);
});

test('adds 0 and 0 to get 0', () => {
    expect(add(0, 0)).toBe(0);
});

test('adds -1 and 1 to get 0', () => {
    expect(add(-1, 1)).toBe(0);
});
```

**Prompt:**
```text
Refactor these Jest tests for the add function using parameterised testing with test.each.
```

**Optimised Output:**
```javascript
describe('add function', () => {
    test.each([
        [2, 3, 5],
        [0, 0, 0],
        [-1, 1, 0],
        [100, 200, 300],
        [-5, -3, -8],
        [1.5, 2.5, 4],
    ])('add(%p, %p) returns %p', (a, b, expected) => {
        expect(add(a, b)).toBe(expected);
    });

    test.each([
        { a: 2, b: 3, expected: 5, description: 'positive integers' },
        { a: 0, b: 0, expected: 0, description: 'zeros' },
        { a: -1, b: 1, expected: 0, description: 'mixed signs' },
    ])('$description: add($a, $b) = $expected', ({ a, b, expected }) => {
        expect(add(a, b)).toBe(expected);
    });
});
```

---

### Framework Conversion

#### Selenium to Cypress

**Original Selenium Test (Python):**
```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://example.com/login")
driver.find_element_by_id("username").send_keys("user")
driver.find_element_by_id("password").send_keys("pass")
driver.find_element_by_id("login-button").click()
assert "Dashboard" in driver.title
driver.quit()
```

**Prompt:**
```text
Convert this Selenium test to Cypress with proper best practices including custom commands and assertions.
```

**Cypress Output:**
```javascript
// cypress/support/commands.js
Cypress.Commands.add('login', (username, password) => {
    cy.get('#username').type(username);
    cy.get('#password').type(password);
    cy.get('#login-button').click();
});

// cypress/e2e/login.cy.js
describe('Login', () => {
    beforeEach(() => {
        cy.visit('/login');
    });

    it('should login successfully with valid credentials', () => {
        cy.login('user', 'pass');
        
        cy.title().should('include', 'Dashboard');
        cy.url().should('include', '/dashboard');
    });

    it('should show error with invalid credentials', () => {
        cy.login('invalid', 'invalid');
        
        cy.get('.error-message').should('be.visible');
        cy.url().should('include', '/login');
    });

    it('should validate required fields', () => {
        cy.get('#login-button').click();
        
        cy.get('#username:invalid').should('exist');
    });
});
```

---

#### JUnit to pytest

**Prompt:**
```text
Convert these JUnit tests to pytest with appropriate fixtures and assertions:

@Test
public void testAddition() {
    Calculator calc = new Calculator();
    assertEquals(5, calc.add(2, 3));
}

@Test
public void testDivisionByZero() {
    Calculator calc = new Calculator();
    assertThrows(ArithmeticException.class, () -> calc.divide(10, 0));
}
```

**pytest Output:**
```python
import pytest
from calculator import Calculator

@pytest.fixture
def calculator():
    """Fixture to create a Calculator instance."""
    return Calculator()

class TestCalculator:
    def test_addition(self, calculator):
        assert calculator.add(2, 3) == 5

    def test_division_by_zero(self, calculator):
        with pytest.raises(ZeroDivisionError):
            calculator.divide(10, 0)

    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
    ])
    def test_addition_parametrized(self, calculator, a, b, expected):
        assert calculator.add(a, b) == expected
```

Note: Java exception types do not map 1:1 to Python. For division by zero, Python raises `ZeroDivisionError`.

---

#### Mocha to Jest

**Prompt:**
```text
Convert this Mocha/Chai test suite to Jest:

const { expect } = require('chai');

describe('Array', function() {
    describe('#indexOf()', function() {
        it('should return -1 when value is not present', function() {
            expect([1, 2, 3].indexOf(4)).to.equal(-1);
        });
    });
});
```

**Jest Output:**
```javascript
describe('Array', () => {
    describe('#indexOf()', () => {
        test('should return -1 when value is not present', () => {
            expect([1, 2, 3].indexOf(4)).toBe(-1);
        });
    });
});
```

---

## Testing Best Practices Prompts

| Goal | Prompt |
|------|--------|
| **Mocking** | "Add mocks for external API calls in these tests using Jest mock functions" |
| **Fixtures** | "Create test fixtures and factory functions for User and Order models" |
| **Snapshot testing** | "Add snapshot tests for this React component" |
| **Performance** | "Optimise these tests to run faster by sharing setup across tests" |
| **Flaky tests** | "Identify potential flakiness in these async tests and add proper waits" |

---

## Quality Assurance Checklist

Before merging test code, verify:

- [ ] **Descriptive names** - Test names clearly describe what is being tested
- [ ] **AAA pattern** - Tests follow Arrange, Act, Assert structure
- [ ] **Independence** - Tests can run in any order
- [ ] **No side effects** - Tests clean up after themselves
- [ ] **Edge cases** - Boundary conditions are tested
- [ ] **Error paths** - Exception scenarios are covered
- [ ] **Mocking** - External dependencies are properly mocked
- [ ] **Assertions** - Each test has meaningful assertions
- [ ] **Speed** - Tests run quickly (unit tests < 100ms each)
- [ ] **Coverage** - New code has corresponding tests

---

## Key Takeaways

1. **Provide context** - Give Copilot the function or describe the behaviour to test
2. **Specify scenarios** - List the test cases you want covered
3. **Include edge cases** - Explicitly ask for boundary and error conditions
4. **Use parameterisation** - Convert repetitive tests to data-driven tests
5. **Maintain framework knowledge** - Copilot knows testing framework conventions
6. **Review generated tests** - Ensure they actually test the right things

---

## Next Steps

- Complete the [Week 3 Lab](3-Week3-Lab.md) for hands-on practice
- Review [Week 3 Prompts](4-Week3-Prompts.md) for testing prompt examples
- Explore [Week 4](../Week4/) for refactoring and code quality topics

---
