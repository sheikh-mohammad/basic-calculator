---
id: 002
title: Update CLAUDE Instructions For Atomic Commits
stage: general
date: 2026-01-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: Claude Sonnet 4.5
command: manual edit
labels: [claude-instructions, atomic-commits, workflow]
links:
  spec: null
  ticket: null
  adr: null
  pr: https://github.com/sheikh-mohammad/basic-calculator/pull/1
files:
 - CLAUDE.md
tests:
 - none
---

## Prompt

Now change the CLAUDE.md to run `/sp.git_commit_pr` for atomic commits when a single and and small change is made in the repo so run the above command

## Response snapshot

Updated the CLAUDE.md file to include instruction for running `/sp.git_commit_pr` for atomic commits when making small changes. Added the instruction to the Default policies section: "For atomic commits with small changes, run `/sp.git_commit_pr` to ensure proper commit and pull request creation."

## Outcome

- ✅ Impact: CLAUDE.md updated with atomic commit instruction
- 🧪 Tests: No tests added in this task
- 📁 Files: Modified CLAUDE.md
- 🔁 Next prompts: Continue with development following updated instructions
- 🧠 Reflection: Instructions now include proper workflow for atomic commits

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - Instruction added to CLAUDE.md
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Follow the updated workflow for future commits