# Jetson TX1 (module P2180)

| Item | Value |
|---|---|
| Family / branch | `tx` · L4T R32.7.x · JetPack 4.6.x |
| Module P/N | P2180 |
| Dev kit / carrier | P2371-2180 dev kit |
| Flash config (L4T) | `jetson-tx1-devkit` |
| Yocto MACHINE (`meta-tegra`) | `jetson-tx1-devkit` — `VERIFY` against pinned branch |

## Hardware specifications

| Spec | Value |
|---|---|
| SoC | NVIDIA Tegra X1 (T210) |
| CPU | Quad-core Arm Cortex-A57 (max ~1.73 GHz — `VERIFY`) |
| GPU | Maxwell GM20B, 256 CUDA cores (~1 TFLOP FP16 / ~0.5 TFLOPS FP32) |
| Memory | 4 GB 128-bit LPDDR4, 25.6 GB/s |
| Storage | 16 GB eMMC 5.1 (module) |
| AI perf | ~472 GFLOPS (FP16) |
| Power modes | 10 W / 15 W |
| Operating temp | `VERIFY` (module Tj range, see datasheet) |

## Interfaces / I/O (module)

| Interface | Value |
|---|---|
| Camera | 6x MIPI CSI-2 lanes (`VERIFY` lane grouping) |
| USB | 1x USB 3.0 + 3x USB 2.0 (`VERIFY`) |
| Ethernet | 1x GbE MAC (RGMII) |
| Display | HDMI 2.0 + DP 1.2 |
| Storage | SDMMC (SD/eSD) |
| Low-speed | UART, I2C, I2S, SPI, PWM, GPIO (260-pin SODIMM module edge — pinout in Product Design Guide, see `datasheets/`) |
| Form factor | SODIMM module (69.6 × 45 mm class — `VERIFY`) |

## Internal hardware

- On-module PMIC + power sequencer; carrier supplies VDD_IN.
- RTC with optional PMIC_BBAT backup input.
- WiFi/BT: none on module — dev kit adds an M.2/wireless module.
- Boot: BCT/BootROM → CBoot from eMMC; recovery via USB OTG (Force Recovery strap).

## How to load the OS

1. **Arches build**: `tx` Yocto branch builds the image per the branch README; flash with
   `meta-tegra`'s tegraflash path.
2. **SDK path (bring-up / stock JetPack 4.6.x)**: install NVIDIA SDK Manager (or the
   L4T R32.7.x BSP tarball), put the board in Force Recovery (hold recovery strap /
   button while powering on), then:
   `sudo ./flash.sh jetson-tx1-devkit mmcblk0p1`
3. Rootfs target `mmcblk0p1` (eMMC); SD-card rootfs uses `--external-device` flows of
   that era — follow the `tx` branch flash docs, not the Orin ones.

## How to log in

- **First boot (stock JetPack dev-kit image):** default user `nvidia`, password
  `nvidia`, auto-login enabled. Change it before exposing the board to a network.
- **Serial console:** dev-kit USB OTG/micro-B port exposes the debug UART at
  115200 8N1 (`ttyTHS*`).
- **SSH:** connect the USB device-mode port; the board answers at `192.168.55.1`
  (`ssh nvidia@192.168.55.1`).
- **Arches images:** user creation follows the `tx` branch's rootfs config — see the
  branch README.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/` (drop the P2180 module datasheet +
TX1 Product Design Guide here)
