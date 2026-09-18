# Example Agent Workflow

## Task
Process a user request that requires a controlled external lookup.

## Flow
```text
1. Validate request
2. Decide whether a tool is required
3. Build structured tool arguments
4. Validate arguments
5. Execute read-only tool
6. Inspect result
7. Produce response
```

For write operations, insert a human approval step before execution.