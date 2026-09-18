# Agent Reliability

Agent systems can fail at the model, tool, network, application, or workflow layer.

Use bounded retries and distinguish transient failures from permanent failures.

```text
Request -> Validate -> Execute -> Verify -> Continue
                     |
                  Failure
                     |
              Retry / Fallback / Stop
```

Every external action should have a clear timeout and failure path.