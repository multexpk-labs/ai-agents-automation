# Tool Design

Good tools are narrow, explicit, and testable.

## Tool Contract
```text
name
description
input schema
permission level
timeout
failure behavior
output schema
```

Avoid a single unrestricted tool such as `execute_anything`. Prefer purpose-specific tools with limited permissions.

## Validation
Validate types, ranges, required fields, authorization, and target resources before execution.