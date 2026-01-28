# GitHub Copilot Prompt Engineering Guide

## Session Overview

**Purpose:** Reference guide for prompt engineering techniques  
**Format:** Example prompts with explanations and tips  
**Objective:** Provide practical prompting techniques using a Book Inventory Management System as context.

---

## Contents

- [1. Template Generation](#1-template-generation)
- [2. Project Scaffolding](#2-project-scaffolding)
- [3. Custom Scaffolding](#3-custom-scaffolding)
- [4. Code Generation](#4-code-generation)
- [5. Code Explanation](#5-code-explanation)
- [6. Debugging & Research](#6-debugging--research)
- [7. Unit Test Generation](#7-unit-test-generation)
- [8. SQL Query Generation](#8-sql-query-generation)

---

## 1. Template Generation

Template generation creates reusable function templates with clearly defined parameters and structure.

- Generate boilerplate code that follows consistent patterns
- Define fields and parameters upfront for customisation
- Build reusable components that can be adapted later
- Start with basic requirements, then iterate with refinements

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

Project scaffolding creates project structures, folder hierarchies, and initial configuration files.

- Create standard directory layouts for new projects
- Generate initial configuration files (package.json, README)
- Establish consistent folder naming conventions
- Set up entry points and basic project organisation

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

Custom scaffolding generates specific files with predefined content tailored to your architecture patterns.

- Create files following specific design patterns (MVC, etc.)
- Generate model, controller, and view layer files
- Include appropriate structure for each layer
- Specify file paths and purposes for contextually appropriate code

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

Code generation requests specific functionality with clear requirements about behaviour and constraints.

- Implement business logic and data operations
- Specify constraints like preventing duplicates
- Define target environment (Node.js, browser)
- Handle data persistence and storage operations

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
In a Node.js environment, write a function to save the book inventory to a JSON file on disk.
```

> **Tip:** Specify constraints (e.g., "prevent duplicates") and the target environment (Node.js, browser) for accurate code.

---

## 5. Code Explanation

Code explanation helps you understand existing code logic, identify patterns, and discover improvements.

- Get explanations of unfamiliar code during onboarding
- Understand specific functions and their logic
- Identify optimisation opportunities
- Review code patterns and edge case handling

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

Debugging and research helps identify bugs, troubleshoot issues, and explore alternative approaches.

- Identify and fix bugs in existing code
- Explore alternative implementation strategies
- Research different error-handling approaches
- Describe expected vs actual behaviour for better diagnostics

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

Unit test generation creates comprehensive test suites covering happy paths, edge cases, and errors.

- Generate tests for TDD implementation
- Increase code coverage for existing functions
- Validate refactored code behaviour
- Specify testing framework and scenarios to cover

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

SQL query generation creates database queries by describing data operations in natural language.

- Generate SELECT, UPDATE, DELETE statements
- Create queries with JOINs and aggregate functions
- Build complex queries with subqueries and grouping
- Include table names, column names, and conditions for accuracy

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

## Week 2 Feedback

Please complete the following reflections after completing Week 2 activities:

- [Submit Week 2 Lab Reflection](../../issues/new?template=week2-lab.yml)
- [Submit Weekly Reflection](../../issues/new?template=weekly-reflection.yml)

---

## Next Steps

After mastering prompt engineering and advanced workflows in Week 2, we will explore DevOps automation and testing strategies in Week 3 to streamline software delivery.

**[← Back to Main README](../../README.md)** | **[Continue to Week 3 →](../Week3/1-DevOps-Automation.md)**