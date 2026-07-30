# Arches-Hardware

Board design source of truth: schematics, PCB layout, BOM, manufacturing artifacts. Human-owned,
read-only, outside the engine's write path.

## Do

* Treat every file here as human-owned. A hardware engineer owns this repo, not the fleet automation.

## Don't

* **Don't write anything outside `.claude/`.** The `PreToolUse` hook denies it — read-only is enforced here, not merely documented.
* **Don't list this repo in a loop's `repos:`.** That is a scope violation. It has no build and no validation gate.
* **Don't assume read-only means no branch.** It receives the fleet-wide feature branch like every other repo. Read-only governs file content, not refs.
