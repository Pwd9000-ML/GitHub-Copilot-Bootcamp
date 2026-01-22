# Week 1 Lab: Getting Started & Scaffold Projects

## Overview

This lab focuses on getting comfortable with GitHub Copilot and using it to scaffold new projects efficiently.

## Objectives

- Set up GitHub Copilot in your development environment
- Practice effective prompt engineering
- Scaffold a new project from scratch
- Generate boilerplate code and configuration files
- Create initial project documentation

## Prerequisites

- GitHub Copilot installed and configured
- IDE of your choice (VS Code, Visual Studio, JetBrains, etc.)
- Basic knowledge of your chosen programming language
- Git installed

## Lab Exercises

### Exercise 1: Copilot Setup Verification

1. Verify Copilot is working in your IDE
2. Test inline suggestions
3. Test Copilot Chat
4. Explore Copilot settings

### Exercise 2: Prompt Kata Practice

Complete at least 5 katas from [prompts/prompt-katas.md](../../prompts/prompt-katas.md):

- [ ] Kata 1: Basic Function Generation
- [ ] Kata 2: Input Validation
- [ ] Kata 3: Error Handling
- [ ] Kata 4: Type-Safe API Client
- [ ] Kata 5: Test Generation

### Exercise 3: Project Scaffolding

Choose ONE of the following projects to scaffold:

**Option A: Todo API (Node.js/TypeScript)**
- Express.js server
- REST API endpoints
- In-memory or database storage
- Basic authentication
- Input validation
- Error handling

**Option B: Task Manager CLI (Python)**
- Command-line interface
- Task CRUD operations
- Data persistence (JSON file)
- Command parsing
- Help documentation

**Option C: Personal Project**
- Any project in your preferred language
- Must include basic CRUD operations
- Should follow organization standards

### Exercise 4: Configuration & Documentation

Generate the following using Copilot:

1. **Configuration Files**
   - package.json / requirements.txt
   - .gitignore
   - .editorconfig
   - Environment variables template

2. **Documentation**
   - README.md with:
     - Project description
     - Installation instructions
     - Usage examples
     - API documentation (if applicable)
   - Code comments and docstrings
   - Architecture diagram (text-based)

## Deliverables

Submit via Pull Request:

1. **Working Project**
   - Scaffolded project structure
   - All configuration files
   - Basic functionality implemented

2. **Documentation**
   - Comprehensive README
   - Code comments
   - Setup instructions

3. **Reflection**
   - Submit a daily reflection issue (see issue templates)
   - Include effective prompts you used
   - Note challenges and how you overcame them

## Using Copilot Effectively

### Prompt Examples

```typescript
// Create an Express.js server with:
// - CORS enabled
// - JSON body parser
// - Error handling middleware
// - Health check endpoint
// - Port from environment variable
```

```python
# Create a CLI parser with commands:
# - add: Add new task
# - list: List all tasks
# - complete: Mark task as complete
# - delete: Remove a task
# Include help text for each command
```

### Tips

1. **Be Specific**: Provide detailed requirements in comments
2. **Iterate**: Refine prompts based on initial results
3. **Context**: Include relevant context before code generation
4. **Review**: Always review and test generated code

## Evaluation Criteria

Your submission will be evaluated on:

- **Functionality** (30%): Does the project work as intended?
- **Code Quality** (25%): Is the code clean and well-organized?
- **Documentation** (20%): Is documentation comprehensive and clear?
- **Copilot Usage** (15%): How effectively did you use Copilot?
- **Completeness** (10%): Are all requirements met?

## Resources

- [Participant Quick Start](../../docs/participant-quickstart.md)
- [Week 1 Materials](../../docs/week-1.md)
- [Prompt Library](../../prompts/prompt-library.md)
- [Coding Standards](../../docs/org-standards/coding-standards.md)

## Support

If you have questions:
- Review the [documentation](../../docs/)
- Check [existing discussions](https://github.com/Pwd9000-ML/GHCP-bootcamp-template/discussions)
- Ask in the bootcamp chat channel
- Open an issue for technical problems

## Next Steps

After completing this lab:
1. Submit your PR
2. Complete daily reflections
3. Review other participants' work
4. Prepare for Week 2: Features, Documentation & Security

Good luck! 🚀
