# AGX Orin 64GB (module P3701-0005)

| Item | Value |
|---|---|
| Family / branch | `orin` · L4T R36.4.x · JetPack 6.2.x |
| Module P/N | P3701-0005 |
| Dev kit / carrier | P3737-0000 carrier |
| Flash config (L4T) | `jetson-agx-orin-devkit` |
| Yocto MACHINE | `jetson-agx-orin-devkit` — `VERIFY` |

## Hardware specifications

| Spec | Value |
|---|---|
| SoC | NVIDIA Orin (T234) |
| CPU | 12x Arm Cortex-A78AE v8.2 @ 2.2 GHz |
| GPU | Ampere, 2048 CUDA cores + 64 Tensor Cores |
| DLA / PVA | 2x NVDLA v2.0 / PVA v2.0 |
| AI perf | up to 275 (sparse) INT8 TOPS |
| Memory | 64 GB 256-bit LPDDR5, 204.8 GB/s |
| Storage | 64 GB eMMC 5.1 (module) |
| Power modes | 15 W / 30 W / 50 W / 60 W (MAXN) |
| Form factor | 699-pin B2B, 100 × 87 mm, integrated TTP |

## Interfaces / I/O

Identical interface set to the 32 GB module (16 CSI lanes, 3x USB 3.2 Gen2 + 3x
USB 2.0, PCIe Gen4, MGBE/GbE, 2x CAN, full low-speed set) — see
`../agx-orin-32gb/README.md` and the P3701 datasheet in `datasheets/`.

## Internal hardware

Same as 32 GB (QSPI-NOR boot + eMMC, secure boot, RTC backup). Higher DRAM enables
large-model inference; otherwise the platform is identical.

## How to load the OS / How to log in

Same as `../agx-orin-32gb/README.md` — `jetson-agx-orin-devkit` config, eMMC or
NVMe rootfs, UEFI boot selection, OEM setup wizard first boot, console 115200 8N1,
SSH at `192.168.55.1`.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/`
