---
id: 002
title: git-workflow-commit-pr
stage: misc
date: '2026-01-06'
surface: agent
model: Claude Sonnet 4.5
feature: cli-calculator
branch: 001-cli-calculator
user: Sheikh Mohammad
command: /sp.git.commit_pr
labels:
  - git
  - commit
  - pull-request
  - workflow
files:
  - specs/001-cli-calculator/spec.md
  - specs/001-cli-calculator/checklists/requirements.md
  - history/prompts/cli-calculator/1-cli-calculator-spec.spec.prompt.md
tests: []
links:
  spec: specs/001-cli-calculator/spec.md
  ticket: null
  adr: null
  pr: https://github.com/sheikh-mohammad/basic-calculator/pull/new/001-cli-calculator
---

# PHR: git-workflow-commit-pr

## Input

```
/sp.git.commit_pr
```

## Response

Executed complete Git workflow to commit specification changes and create pull request:

1. Analyzed repository state and detected new specification files
2. Added all new files to staging:
   - specs/001-cli-calculator/spec.md
   - specs/001-cli-calculator/checklists/requirements.md
   - history/prompts/cli-calculator/1-cli-calculator-spec.spec.prompt.md
3. Created commit with message: "feat(calculator): create CLI calculator specification"
4. Pushed changes to remote with upstream tracking
5. Since gh CLI not available, provided manual PR creation URL

The specification for the CLI calculator is now committed and ready for review via pull request.

## Outcome

Git workflow completed successfully. Specification files committed to branch 001-cli-calculator and pushed to remote. Ready for pull request review.