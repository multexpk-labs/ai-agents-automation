# Human Approval

Sensitive actions should support an approval boundary.

```text
Agent proposes action
        |
        v
Validation
        |
        v
Human approval
     /       \
 Approved   Rejected
    |          |
 Execute     Report
```

Examples include deleting resources, sending external messages, changing production configuration, making purchases, or modifying customer data.