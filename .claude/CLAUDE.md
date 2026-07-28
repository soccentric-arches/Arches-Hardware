# Arches-Hardware

**Remote:** `git@github.com:SiliconCentric/Arches-Hardware.git`
**Parent project:** [Arches](../Arches.md) (target hardware: **NVIDIA Jetson** (Tegra family, L4T/JetPack OS) application processor with an **STM32** real-time co-processor.)
**Leaf type:** `<Project>-Hardware`
**Status:** READ-ONLY — human-owned (`status: readonly` in `loop/fleet-deps.yaml`)

A **board design source of truth** leaf (schematics, PCB layout, BOM, manufacturing artifacts), owned by a human hardware engineer. Content is sparse today — a README template and no design files yet — but this is not a stub awaiting automation: it is deliberately outside the engine's write path.

**For the Loop Engine:** listing this repo in a loop's `repos:` is a scope violation, and it has no `.claude/validate.sh` because it has no build. It *does* receive the fleet-wide feature branch like every other repo (spec §8.2) — read-only governs file content, not refs.

---
Part of the `Arches` project in the `project-managers` fleet. See `docs/project-managers.md` for the full 9-project / 8-leaf hierarchy and shared conventions.
