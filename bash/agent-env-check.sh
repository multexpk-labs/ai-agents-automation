#!/usr/bin/env bash
set -u

echo '=== AI AGENT ENVIRONMENT ==='
echo "Host: $(hostname)"
echo "Kernel: $(uname -r)"
echo
echo '--- Runtime ---'
command -v python3 || true
command -v node || true
command -v curl || true
echo
echo '--- Network ---'
ss -lnt 2>/dev/null || true
echo
echo '--- Memory ---'
free -h 2>/dev/null || true