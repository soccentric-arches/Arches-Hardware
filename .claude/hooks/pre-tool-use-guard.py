#!/usr/bin/env python3
"""PreToolUse hook — enforce this repo's READ-ONLY status.

Arches-Hardware is the board design source of truth (schematics, PCB, BOM),
owned by a human hardware engineer. `status: readonly` in the master repo's
loop/fleet-deps.yaml means no agent writes file content here, ever — listing
this repo in a loop's repos: is a scope violation, and this hook is the same
rule enforced locally for a session rooted in this repo.

The only writable area is .claude/ itself (docs/skills about the repo), and
even that asks first.
"""
import json
import sys

PATH_KEYS = {"filePath", "file_path", "path", "notebook_path"}


def find_paths(obj):
    found = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in PATH_KEYS and isinstance(v, str):
                found.append(v)
            else:
                found.extend(find_paths(v))
    elif isinstance(obj, list):
        for item in obj:
            found.extend(find_paths(item))
    return found


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        print(json.dumps({"continue": True}))
        return

    tool = payload.get("tool_name") or payload.get("toolName") or ""
    if tool not in ("Edit", "Write", "NotebookEdit", "MultiEdit"):
        print(json.dumps({"continue": True}))
        return

    for p in find_paths(payload.get("tool_input") or payload.get("toolInput") or {}):
        norm = p.replace("\\", "/")
        if "/.claude/" in norm or norm.startswith(".claude/"):
            print(json.dumps({
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "ask",
                    "permissionDecisionReason": (
                        ".claude/ is the one writable area of this read-only "
                        "repo. Confirm this is documentation, not design data."
                    ),
                }
            }))
            return
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": (
                    f"Arches-Hardware is READ-ONLY (human-owned board design "
                    f"source of truth). Refusing to write '{p}'. Design changes "
                    "belong to the hardware engineer; the Loop Engine treats "
                    "this repo in a loop's repos: as a scope violation."
                ),
            }
        }))
        return

    print(json.dumps({"continue": True}))


if __name__ == "__main__":
    main()
