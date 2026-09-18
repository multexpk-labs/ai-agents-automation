# Agent Architecture

A practical agent separates model reasoning from application control.

```text
User Request
    |
    v
Agent Controller
    |
    +--> LLM
    |
    +--> Tool Registry
             |
             +--> Read APIs
             +--> Write APIs
             +--> Automation
             +--> Human Approval
```

The controller should enforce permissions, validation, timeouts, retries, and logging.