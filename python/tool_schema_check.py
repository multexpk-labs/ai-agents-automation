#!/usr/bin/env python3
import json
import sys

def main():
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} tool.json')
        return 2
    with open(sys.argv[1], encoding='utf-8') as fh:
        tool = json.load(fh)
    required = ['name', 'description', 'input_schema']
    missing = [key for key in required if key not in tool]
    if missing:
        print(json.dumps({'valid': False, 'missing': missing}, indent=2))
        return 1
    print(json.dumps({'valid': True, 'name': tool['name']}, indent=2))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())