# GitHub Copilot Bootcamp Template

An interactive 4-week bootcamp program designed to help developers master GitHub Copilot through hands-on exercises and real-world scenarios.

## 🎯 Overview

This comprehensive bootcamp template provides everything you need to run or participate in a GitHub Copilot training program. Whether you're a facilitator organizing a bootcamp or a participant learning to use Copilot effectively, this repository has you covered.

## 📚 Bootcamp Structure

### Week 1: Getting Started & Scaffold Projects
- GitHub Copilot fundamentals
- Effective prompt engineering
- Project scaffolding and boilerplate generation
- Code organization patterns

### Week 2: Features, Documentation & Security
- Feature development with Copilot
- Documentation generation
- Security-first development
- Input validation and secure coding practices

### Week 3: DevOps & Testing
- Test-driven development (TDD)
- CI/CD pipeline creation
- Automated testing
- Code quality and DORA metrics

### Week 4: Refactoring Legacy Code
- Legacy code analysis
- Refactoring strategies
- Test-driven refactoring
- Code quality improvements

## 🚀 Getting Started

### For Participants

1. **Fork this repository** to your GitHub account
2. **Review the [Quick Start Guide](docs/participant-quickstart.md)**
3. **Install GitHub Copilot** in your preferred IDE
4. **Start with Week 1** materials in [docs/week-1.md](docs/week-1.md)
5. **Complete labs** in the `labs/` directory
6. **Submit daily reflections** using GitHub Issues

### For Facilitators

1. **Review the [Facilitator Guide](docs/facilitator-guide.md)**
2. **Customize** organization-specific content in `docs/org-standards/` and `prompts/org-style-prompts.md`
3. **Set up** repository access for participants
4. **Follow the weekly structure** outlined in the facilitator guide
5. **Track progress** using the scorecards in `scorecards/`

## 📂 Repository Structure

```
copilot-bootcamp-template/
├── README.md                    # This file
├── docs/                        # Documentation and weekly materials
│   ├── participant-quickstart.md
│   ├── facilitator-guide.md
│   ├── week-1.md               # Week 1: Scaffold & Foundation
│   ├── week-2.md               # Week 2: Features & Security
│   ├── week-3.md               # Week 3: DevOps & Testing
│   ├── week-4.md               # Week 4: Legacy Refactoring
│   └── org-standards/          # Coding and security standards
│       ├── coding-standards.md
│       ├── security-guidelines.md
│       └── documentation-style.md
├── prompts/                     # Prompt engineering resources
│   ├── prompt-library.md       # Collection of effective prompts
│   ├── prompt-katas.md         # Practice exercises
│   └── org-style-prompts.md    # Organization-specific prompts
├── labs/                        # Weekly lab exercises
│   ├── week1-scaffold/
│   ├── week2-feature-docs-security/
│   ├── week3-devops-testing/
│   └── week4-refactor-legacy/
├── sample-app/                  # Sample applications
│   ├── backend-ts/             # TypeScript API with TODOs
│   └── backend-py/             # Python API alternative
├── legacy/                      # Legacy code for refactoring
│   └── messy_module.py         # Intentionally messy code
├── scorecards/                  # Tracking and metrics
│   ├── copilot-adoption-scorecard.csv
│   └── dora-cheat-sheet.md
├── .github/                     # GitHub configuration
│   ├── ISSUE_TEMPLATE/         # Issue templates
│   ├── pull_request_template.md
│   └── workflows/              # CI/CD workflows
│       ├── ci.yml
│       └── codeql.yml
├── .editorconfig               # Editor configuration
└── CONTRIBUTING.md             # Contribution guidelines
```

## 🛠️ Sample Applications

### TypeScript Backend
A simple REST API with authentication and task management. Includes intentional TODOs for learning exercises.

```bash
cd sample-app/backend-ts
npm install
npm run dev
```

### Python Backend (Alternative)
Flask-based API with similar functionality, offering an alternative for Python developers.

```bash
cd sample-app/backend-py
pip install -r requirements.txt
python run.py
```

## 📖 Resources

### Documentation
- [Participant Quick Start](docs/participant-quickstart.md)
- [Facilitator Guide](docs/facilitator-guide.md)
- [Organization Standards](docs/org-standards/)

### Prompts & Practice
- [Prompt Library](prompts/prompt-library.md)
- [Prompt Katas](prompts/prompt-katas.md)

### Metrics & Tracking
- [DORA Metrics Guide](scorecards/dora-cheat-sheet.md)
- [Adoption Scorecard](scorecards/copilot-adoption-scorecard.csv)

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎓 Learning Objectives

By the end of this bootcamp, participants will:

✅ Master GitHub Copilot features and capabilities  
✅ Write effective prompts for code generation  
✅ Develop with security awareness  
✅ Implement test-driven development  
✅ Create CI/CD pipelines  
✅ Refactor legacy code effectively  
✅ Apply organization coding standards  
✅ Generate comprehensive documentation  
✅ Understand DORA metrics and DevOps practices  

## 🌟 Success Stories

Share your bootcamp success stories by opening an issue or discussion!

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/Pwd9000-ML/GHCP-bootcamp-template/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Pwd9000-ML/GHCP-bootcamp-template/discussions)
- **Documentation**: [docs/](docs/)

## 🙏 Acknowledgments

- GitHub Copilot team for the amazing tool
- All bootcamp participants and facilitators
- Contributors to this template

---

**Ready to start your Copilot journey?** Begin with the [Participant Quick Start Guide](docs/participant-quickstart.md)!
