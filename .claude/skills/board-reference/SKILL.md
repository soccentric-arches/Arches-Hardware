---
name: board-reference
description: "Use when: answering questions about the Arches board design — schematics, PCB layout, BOM, connector pinouts, power rails, the Jetson module or STM32 co-processor wiring — or when another repo's work (HAL modules, Configuration board manifests, OS device trees) needs a hardware fact checked against the design source of truth."
---

# Arches-Hardware — reading the board design (never writing it)

This repo is the design source of truth for the Arches board: an NVIDIA Jetson
(Tegra, L4T/JetPack) application processor paired with an STM32 real-time
co-processor. It is **read-only for every agent** — owned by a human hardware
engineer, `status: readonly` in the fleet graph, and a scope violation in any
loop. You consult it; you never modify it.

## What you can legitimately do here

- **Answer hardware questions for other repos.** The common consumers:
  - `Arches-HAL` — a module author needs to know what a hardware block actually
    is (which CAN transceiver, which NVMe slot wiring, which GPIO bank).
  - `Arches-Configuration` — `board-manifests/arches.json` encodes hardware
    knowledge (STM32 MCU panel, CAN, cameras, GPU tiles) redundantly with the
    design; when manifest and design disagree, the design wins and the manifest
    is the bug.
  - `Arches-OS` — device tree / carrier-board questions.
- **Cross-check a BOM or connector fact** before someone writes software
  against a wrong assumption.
- **Flag inconsistencies to the human** — as findings, never as edits.

## Current state — don't over-promise

Content is sparse today: a README template, no committed design files yet. If
asked something the repo cannot answer, say that the design data hasn't been
committed here rather than inferring from the Jetson's general documentation —
carrier-board wiring is exactly where generic Jetson knowledge goes wrong.

## Rules

- No file writes outside `.claude/`, and those only for documentation. The
  PreToolUse hook denies everything else; do not route around it with Bash.
- No commits, no pushes (denied in settings). The hardware engineer owns
  history here.
- The repo still receives the fleet-wide `feature/<slug>` branch during loops —
  read-only governs file *content*, not refs. Don't be surprised by branches.
- Never list this repo in a loop's `repos:` — `make loop-lint` in the master
  repo flags it and the scope-check rejects it.
