# GitHub Copilot API Metrics Reference Guide

## Overview

This guide outlines the properties of the Copilot API response that can be used to build various metrics and visuals for tracking adoption, usage patterns, and engagement across your organisation.

> **Note:** This reference is designed for administrators and analytics teams building custom dashboards and reports using the GitHub Copilot API.

## Table of Contents

- [Top-Level Metrics](#top-level-metrics)
- [Copilot IDE Chat Metrics](#copilot-ide-chat-metrics)
- [Copilot IDE Code Completions Metrics](#copilot-ide-code-completions-metrics)
- [Copilot Dotcom Chat Metrics](#copilot-dotcom-chat-metrics)
- [Copilot Dotcom Pull Requests Metrics](#copilot-dotcom-pull-requests-metrics)
- [Key Metrics Summary](#key-metrics-summary)
- [Best Practices](#best-practices)

---

## Top-Level Metrics

These metrics are returned at the root level of the API response for each date.

| Metric | Description | API Property |
|---|---|---|
| **Date** | The date for which metrics are reported | `date` |
| **Total Active Users** | Total number of users with active Copilot licences on this date | `total_active_users` |
| **Total Engaged Users** | Total number of users who actively used any Copilot feature | `total_engaged_users` |

> **Note:** The API only returns results for a given day if the organisation contained five or more members with active Copilot licences on that day.

---

## Copilot IDE Chat Metrics

Chat metrics track how users interact with Copilot Chat across different IDEs and AI models.

### A. General Metrics

| Metric | Description | API Property |
|---|---|---|
| **Total Engaged Users (IDE Chat)** | Total number of users who prompted Copilot Chat in the IDE | `copilot_ide_chat.total_engaged_users` |

### B. Editor-Level Metrics

Breakdown of chat engagement by IDE/editor:

| Metric | Description | API Property |
|---|---|---|
| **Editor Name** | Name of the IDE (e.g., VS Code, PyCharm, Visual Studio) | `copilot_ide_chat.editors[].name` |
| **Total Engaged Users for the Editor** | Number of users who prompted Copilot Chat in the specified editor | `copilot_ide_chat.editors[].total_engaged_users` |

**Example:** Track which IDEs have the highest chat adoption

### C. Model-Level Metrics (Within Each Editor)

Detailed metrics for each AI model used within an editor:

| Metric | Description | API Property |
|---|---|---|
| **Model Name** | Name of the AI model used (e.g., 'default' for standard model, or a custom model identifier) | `copilot_ide_chat.editors[].models[].name` |
| **Is Custom Model** | Boolean flag indicating if this is a custom or default model | `copilot_ide_chat.editors[].models[].is_custom_model` |
| **Custom Model Training Date** | Date when the custom model was trained (null for default models) | `copilot_ide_chat.editors[].models[].custom_model_training_date` |
| **Total Engaged Users for the Model** | Number of users who used Copilot Chat with this model in the given editor | `copilot_ide_chat.editors[].models[].total_engaged_users` |
| **Total Chats Initiated** | Total number of chat conversations started by users with this model | `copilot_ide_chat.editors[].models[].total_chats` |
| **Total Chat Insertion Events** | Number of times users accepted suggestions by clicking 'Insert Code' in chat | `copilot_ide_chat.editors[].models[].total_chat_insertion_events` |
| **Total Chat Copy Events** | Number of times users copied suggestions using keyboard or 'Copy' button | `copilot_ide_chat.editors[].models[].total_chat_copy_events` |

**Use Cases:**
- Compare engagement rates across different models
- Measure suggestion acceptance rates (insertions + copies vs. total chats)
- Identify which models drive more user interactions
---

## Copilot IDE Code Completions Metrics

Code completion metrics track how users accept or interact with inline code suggestions across different languages, editors, and models.

### A. General Metrics

| Metric | Description | API Property |
|---|---|---|
| **Total Engaged Users (Code Completions)** | Number of users who accepted **at least one** Copilot code suggestion across all editors (includes full and partial acceptances) | `copilot_ide_code_completions.total_engaged_users` |

### B. Language-Level Metrics

Breakdown of code completion adoption by programming language:

| Metric | Description | API Property |
|---|---|---|
| **Language Name** | Programming language used (e.g., Python, JavaScript, Java) | `copilot_ide_code_completions.languages[].name` |
| **Total Engaged Users for the Language** | Number of users who accepted at least one suggestion for this language (full or partial) | `copilot_ide_code_completions.languages[].total_engaged_users` |

**Use Case:** Identify which programming languages have the strongest Copilot adoption

### C. Editor-Level Metrics

Code completion engagement by IDE/editor:

| Metric | Description | API Property |
|---|---|---|
| **Editor Name** | IDE name (e.g., VS Code, IntelliJ IDEA, Visual Studio) | `copilot_ide_code_completions.editors[].name` |
| **Total Engaged Users for the Editor** | Number of users who accepted at least one suggestion in this editor (full or partial) | `copilot_ide_code_completions.editors[].total_engaged_users` |

**Use Case:** Compare code completion adoption across different IDEs in your organization

### D. Model-Level Metrics (Within Each Editor)

Detailed metrics for each AI model within an editor:

| Metric | Description | API Property |
|---|---|---|
| **Model Name** | AI model identifier ('default' for standard, or specific model name) | `copilot_ide_code_completions.editors[].models[].name` |
| **Is Custom Model** | Boolean flag indicating if this is a custom or default model | `copilot_ide_code_completions.editors[].models[].is_custom_model` |
| **Custom Model Training Date** | Date when the custom model was trained (null for default models) | `copilot_ide_code_completions.editors[].models[].custom_model_training_date` |
| **Total Engaged Users for the Model** | Users who accepted at least one suggestion with this model in this editor (full or partial) | `copilot_ide_code_completions.editors[].models[].total_engaged_users` |

### E. Model & Language Breakdown (Within Each Model)

Granular metrics showing the intersection of models and programming languages:

| Metric | Description | API Property |
|---|---|---|
| **Language Name** | Programming language for this breakdown | `copilot_ide_code_completions.editors[].models[].languages[].name` |
| **Total Engaged Users for the Language** | Users who accepted at least one suggestion for this language with this model (full or partial) | `copilot_ide_code_completions.editors[].models[].languages[].total_engaged_users` |
| **Total Code Suggestions** | Total number of code suggestions generated for this language/model combination | `copilot_ide_code_completions.editors[].models[].languages[].total_code_suggestions` |
| **Total Code Acceptances** | Number of suggestions accepted (full or partial acceptances) | `copilot_ide_code_completions.editors[].models[].languages[].total_code_acceptances` |
| **Total Code Lines Suggested** | Total lines of code suggested across all suggestions for this language/model | `copilot_ide_code_completions.editors[].models[].languages[].total_code_lines_suggested` |
| **Total Code Lines Accepted** | Total lines of code accepted by users for this language/model | `copilot_ide_code_completions.editors[].models[].languages[].total_code_lines_accepted` |

#### Key Calculations

From this granular data, you can calculate:

```
Acceptance Rate = Total Code Acceptances / Total Code Suggestions

Average Lines Per Suggestion = Total Code Lines Suggested / Total Code Suggestions

Average Lines Accepted Per Suggestion = Total Code Lines Accepted / Total Code Acceptances
```

> **Important Note:** To determine the overall number of accepted suggestions across all languages, sum the values from all instances of `total_code_acceptances` within the nested language objects.

---

## Copilot Dotcom Chat Metrics

Metrics for Copilot Chat usage on GitHub.com (outside of IDEs).

### A. General Metrics

| Metric | Description | API Property |
|---|---|---|
| **Total Engaged Users (Dotcom Chat)** | Total number of users who used Copilot Chat on GitHub.com | `copilot_dotcom_chat.total_engaged_users` |

### B. Model-Level Metrics

| Metric | Description | API Property |
|---|---|---|
| **Model Name** | Name of the AI model used | `copilot_dotcom_chat.models[].name` |
| **Is Custom Model** | Boolean flag indicating if this is a custom model | `copilot_dotcom_chat.models[].is_custom_model` |
| **Custom Model Training Date** | Date when the custom model was trained | `copilot_dotcom_chat.models[].custom_model_training_date` |
| **Total Engaged Users for the Model** | Users who used this model for Dotcom Chat | `copilot_dotcom_chat.models[].total_engaged_users` |
| **Total Chats** | Total number of chat conversations with this model | `copilot_dotcom_chat.models[].total_chats` |

---

## Copilot Dotcom Pull Requests Metrics

Metrics for Copilot-generated pull request summaries on GitHub.com.

### A. General Metrics

| Metric | Description | API Property |
|---|---|---|
| **Total Engaged Users (PR Summaries)** | Total number of users who used Copilot PR summaries | `copilot_dotcom_pull_requests.total_engaged_users` |

### B. Repository-Level Metrics

| Metric | Description | API Property |
|---|---|---|
| **Repository Name** | Name of the repository (format: owner/repo) | `copilot_dotcom_pull_requests.repositories[].name` |
| **Total Engaged Users for Repository** | Users who created PR summaries in this repository | `copilot_dotcom_pull_requests.repositories[].total_engaged_users` |

### C. Model-Level Metrics (Within Each Repository)

| Metric | Description | API Property |
|---|---|---|
| **Model Name** | Name of the AI model used | `copilot_dotcom_pull_requests.repositories[].models[].name` |
| **Is Custom Model** | Boolean flag indicating if this is a custom model | `copilot_dotcom_pull_requests.repositories[].models[].is_custom_model` |
| **Custom Model Training Date** | Date when the custom model was trained | `copilot_dotcom_pull_requests.repositories[].models[].custom_model_training_date` |
| **Total PR Summaries Created** | Number of pull request summaries generated | `copilot_dotcom_pull_requests.repositories[].models[].total_pr_summaries_created` |
| **Total Engaged Users for the Model** | Users who used this model for PR summaries | `copilot_dotcom_pull_requests.repositories[].models[].total_engaged_users` |

---

## Key Metrics Summary

### Chat Metrics Dashboard

| KPI | Metric | Formula |
|---|---|---|
| **Chat Adoption Rate** | % of engaged users using Copilot Chat | (Total Chat Users / Total Users) × 100 |
| **Chat Acceptance Rate** | % of chats that resulted in accepted suggestions | (Chat Insertions + Chat Copies) / Total Chats |
| **Editor Preference** | Most used editor for chat | Editor with highest total_engaged_users |
| **Model Preference** | Most used AI model | Model with highest total_engaged_users |

### Code Completion Metrics Dashboard

| KPI | Metric | Formula |
|---|---|---|
| **Code Completion Adoption** | % of users accepting suggestions | (Total Users Accepting / Total Users) × 100 |
| **Suggestion Acceptance Rate** | % of suggestions accepted | Total Acceptances / Total Suggestions |
| **Language Adoption** | Which languages are most supported | Languages by engaged_users count |
| **Productivity Gain** | Lines of code auto-completed | Total Code Lines Accepted |
| **Quality Metric** | Avg. suggestions per user | Total Suggestions / Total Engaged Users |

---

## Best Practices

### 1. Data Collection Intervals
- **Daily:** Track total engaged users and acceptance rates for trend analysis
- **Weekly:** Analyse language and model breakdowns to identify patterns
- **Monthly:** Review editor adoption and overall ROI metrics

### 2. Meaningful Metrics to Track
- **Adoption Rate:** % of team using Copilot features
- **Acceptance Rate:** % of suggestions actually used
- **Language Distribution:** Which languages benefit most
- **Editor Distribution:** Platform adoption rates
- **Productivity Impact:** Lines of code auto-completed

### 3. Avoid Common Pitfalls
- Don't confuse "total suggestions" with "valuable suggestions"
- Don't assume high acceptance rate = high productivity
- Don't ignore language/editor breakdowns when making rollout decisions
- Don't rely solely on metrics, combine with user feedback

### 4. Building Custom Dashboards
**Recommended visualisations:**
- Time-series adoption curves
- Acceptance rate by language
- Editor/model performance comparison
- Geographic or team-based breakdowns
- Retention and engagement trends

---

## Related Resources

- [GitHub Copilot Metrics API Documentation](https://docs.github.com/en/rest/copilot/copilot-metrics)
- [Reviewing User Activity Data](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/reviewing-activity-related-to-github-copilot-in-your-organization/reviewing-user-activity-data-for-copilot-in-your-organization)
- [Adoption Measurement Cheatsheet](./GHCP-adoption-measurement-cheatsheet.md)
- [Spreadsheet Usage Guide](./spreadsheet-usage.md)

---

*Last updated: January 2026*



