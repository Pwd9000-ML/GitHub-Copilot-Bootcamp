# DORA Metrics Cheat Sheet

DORA (DevOps Research and Assessment) metrics are key performance indicators for software delivery and operational performance.

## The Four Key Metrics

### 1. Deployment Frequency

**Definition**: How often your organization successfully releases to production.

**Measurement**:
- Count deployments per day/week/month
- Track via CI/CD pipeline logs
- GitHub Actions workflow runs

**Benchmarks**:
- **Elite**: Multiple deploys per day
- **High**: Once per day to once per week
- **Medium**: Once per week to once per month
- **Low**: Once per month to once every 6 months

**How to Improve**:
- Automate deployment pipeline
- Reduce batch size
- Implement feature flags
- Use trunk-based development

**GitHub Actions Example**:
```yaml
# Track deployments in workflow
- name: Record Deployment
  run: |
    echo "Deployment completed at $(date)"
    # Send metrics to monitoring system
```

---

### 2. Lead Time for Changes

**Definition**: Time from code commit to code successfully running in production.

**Measurement**:
- Time from commit to production deployment
- Track: commit timestamp → deployment completion

**Benchmarks**:
- **Elite**: Less than one hour
- **High**: One day to one week
- **Medium**: One week to one month
- **Low**: One month to six months

**How to Improve**:
- Optimize CI/CD pipeline
- Reduce code review time
- Automate testing
- Parallelize build steps
- Use GitHub Copilot to accelerate development

**Calculation**:
```
Lead Time = Production Deployment Time - First Commit Time
```

---

### 3. Time to Restore Service

**Definition**: How long it takes to recover from a failure in production.

**Measurement**:
- Time from incident detection to resolution
- Track: alert triggered → service restored

**Benchmarks**:
- **Elite**: Less than one hour
- **High**: Less than one day
- **Medium**: One day to one week
- **Low**: One week to one month

**How to Improve**:
- Implement comprehensive monitoring
- Create runbooks for common issues
- Practice incident response
- Automate rollback procedures
- Maintain good documentation

**Incident Response Template**:
```markdown
## Incident Timeline
- **Detected**: YYYY-MM-DD HH:MM
- **Team Notified**: YYYY-MM-DD HH:MM
- **Investigation Started**: YYYY-MM-DD HH:MM
- **Root Cause Identified**: YYYY-MM-DD HH:MM
- **Fix Deployed**: YYYY-MM-DD HH:MM
- **Service Restored**: YYYY-MM-DD HH:MM

**Total Time to Restore**: X hours Y minutes
```

---

### 4. Change Failure Rate

**Definition**: Percentage of deployments that result in degraded service and require remediation.

**Measurement**:
- (Failed Deployments / Total Deployments) × 100

**Benchmarks**:
- **Elite**: 0-15%
- **High**: 16-30%
- **Medium**: 31-45%
- **Low**: 46-60%

**How to Improve**:
- Increase test coverage
- Implement automated testing
- Use canary deployments
- Conduct code reviews
- Monitor production closely
- Use GitHub Advanced Security

**Tracking Example**:
```bash
# Total deployments this month: 100
# Failed deployments: 5
# Change Failure Rate: 5%
```

---

## Tracking DORA Metrics with GitHub

### Using GitHub Actions

**Track Deployment Frequency**:
```yaml
name: Track Deployment
on:
  workflow_run:
    workflows: ["Deploy to Production"]
    types: [completed]

jobs:
  record:
    runs-on: ubuntu-latest
    steps:
      - name: Record Deployment Metric
        run: |
          echo "Deployment completed at $(date)"
          # Send to metrics system
```

### Using GitHub API

**Query Deployments**:
```bash
# Get all deployments
curl -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/OWNER/REPO/deployments
```

### Using GitHub Insights

- Use **Insights** → **Pulse** for activity overview
- Use **Insights** → **Network** for branch activity
- Use **Actions** tab for deployment frequency

---

## Implementing DORA Metrics in Your Bootcamp

### Week 1: Establish Baseline
- Set up deployment pipeline
- Start tracking metrics
- Document current state

### Week 2: Improve Testing
- Increase test coverage
- Automate security scanning
- Reduce change failure rate

### Week 3: Optimize Pipeline
- Parallelize tests
- Optimize build times
- Reduce lead time

### Week 4: Monitor and Iterate
- Review metrics
- Identify bottlenecks
- Plan improvements

---

## DORA Metrics Dashboard Template

Create a simple dashboard to track your metrics:

```markdown
## DORA Metrics - [Month/Year]

### Deployment Frequency
- **This Week**: 15 deployments
- **Average**: 2.1 per day
- **Trend**: ↑ +20% from last month

### Lead Time for Changes
- **Average**: 4.2 hours
- **Median**: 3.1 hours
- **Trend**: ↓ -15% from last month

### Time to Restore Service
- **Incidents This Month**: 2
- **Average Recovery Time**: 45 minutes
- **Longest Incident**: 1.5 hours

### Change Failure Rate
- **Total Deployments**: 100
- **Failed Deployments**: 8
- **Failure Rate**: 8%
- **Trend**: ↓ -3% from last month

### Performance Level: HIGH ⭐
```

---

## Tools for Measuring DORA Metrics

### Free/Open Source
- **GitHub Actions** - Built-in deployment tracking
- **Grafana** - Visualization
- **Prometheus** - Metrics collection

### Commercial
- **Sleuth** - DORA metrics platform
- **LinearB** - Engineering intelligence
- **Velocity by Code Climate** - Engineering metrics

### DIY Approach
```python
# Simple script to calculate metrics
import requests
from datetime import datetime, timedelta

def get_deployment_frequency(repo, days=7):
    # Query GitHub API for deployments
    deployments = get_deployments(repo, days)
    return len(deployments) / days

def get_lead_time(repo, deployment_id):
    # Calculate time from first commit to deployment
    deployment = get_deployment(deployment_id)
    first_commit = get_first_commit(deployment)
    return (deployment.time - first_commit.time).hours
```

---

## Best Practices

1. **Start Simple**: Don't try to perfect all metrics at once
2. **Automate Collection**: Manual tracking is error-prone
3. **Focus on Trends**: Absolute numbers matter less than improvement
4. **Team Ownership**: Make metrics visible to the team
5. **Continuous Improvement**: Use metrics to drive decisions
6. **Context Matters**: Compare yourself to your past, not others

---

## Resources

- [DORA Research](https://www.devops-research.com/research.html)
- [State of DevOps Report](https://services.google.com/fh/files/misc/state-of-devops-2021.pdf)
- [Accelerate Book](https://itrevolution.com/book/accelerate/)
- [GitHub Blog: DORA Metrics](https://github.blog/2023-02-02-measuring-productivity-the-right-way-with-dora-metrics/)

---

## Bootcamp Exercise

**Task**: Calculate your team's DORA metrics for the bootcamp period.

1. Set up tracking in GitHub Actions
2. Record metrics weekly
3. Calculate averages
4. Identify improvement areas
5. Present findings in Week 4

**Deliverable**: A DORA metrics report showing your bootcamp progress.
