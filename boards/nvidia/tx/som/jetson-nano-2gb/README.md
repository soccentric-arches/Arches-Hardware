# Jetson Nano 2GB (module P3448-0003)

| Item | Value |
|---|---|
| Family / branch | `tx` · L4T R32.7.x · JetPack 4.6.x |
| Module P/N | P3448-0003 |
| Dev kit / carrier | P3541 dev kit |
| Flash config (L4T) | `jetson-nano-2gb-devkit` (image written to microSD) |
| Yocto MACHINE | `jetson-nano-2gb-devkit` — `VERIFY` |

## Hardware specifications

| Spec | Value |
|---|---|
| SoC | NVIDIA Tegra X1 (T210) |
| CPU | Quad-core Arm Cortex-A57 @ 1.4 GHz |
| GPU | Maxwell, 128 CUDA cores @ ~614 MHz (`VERIFY` exact clock/GFLOPS) |
| Memory | 2 GB 64-bit LPDDR4 (`VERIFY` bandwidth) |
| Storage | none on module — microSD on dev kit |
| Power | 5 W (USB-C PD 5 V/3 A input on dev kit) |

## Interfaces / I/O

| Interface | Value |
|---|---|
| Camera | 1x MIPI CSI-2 (15-pin connector) |
| USB | 1x USB 3.0 + 2x USB 2.0 (dev kit) |
| Ethernet | GbE MAC |
| Display | HDMI `VERIFY` (2.0) — Nano 2GB dev kit |
| Low-speed | 40-pin header (UART, I2C, I2S, SPI, PWM, GPIO) |
| Form factor | 260-pin SODIMM, 69.6 × 45 mm |

## Internal hardware

On-module PMIC; boots from microSD; no WiFi/BT on module (dev kit has none fitted —
`VERIFY`); recovery via USB OTG / jumpers.

## How to load the OS

- **Stock JetPack:** write the Nano 2GB SD-card image (JetPack 4.6.x) to microSD.
- **Arches build:** `tx` Yocto branch image per branch README (legacy tegraflash path).

## How to log in

First boot runs the setup wizard (create user/password). Serial console 115200 8N1
via the dev-kit USB port (`VERIFY` connector); SSH over network once configured.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/`
