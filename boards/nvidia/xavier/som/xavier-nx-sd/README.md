# Xavier NX (SD variant, module P3668-0000)

| Item | Value |
|---|---|
| Family / branch | `xavier` · L4T R35.6.x · JetPack 5.1.x |
| Module P/N | P3668-0000 (boots microSD) |
| Dev kit / carrier | P3509 dev kit |
| Flash config (L4T) | `jetson-xavier-nx-devkit` |
| Yocto MACHINE | `jetson-xavier-nx-devkit` — `VERIFY` |

## Hardware specifications

| Spec | Value |
|---|---|
| SoC | NVIDIA Xavier (T194, low-power bin) |
| CPU | 6x NVIDIA Carmel @ 1.9 GHz |
| GPU | Volta, 384 CUDA cores + 48 Tensor Cores |
| DLA / PVA | 2x NVDLA v1 / 1x PVA v1 (`VERIFY` count for NX) |
| AI perf | up to 21 TOPS (INT8, sparse, 20 W mode) |
| Memory | 8 GB 128-bit LPDDR4x, 51.2 GB/s |
| | Storage | none on module — microSD (≥32 GB UHS-1 recommended) |
| Power modes | 10 W / 15 W / 20 W (MAXN `VERIFY`) |
| Form factor | 260-pin SODIMM, 69.6 × 45 mm (Orin NX/Nano footprint) |

## Interfaces / I/O (module)

| Interface | Value |
|---|---|
| Camera | up to 6x MIPI CSI-2 lanes (`VERIFY`) |
| | USB | 3x USB 3.1 Gen2 + 3x USB 2.0 (module; dev-kit carrier: 4x Type-A via Gen2 hub + Micro-B device-only) |
| | PCIe | C0 x4 Gen4, C1 x1, C3 x1, C5 dual-mode x8 (dev-kit default: C4 x1 Gen3 → M.2 Key E, C5 x4 Gen4 → M.2 Key M) |
| Networking | GbE MAC |
| | Display | stacked HDMI 2.0a/b + DP 1.4 on carrier |
| Low-speed | UART, I2C, I2S, SPI, PWM, GPIO (260-pin SODIMM — design guide in `datasheets/`) |

## Internal hardware

On-module PMIC/sequencer; microSD boot (SD SKU); RTC backup input; recovery via USB
OTG. No on-module WiFi/BT — use carrier M.2 Key E.

## How to load the OS

1. **Stock:** write the JetPack 5.1.x Xavier NX SD image to microSD, insert, power on.
2. **Host flash:** Force Recovery → `sudo ./flash.sh jetson-xavier-nx-devkit mmcblk0p1`
   (eMMC-rooted flows) — Arches `xavier` branch image per branch README.

## How to log in

- First boot: OEM setup wizard (stock image) or rootfs-defined user (Arches).
- Serial console: 115200 8N1 on carrier debug UART.
- SSH: `192.168.55.1` via USB device mode.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/` (P3668 datasheet, P3509 carrier)
