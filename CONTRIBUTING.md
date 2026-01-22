# Contributing to GitHub Copilot Bootcamp Template

Thank you for your interest in contributing! This document provides guidelines for contributing to this bootcamp template.

## Code of Conduct

This project follows the [GitHub Community Guidelines](https://docs.github.com/articles/github-community-guidelines). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Issues

Before creating an issue:
- Check if the issue already exists
- Use the issue templates provided
- Include relevant details (environment, steps to reproduce, etc.)

### Suggesting Enhancements

Enhancement suggestions are welcome! Please:
- Use a clear and descriptive title
- Provide detailed explanation of the enhancement
- Explain why this enhancement would be useful
- Include examples if applicable

### Pull Requests

1. **Fork the repository** and create your branch from `main`
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Follow the coding standards in [docs/org-standards/](docs/org-standards/)
   - Write clear, descriptive commit messages
   - Add tests if applicable
   - Update documentation

3. **Test your changes**
   - Ensure all tests pass
   - Add new tests for new functionality
   - Verify documentation builds correctly

4. **Submit your PR**
   - Use the PR template
   - Link related issues
   - Provide clear description of changes
   - Request review from maintainers

## Development Setup

### Prerequisites
- Git
- Node.js 20+ (for TypeScript sample app)
- Python 3.9+ (for Python sample app)
- GitHub account with Copilot access

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/GHCP-bootcamp-template.git
   cd GHCP-bootcamp-template
   ```

2. Install dependencies:
   ```bash
   # For TypeScript backend
   cd sample-app/backend-ts
   npm install
   
   # For Python backend
   cd ../backend-py
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run tests:
   ```bash
   # TypeScript
   npm test
   
   # Python
   pytest
   ```

## Coding Standards

### General Guidelines
- Write clear, self-documenting code
- Follow existing code style
- Add comments for complex logic
- Keep functions small and focused

### TypeScript/JavaScript
- Use TypeScript for new code
- Follow ESLint rules
- Use meaningful variable names
- Add JSDoc comments for functions

### Python
- Follow PEP 8 style guide
- Use type hints
- Add docstrings for functions and classes
- Use meaningful variable names (snake_case)

### Markdown
- Use clear, concise language
- Include code examples
- Add links to related documentation
- Check for spelling and grammar

## Commit Message Guidelines

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
type(scope): subject

body

footer
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples**:
```
feat(docs): add week 5 materials

Add documentation and exercises for bonus week 5 content
covering advanced Copilot features.

Closes #123
```

```
fix(labs): correct week 2 lab instructions

Fix typo in security checklist that caused confusion
for participants.
```

## Documentation

### Adding New Documentation
- Place documentation in appropriate `docs/` subdirectory
- Follow existing documentation structure
- Use clear headings and sections
- Include examples where helpful
- Add links to related content

### Updating Documentation
- Keep documentation in sync with code
- Update table of contents if needed
- Check for broken links
- Verify examples still work

## Testing

### Adding Tests
- Write tests for new features
- Ensure tests are clear and focused
- Use descriptive test names
- Include both positive and negative cases

### Running Tests
```bash
# TypeScript
cd sample-app/backend-ts
npm test

# Python
cd sample-app/backend-py
pytest
```

## Review Process

1. **Automated Checks**: PRs must pass all CI checks
2. **Code Review**: At least one maintainer review required
3. **Documentation Review**: Verify documentation is updated
4. **Testing**: Ensure tests pass and coverage is maintained

## Release Process

This template follows semantic versioning (MAJOR.MINOR.PATCH):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes

## Questions?

- Check [existing issues](https://github.com/Pwd9000-ML/GHCP-bootcamp-template/issues)
- Review [documentation](docs/)
- Ask in [Discussions](https://github.com/Pwd9000-ML/GHCP-bootcamp-template/discussions)

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

Thank you for contributing! 🚀
