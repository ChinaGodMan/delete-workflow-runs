<div align="right">
    <h6>
        <picture>
            <source type="image/svg+xml" media="(prefers-color-scheme: dark)" srcset="https://assets.aiwebextensions.com/images/icons/earth/white/icon32.svg">
            <img height=14 src="https://assets.aiwebextensions.com/images/icons/earth/black/icon32.svg">
        </picture>
        &nbsp;English |
        <a href="README_zh.md">简体中文</a>
    </h6>
</div>

# Delete Workflow Runs

A script and workflow for automating the cleanup of GitHub Actions workflow run records, supporting batch deletion across multiple repositories.

## Introduction

- **Supports manual triggers and scheduled tasks**: You can manually trigger the workflow or set up a schedule for automatic execution.
- **Supports multiple repositories**: By configuring environment variables, you can clean up workflow run records for multiple repositories at once.
- **Easy to use**: Requires minimal configuration with no complex setup.

## Configuration

### 1. Environment Variables

The following environment variables need to be set in GitHub Secrets:

| Variable Name  | Description                                                                           |
| -------------- | ------------------------------------------------------------------------------------- |
| `GITHUB_TOKEN` | GitHub Personal Access Token with `repo` and `workflow` permissions.                  |
| `REPO_OWNER`   | Repository owner username (typically your GitHub username or org name).               |
| `REPO_NAME`    | Names of repositories to clean up, separated by commas (e.g., `repoa,repob,repoccc`). |

### 2. Scheduled Tasks

The `schedule` in the workflow uses a [cron expression](https://crontab.guru) for configuration. By default, it is set to run daily at midnight (UTC time).

```yaml
on:
  schedule:
    - cron: "0 0 * * *" # Executes daily at 00:00 UTC
```
