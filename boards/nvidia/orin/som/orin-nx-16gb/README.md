# Orin NX 16GB (module P3767-0000)

| Item | Value |
|---|---|
| Family / branch | `orin` · L4T R36.4.x · JetPack 6.2.x |
| Module P/N | P3767-0000 |
| Dev kit / carrier | P3768 Orin Nano carrier; P3509 Xavier NX carrier |
| Flash config (L4T) | `jetson-orin-nano-devkit` (NX on P3768 — same config as Nano) |
| Yocto MACHINE | `jetson-orin-nano-devkit` (NX on P3768) / P3509 variant — `VERIFY` |

## Hardware specifications (DS-10712-001, verified)

| Spec | Value |
|---|---|
| SoC | NVIDIA Orin NX (low-power Orin) |
| CPU | 8x Arm Cortex-A78AE v8.2 @ 2 GHz |
| GPU | Ampere, 1024 CUDA cores + 32 Tensor Cores, up to 918 MHz (1173 MHz Super) |
| DLA / PVA | 2x NVDLA v2.0 (up to 40 TOPS sparse) / 1x PVA v2.0 |
| AI perf | 100 (sparse) / 50 (dense) INT8 TOPS; 157/78 TOPS (MAXN_SUPER) |
| Memory | 16 GB 128-bit LPDDR5, 102.4 GB/s (3200 MHz) |
| Storage | **no eMMC** — external NVMe (PCIe) or USB 3.2 SSD; boot from on-module QSPI-NOR |
| Camera | 8x MIPI CSI-2 lanes (2x4 or 4x2, D-PHY 2.1, 20 Gbps) |
| Video | decode 1x 8K30 / 2x 4K60 (H.265); encode 1x 4K60 (H.265/AV1) |
| Display | 1x shared HDMI 2.1 / DP 1.4a (up to 8K30) |
| Power modes | 10 W / 15 W / 25 W / 40 W (MAXN_SUPER; needs ≥8 V VDD_IN) |
| Form factor | 260-pin SODIMM, 69.6 × 45 mm |

## Interfaces / I/O (module, verified)

| Interface | Value |
|---|---|
| USB | 3x USB 3.2 Gen2 (10 Gbps) + 3x USB 2.0 (USB0 = RCM/device mode) |
| PCIe | 4 controllers: 1x4 + 3x1 (or 1x2+1x1 + 1x4) **Gen4** |
| Ethernet | 1x GbE MAC |
| CAN | 1x CAN (M_TTCAN 3.2, up to 8 Mbps) |
| Low-speed | 3x UART, 2x SPI, 4x I2C, 2x I2S, 4x PWM, 15x dedicated GPIO |
| GPIO voltages | most I/O 1.8 V CMOS; I2C0/1 3.3 V open-drain; CAN 3.3 V |
| Power input | VDD_IN 5-20 V (MODULE_ID strap; ≥8 V for MAXN_SUPER) |

## Internal hardware

- On-module PMIC/sequencer + RTC (PMIC_BBAT input, non-rechargeable cell only).
- 64 MB QSPI-NOR boot device (no eMMC on this module family).
- Force Recovery strap (pin 214); MODULE_ID strap (pin 217).
- 15 dedicated GPIOs (GPIO00-GPIO14); GPIO08 = fan tach capable; 4x PWM-capable pins.

## How to load the OS

1. **Arches build:** `orin` Yocto branch → initrd-flash path (NX/Nano use
   `l4t_initrd_flash.sh`, not plain `flash.sh`).
2. **SDK path (JetPack 6.2.x):** Force Recovery, then rootfs on NVMe/USB/SD:
   `sudo ./l4t_initrd_flash.sh --erase-all jetson-orin-nano-devkit internal` (NVMe)
   — same config carries Orin NX on the P3768 carrier; select the flashed media in
   the UEFI menu.
3. Rootfs storage must be ≥64 GB for SD/USB flows.
4. Confirm recovery mode via `lsusb` (`0955:7323`).

## How to log in

- First boot: on-display OEM setup wizard creates the user (stock image).
- Serial console: 115200 8N1 — via USB-C device port (ttyGS0) on the P3768 carrier
  or the 40-pin UART pins (`VERIFY` routing per carrier).
- SSH: USB device mode → `192.168.55.1`; or Ethernet once configured.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/` (DS-10712-001, NX Product Design
Guide, P3768 carrier)
