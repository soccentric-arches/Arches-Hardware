# Jetson TX2 4GB (module P3489-0888)

| Item | Value |
|---|---|
| Family / branch | `tx` · L4T R32.7.x · JetPack 4.6.x |
| Module P/N | P3489-0888 |
| Dev kit / carrier | P2771 carrier (P2597 carrier board; no dedicated dev kit) |
| Flash config (L4T) | `jetson-tx2-4gb` |
| Yocto MACHINE | `jetson-tx2-4gb` — `VERIFY` |

## Hardware specifications

| Spec | Value |
|---|---|
| SoC | NVIDIA Tegra X2 (T186) |
| CPU | Dual Denver 2 + Quad Cortex-A57 |
| GPU | Pascal GP10B, 256 CUDA cores |
| Memory | 4 GB 128-bit LPDDR4 (`VERIFY` exact bandwidth/bin) |
| Storage | 16 GB eMMC 5.1 |
| Power modes | 7.5 W / 15 W |

## Interfaces / I/O

Same module interface set as Jetson TX2 (12 CSI-2 lanes, USB 3.0 + USB 2.0, GbE,
HDMI 2.0 + DP 1.2, SATA, CAN, UART/I2C/I2S/SPI) with reduced memory/storage.
See `../jetson-tx2/README.md` and `datasheets/`.

## Internal hardware

Identical platform to TX2 with reduced DRAM/eMMC; no WiFi/BT module (`VERIFY`).
Boot from eMMC via BCT → CBoot.

## How to load the OS

- Force Recovery, then: `sudo ./flash.sh jetson-tx2-4gb mmcblk0p1`
- Arches `tx` branch image; legacy tegraflash path.

## How to log in

Same as TX2 — stock default `ubuntu`/`ubuntu` (change it), serial console 115200 8N1
on the carrier serial header (3.3 V), SSH at `192.168.55.1` via USB device mode.

## Module connector

Same 400-pin B2B + P2597 carrier interface set as TX2 — see
`../jetson-tx2/README.md` (module connector section).

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/`
