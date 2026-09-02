# Jetson Nano (eMMC variant, module P3448-0002)

| Item | Value |
|---|---|
| Family / branch | `tx` · L4T R32.7.x · JetPack 4.6.x |
| Module P/N | P3448-0002 (16 GB eMMC) |
| Dev kit / carrier | P3449 carrier (production carrier, no dev kit) |
| Flash config (L4T) | `jetson-nano-emmc` |
| Yocto MACHINE | `jetson-nano-emmc` — `VERIFY` |

## Hardware specifications

| Spec | Value |
|---|---|
| SoC | NVIDIA Tegra X1 (T210) |
| CPU | Quad-core Arm Cortex-A57 @ 1.43 GHz |
| GPU | Maxwell, 128 CUDA cores @ 921 MHz (472 GFLOPS FP16) |
| Memory | 4 GB 64-bit LPDDR4, 25.6 GB/s |
| Storage | 16 GB eMMC 5.1 (module) |
| Power modes | 5 W / 10 W |

## Interfaces / I/O

Same interface set as the Nano SD variant (1x 4-lane CSI-2, USB 3.x + USB 2.0, GbE
MAC, HDMI 2.0 + DP 1.2, 40-pin low-speed I/O). See `../jetson-nano-sd/README.md` and
the P3448 datasheet in `datasheets/`. The eMMC variant is intended for production
carriers (P3449) — SD boot is not the primary path.

## Internal hardware

On-module PMIC + 16 GB eMMC; boot BCT → CBoot from eMMC; recovery via USB OTG.

## How to load the OS

- Force Recovery on the carrier, then: `sudo ./flash.sh jetson-nano-emmc mmcblk0p1`
- Arches `tx` branch image; legacy tegraflash path.

## How to log in

Same as Nano SD — stock images default `nvidia`/`nvidia` (change immediately); serial
console 115200 8N1 on the carrier debug UART; SSH via `192.168.55.1` in USB device
mode.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/`
