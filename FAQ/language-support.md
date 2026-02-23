# Language Support with GitHub Copilot

GitHub Copilot supports a wide range of programming languages, but the quality and depth of suggestions vary depending on how much publicly available training data exists for each language. This guide covers language-specific considerations, known limitations, and best practices.

For IDE setup instructions, see the [Week 1 Setup and Configuration Guide](../Workshops/Week1/2-Setup-and-Configuration.md). For general IDE feature availability, see the [IDE Support Guide](IDE-support.md).

---

## Contents

- [ABAP](#abap)
  - [Language Support Quality](#language-support-quality)
  - [Known Limitations for ABAP Development](#known-limitations-for-abap-development)
  - [Best Practices for ABAP Developers](#best-practices-for-abap-developers)

---

## ABAP

ABAP is a proprietary SAP language with limited open-source code available. This section covers ABAP-specific considerations when using GitHub Copilot. For Eclipse IDE setup instructions, see the [Week 1 Setup and Configuration Guide](../Workshops/Week1/2-Setup-and-Configuration.md#eclipse).

### Language Support Quality

GitHub Copilot's AI models are trained primarily on publicly available code repositories. Since ABAP is a **proprietary SAP language** with limited open-source code available:

- Suggestions may be **less accurate** compared to popular languages (Python, JavaScript, Java)
- Complex SAP-specific patterns, BAPIs, and function modules may not be well-represented in training data
- Code completions for standard ABAP constructs work, but domain-specific SAP modules may have inconsistent support
- Custom SAP tables, data elements, and domains are unknown to Copilot

### Known Limitations for ABAP Development

#### 1. Eclipse/ADT Integration Limitations (Validate in Your Environment)

ABAP Development Tools (ADT) uses Eclipse-specific mechanisms for accessing ABAP objects. Some Copilot features that operate by editing local files (for example, multi-file edits or agentic workflows) may behave differently depending on your Eclipse/ADT setup.

- If you see unexpected behaviour with ABAP objects, fall back to **Ask mode** and apply changes manually.
- Use the [Copilot feature matrix (Eclipse)](https://docs.github.com/en/copilot/reference/copilot-feature-matrix?tool=eclipse) as the source of truth for what is supported.

#### 2. Eclipse Installation Dependencies

Users have reported dependency conflicts during GitHub Copilot installation in Eclipse:

- Conflicts with **Mylyn WikiText UI** and **LSP4e** components may occur
- "Cannot satisfy dependency" errors may prevent installation
- **Solution:** Ensure your Eclipse installation is fully up-to-date and consider removing conflicting plugins if necessary

#### 3. Network and Certificate Issues

Organisations using corporate proxies may experience:

- Certificate validation failures during sign-in
- Language server connection issues
- **Solution:** Configure the `NODE_EXTRA_CA_CERTS` environment variable to point to your organisation's CA certificates

#### 4. SAP Backend Connectivity

ABAP development requires connection to an SAP backend system. GitHub Copilot:

- Cannot access your SAP system metadata directly
- Has no visibility into your custom function modules, classes, or data dictionary objects
- Cannot suggest code based on your specific SAP customisations or transport requests

### Best Practices for ABAP Developers

1. **Use Copilot for boilerplate code:** Standard ABAP syntax, loops, SELECT statements, and common patterns
2. **Provide detailed comments:** Help Copilot understand your intent with descriptive ABAP comments (`" comment`)
3. **Verify all suggestions:** Always review generated ABAP code against SAP documentation and your system's data dictionary
4. **Combine with SAP tools:** Use Copilot alongside SAP's built-in code templates, patterns, and ABAP documentation
5. **Leverage for non-ABAP files:** Copilot works well for related files like JSON, XML, JavaScript (UI5/Fiori), and documentation
