# Git Commands Quick Reference

## Basic Update Workflow
```bash
# 1. Check status
git status

# 2. Add changes
git add .                    # Add all files
git add README.md           # Add specific file

# 3. Commit changes
git commit -m "Your message here"

# 4. Push to GitHub
git push
```

## Commit Message Convention
```bash
# Bug fixes
git commit -m "🐛 Fix [description]"

# New features
git commit -m "✨ Add [feature name]"

# Documentation updates
git commit -m "📖 Update [what was updated]"

# Code improvements
git commit -m "♻️ Refactor [what was refactored]"

# Performance improvements
git commit -m "⚡ Improve [what was improved]"

# Breaking changes
git commit -m "💥 BREAKING: [description]"
```

## Release Workflow
```bash
# Create new release
git tag -a v1.1.0 -m "🚀 Version 1.1.0 Release Notes"
git push origin v1.1.0

# This triggers GitHub Actions to:
# - Build new executable
# - Create release with download
# - Generate release notes
```

## Useful Commands
```bash
# View commit history
git log --oneline

# See differences in files
git diff

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo changes to a file
git checkout -- filename.py

# Pull latest changes from GitHub
git pull
```

## Branch Management (Advanced)
```bash
# Create new feature branch
git checkout -b feature/new-feature

# Switch back to main
git checkout main

# Merge feature branch
git merge feature/new-feature

# Delete branch
git branch -d feature/new-feature
```
