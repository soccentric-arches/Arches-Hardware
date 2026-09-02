# Jetson TX2 NX (module P3449-0000 — doc lists P3636, `VERIFY`)

| Item | Value |
|---|---|
| Family / branch | `tx` · L4T R32.7.x · JetPack 4.6.x |
| Module P/N | P3449-0000 (`VERIFY`; branching doc §5.2 lists P3636) |
| Dev kit / carrier | P3509 carrier / Nano dev kit carrier |
| Flash config (L4T) | `jetson-tx2-nx-devkit` — `VERIFY` |
| Yocto MACHINE | `jetson-tx2-nx-devkit` — `VERIFY` |

## Hardware specifications

| Spec | Value |
|---|---|
| SoC | NVIDIA Tegra X2 (T186) |
| CPU | Dual Denver 2 + Quad Cortex-A57 (`VERIFY` clocks) |
| GPU | Pascal GP10B, 256 CUDA cores |
| Memory | 4 GB 128-bit LPDDR4, 51.2 GB/s (`VERIFY`) |
| Storage | 16 GB eMMC 5.1 (`VERIFY`) |
| Power modes | 7.5 W / 15 W |

## Interfaces / I/O

| Interface | Value |
|---|---|
| Camera | MIPI CSI-2 (`VERIFY` lane count) |
| USB | USB 3.x + USB 2.0 ports (`VERIFY`) |
| Ethernet | GbE MAC |
| Display | HDMI 2.0 + DP 1.2 |
| Low-speed | UART, I2C, I2S, SPI, PWM, GPIO |
| Form factor | 260-pin SODIMM, 69.6 × 45 mm (same footprint family as Orin NX/Nano) |

## Internal hardware

On-module PMIC/sequencer, eMMC boot (BCT → CBoot). No on-module WiFi/BT
(`VERIFY`) — add via carrier M.2 Key E.

## How to load the OS

- Force Recovery, then: `sudo ./flash.sh jetson-tx2-nx-devkit mmcblk0p1` (`VERIFY`
  exact config name in L4T R32.7.x)
- Arches `tx` branch image; legacy tegraflash path.

## How to log in

Default `nvidia`/`nvidia` on stock images (change it); serial console 115200 8N1;
SSH via `192.168.55.1` on USB device mode.

## Module connector — 260-pin SODIMM

260-pin SO-DIMM (69.6 × 45 mm class, same footprint family as Jetson Nano /
Orin NX / Orin Nano). Full pin list: Jetson TX2 NX Pin and Function Names
Guide (DA-10697-001) — add to `datasheets/`. `VERIFY` module connector
mapping against that guide (TX2 NX is **not** pin-compatible with the P2597
TX2 carrier).

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/`
