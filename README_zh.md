<div align="right">
    <h6>
        <picture>
            <source type="image/svg+xml" media="(prefers-color-scheme: dark)" srcset="https://assets.aiwebextensions.com/images/icons/earth/white/icon32.svg">
            <img height=14 src="https://assets.aiwebextensions.com/images/icons/earth/black/icon32.svg">
        </picture>
        &nbsp;简体中文 |
        <a href="README.md">English</a>
    </h6>
</div>

# Delete Workflow Runs

一个用于清理 GitHub Actions 工作流运行记录的自动化脚本和工作流，支持批量删除多个仓库的工作流运行记录。

## 简介

- **支持手动触发和定时任务**：可通过手动触发工作流或设置定时任务自动运行。
- **支持多个仓库**：通过配置环境变量，可一次性清理多个仓库的工作流运行记录。
- **使用简单**：无需复杂操作，只需少量配置即可运行。

## 配置说明

### 1. 环境变量

以下环境变量需要设置在 GitHub Secrets 中：

| 变量名称       | 说明                                                                   |
| -------------- | ---------------------------------------------------------------------- |
| `GITHUB_TOKEN` | GitHub 个人访问令牌，需包含 `repo` 和 `workflow` 权限。                |
| `REPO_OWNER`   | 仓库所有者用户名（通常是你的 GitHub 用户名或组织名）。                 |
| `REPO_NAME`    | 需要清理的仓库名称，多个仓库用逗号分隔（例如 `repoa,repob,repoccc`）。 |

### 2. 定时任务

工作流中的 `schedule` 使用 [cron 表达式](https://crontab.guru) 配置，默认设置为每天 UTC 时间凌晨 00:00 运行。

```yaml
on:
  schedule:
    - cron: "0 0 * * *" # UTC 时间每天凌晨 00:00 执行
```
