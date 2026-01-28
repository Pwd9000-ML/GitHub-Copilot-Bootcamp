# GitHub Copilot Prompt Engineering Guide

A comprehensive guide to different prompting techniques for GitHub Copilot, with practical examples using a Book Inventory Management System.

---

## Table of Contents

1. [Template Generation](#1-template-generation)
2. [Project Scaffolding](#2-project-scaffolding)
3. [Custom Scaffolding](#3-custom-scaffolding)
4. [Code Generation](#4-code-generation)
5. [Code Explanation](#5-code-explanation)
6. [Debugging & Research](#6-debugging--research)
7. [Unit Test Generation](#7-unit-test-generation)
8. [SQL Query Generation](#8-sql-query-generation)

---

## 1. Template Generation

**Technique:** Ask Copilot to generate reusable function templates with clearly defined parameters and structure.

**When to use:** When you need boilerplate code that follows a consistent pattern and can be customised later.

### Example Prompts

#### Creating Functions with Defined Fields

```text
Generate a JavaScript function template to add a new book with fields like title, author, and genre.
```

```text
Can you create a reusable function to add books with properties such as title, author, genre, and publication year?
```

#### Search/Filter Functions

```text
Write a function template to search for books in an inventory by title or genre.
```

```text
Generate a reusable JavaScript function to filter books based on their title or genre.
```

#### Iterative Refinement

```text
Refactor the addBook function to include an optional field for publication year.
```

```text
Modify the searchBooks function to include filtering by author as well.
```

> **Tip:** Start with basic requirements, then iterate with refinement prompts to add complexity.

---

## 2. Project Scaffolding

**Technique:** Use Copilot to create project structures, folder hierarchies, and initial configuration files.

**When to use:** When starting a new project and need to establish a standard directory layout.

### Example Prompts

#### Directory Structure

```text
Create a project structure with folders for src, tests, and public.
```

```text
Generate an initial scaffold for a project, including src, tests, public, and a README file.
```

#### Configuration Files

```text
Create a basic index.js file to serve as the entry point for the application.
```

```text
Generate a package.json file with a basic project configuration.
```

```text
Write a README.md template for a Book Inventory Management System project.
```

#### Modular Organisation

```text
Add subfolders models, controllers, and views inside the src folder for better modularity.
```

> **Tip:** Be specific about the folder names and their purposes for better results.

---

## 3. Custom Scaffolding

**Technique:** Generate specific files with predefined content tailored to your architecture patterns.

**When to use:** When you need files that follow specific design patterns (MVC, etc.) with appropriate structure.

### Example Prompts

#### Model Layer

```text
Create a file named book.js inside the src/models folder and define a Book class with properties for title, author, and genre.
```

#### Controller Layer

```text
Generate a file inventoryController.js in the src/controllers folder to handle adding and searching books.
```

#### View Layer

```text
Create an index.html file inside the src/views folder with a simple form for adding a new book.
```

#### Dependencies & Scripts

```text
Update the package.json file to include Jest for testing and add start and test scripts.
```

> **Tip:** Include the file path and purpose in your prompt for contextually appropriate code.

---

## 4. Code Generation

**Technique:** Request specific functionality with clear requirements about behaviour and constraints.

**When to use:** When implementing business logic, data operations, or specific algorithms.

### Example Prompts

#### Core Business Logic

```text
Write a function to add books to an array and prevent duplicate entries based on the title.
```

```text
Create a function to list all books in the inventory with their details.
```

```text
Generate a function to search for books by title or genre in an array.
```

#### Data Persistence

```text
Write a function to save the book inventory to a JSON file using Node.js.
```

```text
Generate a function to save and retrieve book data from local storage for a browser-based application.
```

> **Tip:** Specify constraints (e.g., "prevent duplicates") and the target environment (Node.js, browser) for accurate code.

---

## 5. Code Explanation

**Technique:** Ask Copilot to explain existing code logic, identify patterns, and suggest improvements.

**When to use:** When reviewing unfamiliar code, onboarding, or seeking optimisation opportunities.

### Example Prompts

#### Understanding Logic

```text
Explain the logic used in the addBook function, especially how duplicates are handled.
```

```text
Describe how the searchBooks function works and how it filters by title or genre.
```

```text
Can you provide an explanation of the function that saves the inventory to local storage?
```

#### Requesting Improvements

```text
Suggest ways to optimise the addBook function for performance.
```

```text
Identify any potential edge cases in the searchBooks function and how they could be handled.
```

> **Tip:** Reference specific functions or code sections for targeted explanations.

---

## 6. Debugging & Research

**Technique:** Use Copilot to identify bugs, debug issues, and research alternative approaches.

**When to use:** When troubleshooting errors, exploring solutions, or evaluating different implementation strategies.

### Example Prompts

#### Introducing & Fixing Bugs (Learning Exercise)

```text
Deliberately introduce a bug where the searchBooks function uses an undefined variable.
```

```text
How can I debug and fix an issue where the addBook function isn't adding books to the array?
```

#### Exploring Alternatives

```text
Research alternative error-handling strategies for saving data to local storage.
```

```text
Can you suggest a more efficient algorithm for searching through a large book inventory?
```

> **Tip:** When debugging, describe the expected vs actual behaviour for better diagnostics.

---

## 7. Unit Test Generation

**Technique:** Generate comprehensive test suites covering happy paths, edge cases, and error scenarios.

**When to use:** When implementing TDD, increasing code coverage, or validating refactored code.

### Example Prompts

#### Basic Test Generation

```text
Write unit tests using Jest for the addBook function to ensure it handles duplicates correctly.
```

```text
Generate Jest test cases for the searchBooks function, including cases for no results and multiple matches.
```

#### Test Refinement

```text
Run the Jest tests and provide suggestions to improve code coverage.
```

```text
Generate additional test cases for edge scenarios, like searching with an empty query or adding books with missing fields.
```

> **Tip:** Specify the testing framework and mention specific scenarios to cover.

---

## 8. SQL Query Generation

**Technique:** Generate SQL queries by describing the data operation in natural language.

**When to use:** When writing database queries for CRUD operations, reports, or data analysis.

### Example Prompts

#### Basic SELECT

```text
Write a SQL query to select all columns from the 'employees' table where the department is 'Sales'.
```

#### Filtering with WHERE

```text
Create a SQL query to find all orders placed by customers in the 'New York' city with a total amount greater than $100.
```

#### JOIN Operations

```text
Write a SQL query to join the 'orders' and 'customers' tables on the 'customer_id' field, selecting the order ID, customer name, and order total.
```

#### Aggregate Functions

```text
Write a SQL query to calculate the average salary of employees in each department.
```

#### GROUP BY

```text
Create a SQL query that groups the 'sales' table by 'product_id' and sums the 'quantity_sold' for each product.
```

#### Subqueries

```text
Write a SQL query to find employees who earn more than the average salary in the company.
```

#### UPDATE Statements

```text
Write a SQL query to update the 'status' column to 'inactive' for all employees who haven't logged in for 6 months.
```

#### DELETE Statements

```text
Write a SQL query to delete all records from the 'temp_employees' table where the 'hire_date' is earlier than 2020.
```

#### DISTINCT Values

```text
Create a SQL query to select distinct job titles from the 'employees' table.
```

#### Sorting & Limiting

```text
Write a SQL query to get the top 5 highest-paid employees ordered by salary in descending order.
```

> **Tip:** Include table names, column names, and specific conditions for accurate query generation.

---

## Quick Reference: Prompting Best Practices

| Technique | Key Principle | Example Trigger Words |
|-----------|--------------|----------------------|
| **Template Generation** | Define structure & fields | "template", "reusable", "with fields" |
| **Scaffolding** | Specify folder/file hierarchy | "create structure", "scaffold", "folders for" |
| **Code Generation** | State behaviour & constraints | "write a function", "prevent", "handle" |
| **Code Explanation** | Reference specific code | "explain", "describe how", "logic used" |
| **Debugging** | Describe expected vs actual | "debug", "fix issue", "not working" |
| **Test Generation** | Specify framework & scenarios | "unit tests using Jest", "test cases for" |
| **SQL Generation** | Name tables & conditions | "SQL query", "join", "where", "group by" |

---

## Additional Tips

1. **Be Specific:** Include language, framework, and context in your prompts
2. **Iterate:** Start simple, then refine with follow-up prompts
3. **Provide Context:** Reference existing code or file locations when relevant
4. **Specify Constraints:** Mention edge cases, error handling, or performance requirements
5. **Use Examples:** When possible, show the expected input/output format