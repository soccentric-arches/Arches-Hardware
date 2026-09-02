# AGX Thor T4000 (module P3834-0000)

| Item | Value |
|---|---|
| Family / branch | `thor` · L4T R38.2.x+ · JetPack 7.x |
| Module P/N | P3834-0000 (64 GB DRAM) |
| Dev kit / carrier | P4071-0000 carrier |
| Flash config (L4T) | `jetson-agx-thor-t4000` |
| Yocto MACHINE | `jetson-agx-thor-t4000` — `VERIFY` |

## Hardware specifications (DS-11945-001 v1.3+, verified)

| Spec | Value |
|---|---|
| CPU | 12x Arm Neoverse-V3AE @ 2.6 GHz (1 MB L2/core, 16 MB shared L3) |
| GPU | Blackwell, 1536 CUDA cores + 5th-gen Tensor Cores (64), MIG (6 TPCs), up to 1.53 GHz |
| AI perf | up to 1200 FP4 TFLOPS sparse (600 FP8); 4.7 TFLOPS FP32 |
| Memory | 64 GB 256-bit LPDDR5X @ 4266 MHz, 273 GB/s |
| Storage | 64 MB QSPI-NOR (boot); rootfs on NVMe / USB 3.2 SSD |
| Video | 1x NVDEC (H.265/AV1/VP9/H.264), 1x NVENC (H.265/H.264) |
| Camera | 16 CSI-2 lanes (C-PHY/D-PHY 2.1); HSB camera via QSFP |
| Networking | 3x MGBE up to 25 GbE |
| Display | 4x shared HDMI 2.1 / DP 1.4a |
| USB | 3x USB 3.2 + 4x USB 2.0 |
| PCIe | Gen5 up to x8 (same controller map as T5000) |
| CAN | **not available on T4000** (CAN is T5000-only per datasheet) |
| Low-speed | 4x UART, 3x SPI, 13x I2C, 5x I2S, 6x PWM (T4000 low-speed spec preliminary — `VERIFY`) |
| Power | 70 W (default) / MAXN ≤ 90 W TMP; SYS_VIN_HV 7-20 V |
| Form factor | 699-pin B2B, 100 × 87 mm, integrated TTP |

## Internal hardware

Same platform/sequencing as T5000 minus the second NVENC/NVDEC instance, fourth
MGBE, CAN controllers, and the SYS_VIN_SV rail. Recovery USB ID `0955:7226`.

## How to load the OS

- Force Recovery (J81 flow) → `lsusb` → `0955:7226` →
  `sudo ./l4t_initrd_flash.sh --erase-all jetson-agx-thor-t4000 internal`
- Reboot manually after install. Arches `thor` branch image per branch README.

## How to log in

Same as T5000 — first-boot user setup on display, serial console 115200 8N1
(`VERIFY` connector), SSH over Ethernet/USB.

## Module connector — 699-pin board-to-board

Identical 699-pin B2B connector/mechanical to T5000; differences: 3x MGBE,
**no CAN controllers**, no SYS_VIN_SV rail, single ISP/NVENC/NVDEC (see
DS-11945-001 and `../agx-thor-t5000/README.md`).

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/`
