# Arches-Hardware

Hardware-definition repository for the **Arches** platform. Single point of source
for all hardware supported by the Arches system:

- **NVIDIA Jetson** — every SOM and developer kit across the four supported
  generations (`tx`, `xavier`, `orin`, `thor`)
- **STM32** — the real-time co-processor on the Arches carrier

Human-owned (`status: readonly` in the fleet dependency graph): design files are
committed by the hardware engineer; the fleet automation never writes here.

## Layout

```
boards/nvidia/<family>/{som,devkit}/<board>/README.md
    One README per NVIDIA board — identity (P/Ns, flash config, MACHINE),
    hardware specs, I/O/GPIO tables, memory/storage, power/thermal,
    internal hardware, how to load the OS, how to log in.
    Artifact subfolders: schematics/ pcb/ bom/ datasheets/

mcu/stm32/README.md
    STM32 real-time co-processor: role, Jetson↔STM32 contract, artifacts.

arches-yocto-generation-branching-requirements.md
    The generation-branching spec that defines the family coverage matrix
    (§5), upstream pins (§5.1), and the no-invention rule (§9.4).
```

Families mirror the Arches Yocto build branches — generations are
BSP-incompatible, so hardware knowledge stays inside its family folder.

## Key references

- `boards/README.md` — folder conventions, what each board README contains
- `boards/nvidia/README.md` — family → branch → L4T/JetPack → `meta-tegra` pin matrix
- `.claude/skills/board-reference/SKILL.md` — how agents may consume (never
  modify) the board design; design wins over board manifests

## Status

Board READMEs are complete for specs/I/O/flash/login; schematic, PCB, and BOM
artifacts are placeholders until the hardware owner commits design files. Any
value that could not be verified is flagged `VERIFY` in place — do not resolve
it by invention.