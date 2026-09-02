# STM32 real-time co-processor

The Arches board pairs an NVIDIA Jetson application processor with an **STM32
real-time co-processor** on the custom carrier (see
`.claude/skills/board-reference/SKILL.md`). This folder is the single point of
source for the STM32 side of that design.

## Role

- Real-time control: MCU GPIO panel, CAN bus, and other latency-critical I/O
  that must not run on the Jetson (Linux) side.
- Consumed by:
  - **Arches-HAL** — module authors need the actual hardware blocks (which CAN
    transceiver, which GPIO bank).
  - **Arches-Configuration** — board-manifests encode the STM32 MCU panel, CAN,
    cameras; when the manifest and the design disagree, **the design wins**.
  - **Arches-OS** — device-tree / carrier-board questions.

## Jetson ↔ STM32 contract

`VERIFY` — pin the exact STM32 part, bus wiring (CAN transceiver, UART/SPI/I2C
link to the Jetson), and power rails here as the carrier design is committed.
Do not infer carrier wiring from generic documentation.

## Artifacts

- `schematics/` — STM32 section of the carrier schematic (revisioned)
- `pcb/` — layout/fab outputs for the STM32 section
- `bom/` — STM32, transceivers, support components
- `datasheets/` — STM32 datasheets/reference manuals, transceiver datasheets

Design files are owned by the human hardware engineer; nothing is committed
here yet.
