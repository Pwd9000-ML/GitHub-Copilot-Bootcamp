# Weekly GitHub Copilot Check-in and Scorecard Template Guide

## Overview

This guide walks you through using the **GitHub Copilot Weekly Capture Scorecard Template** to systematically track adoption, effectiveness, and team satisfaction with GitHub Copilot during your weekly team meetings.

> **Time commitment:** ~60 to 90 seconds per person per week
> 
> **Goal:** Build a lightweight, data-driven feedback loop without adding process overhead

## Table of Contents

- [The Weekly Check-in Format](#the-weekly-check-in-format)
- [How the Excel Template Works](#-how-the-excel-template-works)
- [Scoring System](#-scoring-system)
- [Implementation Roadmap](#-implementation-roadmap)
- [Tips for Success](#-tips-for-success)

---

## The Weekly Check-in Format

### Core Questions (5 Questions + 1 Optional)

Run through these **5 core questions** once per week during your team meeting:

| # | Question | Response Format |
|---|---|---|
| **1** | Used GHCP since last standup? | Yes / No |
| **2** | What did you use it for (top 1–2)? | Feature, Bug fix, Unit tests, Documentation, Refactor, DevOps-IaC, Learning, Other |
| **3** | Net time impact (quick estimate) | Minutes saved (+) or wasted (-) |
| **4** | Helpfulness rating + confidence | 1–5 scale + High/Med/Low confidence |
| **5** | Top pain point category | Choose one + optional note |
| **(6)** | *(Optional)* Rework needed? | None / Some / A lot |

### Optional Rotating Questions

Rotate these **supplementary questions weekly**:

- "Did you verify the suggestion with tests / docs / source?" (Yes/No)
- "Did GHCP help you understand unfamiliar code faster?" (Yes/No + 1 line)
- "Any security/compliance concern triggered?" (Yes/No)
---

## How the Excel Template Works

### Template Tabs (5 Worksheets)

| Tab | Purpose | Who Uses It |
|---|---|---|
| **Weekly Capture** | Live data entry | Scrum Master records one row per person per week during meeting |
| **Sprint Summary** | Aggregated reporting | Team Lead filters by Sprint/Team, auto-calculates KPIs |
| **Scorecard** | Overall performance | Leadership views 0 to 100 scores and rollups |
| **Dashboard** | Visual analytics | All stakeholders see charts and topline metrics |
| **Lists** | Data validation | Admin configures dropdown values for pain points and use types |

### Workflow

1. Scrum Master opens Weekly Capture sheet
2. Adds one row per person per week
3. During the weekly meeting, ask the 5 core questions
4. Records responses in columns
5. Sheet auto-populates Sprint Summary and Scorecard
6. Dashboard refreshes for quick metrics

---

## Scoring System

The template calculates an **Overall Health Score (0 to 100)** with four weighted components:

| Component | Weight | Metric |
|---|---|---|
| **Adoption** | 30% | Percentage of team using GHCP |
| **Time Impact** | 30% | Normalized net minutes per person per week (capped at plus or minus 60) |
| **Sentiment** | 20% | Average helpfulness rating (1 to 5) |
| **Rework Quality** | 20% | Penalty if "Some" or "A lot" rework is reported |

### Example Score Breakdown

```
Adoption (75 percent x 30):       22.5 points
Time Impact (plus 20 minutes x 30): 22.5 points
Sentiment (4.0 out of 5 x 20):     16.0 points
Rework Quality (85 percent x 20):  17.0 points
Overall Score = 78 out of 100 (Good)
```

### Customizing in Scorecard Tab

**Edit blue cells to adjust:**

- Weight percentages (must sum to 100%)
- Time cap (default ±60 minutes)
- Rework penalty thresholds
---

## Implementation Roadmap

### Week 1: Soft Launch

- Run check-in once per week, for example, on **Friday**
- Prevents survey fatigue while gathering initial feedback
- Refine pain point categories and question phrasing

**Scrum Master Action:**
```
"Before we wrap up: Copilot check-in, used it? For what? 
Net minutes? Helpfulness and confidence? Pain point? Rework needed?"
```

### Week 2 Onward: Sustain Weekly Rhythm

- Continue **weekly check-ins** on the same day each week
- Data volume accumulates, patterns become clearer over time
- Team gets into rhythm, 60 to 90 seconds becomes routine

**Success Indicators:**
- Team meeting remains on schedule
- Team treats check-in as normal part of weekly meeting
- Participation rate exceeds 80%

### Quick Scrum Master Script (10 seconds)

> "Before we wrap up: Copilot check-in, used it? For what? Net minutes? Helpfulness and confidence? Pain point? Any rework needed?"

**Tone:** Casual, conversational. Not formal.

---

## Tips for Success

### Make It Psychologically Safe

**Do:**
- Normalize negative time ("Taking longer is valuable data, helps us find blockers")
- Frame as **process improvement**, not performance review
- Celebrate learning moments even without time savings

**Don't:**
- Use data for individual performance reviews
- Judge low satisfaction scores
- Dismiss negative feedback as "user error"

**Key Message:**
> "Negative time is allowed. It helps us fix real blockers, verify legitimacy, reduce hallucinations, and keep the human in the loop always."

### Data Quality Best Practices

| Principle | Action |
|---|---|
| **Trend over Perfection** | Time saved is a rough estimate. Track trends, not exact minutes. |
| **Keep It Brief** | Responses taking more than 10 seconds, offer as follow-up, not in the meeting. |
| **Consistent Format** | Same questions every week so team expects it and data stays comparable. |
| **Act on Feedback** | Review pain points weekly and show you are responding. |

### Pain Point Categories (Suggested)

Configure these in the **Lists tab** dropdown:

- Accuracy and Hallucinations
- Context awareness (missing relevant code)
- Latency and Performance
- Documentation and Setup issues
- IDE and Extension bugs
- Learning curve and UX confusion
- Security and Compliance concerns
- Other

---

## Dashboard Patterns to Watch

### High Adoption and High Rework - Investigate

**Meaning:** Team engaged but low-quality suggestions  
**Action:** Review model selection, provide context training, check accuracy

### Low Adoption and Low Time Savings - Opportunity

**Meaning:** Team not using Copilot, needs better training  
**Action:** Workshop, share success stories, unblock pain points

### High Adoption and Consistent Savings - Scale

**Meaning:** Copilot delivering real value  
**Action:** Expand to teams, document best practices, invest in advanced features

### Declining Sentiment - Early Warning

**Meaning:** Satisfaction dropping despite high adoption  
**Action:** Investigate pain point changes, gather feedback, update training

---

## Related Resources

- **[GHCP API Metrics](./GHCP-API-Metrics.md)** - System-level usage data from GitHub
- **[Adoption Measurement Cheatsheet](./GHCP-adoption-measurement-cheatsheet.md)** - Broader adoption KPIs
- **[Spreadsheet Usage Guide](./spreadsheet-usage.md)** - Excel tips and advanced formulas

---

## Getting Started Checklist

- [ ] Download and customize Excel template (blue cells)
- [ ] Meet with Scrum Masters to review questions
- [ ] Populate **Lists tab** with pain point categories
- [ ] Run practice round on chosen day (Week 1)
- [ ] Brief team: explain purpose and emphasize psychological safety
- [ ] Week 1: Run once per week on chosen day
- [ ] Review Sprint Summary after Week 1
- [ ] Week 2 onward: Continue weekly cadence, monitor participation
- [ ] Weekly: Review Dashboard for top 2 to 3 insights
- [ ] Monthly: Share summary with leadership and team

---

*Last updated: January 2026*

