# Orin NX 8GB (module P3767-0001)

| Item | Value |
|---|---|
| Family / branch | `orin` · L4T R36.4.x · JetPack 6.2.x |
| Module P/N | P3767-0001 |
| Dev kit / carrier | P3768 / P3509 carrier |
| Flash config (L4T) | `jetson-orin-nano-devkit` |
| Yocto MACHINE | `jetson-orin-nano-devkit` — `VERIFY` |

## Hardware specifications (DS-10712-001, verified)

| Spec | Value |
|---|---|
| CPU | 6x Arm Cortex-A78AE @ 2 GHz |
| GPU | Ampere, 1024 CUDA cores + 32 Tensor Cores, up to 765 MHz (1173 MHz Super) |
| DLA / PVA | 1x NVDLA v2.0 (up to 20 TOPS) / 1x PVA v2.0 |
| AI perf | 70 (sparse) / 35 (dense) INT8 TOPS; 117/58 TOPS (MAXN_SUPER) |
| Memory | 8 GB 128-bit LPDDR5, 102.4 GB/s |
| Storage | **no eMMC** — external NVMe/USB; QSPI-NOR boot |
| Power modes | 10 W / 15 W / 20 W / 40 W (MAXN_SUPER, ≥8 V VDD_IN) |
| Form factor | 260-pin SODIMM, 69.6 × 45 mm |

## Interfaces / I/O

Identical to Orin NX 16GB (3x USB 3.2 Gen2 + 3x USB 2.0, PCIe Gen4 1x4+3x1, GbE,
1x CAN, 3x UART, 2x SPI, 4x I2C, 2x I2S, 4x PWM, 15x GPIO, 8 CSI lanes) — see
`../orin-nx-16gb/README.md` and `datasheets/`.

## Internal hardware

Same as Orin NX 16GB (QSPI-NOR boot, no eMMC, RTC backup input, Force Recovery
strap). Recovery USB ID `0955:7423`.

## How to load the OS

Same flow as Orin NX 16GB — `l4t_initrd_flash.sh` with `jetson-orin-nano-devkit`;
Arches `orin` branch image. Rootfs on NVMe/USB/SD.

## How to log in

Same as Orin NX 16GB — OEM setup wizard first boot, console 115200 8N1, SSH at
`192.168.55.1`.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/`
