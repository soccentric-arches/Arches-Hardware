# AGX Thor T5000 (module P3834-0008)

| Item | Value |
|---|---|
| Family / branch | `thor` · L4T R38.2.x+ · JetPack 7.x |
| Module P/N | P3834-0008 (128 GB DRAM) |
| Dev kit / carrier | P4071-0000 carrier / AGX Thor dev kit |
| Flash config (L4T) | `jetson-agx-thor-devkit` |
| Yocto MACHINE | `jetson-agx-thor-devkit` — `VERIFY` against pinned `meta-tegra` |

## Hardware specifications (DS-11945-001, verified)

| Spec | Value |
|---|---|
| SoC | NVIDIA Thor (Blackwell GPU + Neoverse CPU) |
| CPU | 14x Arm Neoverse-V3AE @ 2.6 GHz (64 KB I$/64 KB D$ per core, 1 MB L2/core, 16 MB shared L3) |
| GPU | Blackwell, 2560 CUDA cores + 5th-gen Tensor Cores (96), MIG (10 TPCs), up to 1.57 GHz |
| AI perf | up to 2070 FP4 TFLOPS sparse (1035 FP8); 8.06 TFLOPS FP32 |
| Accelerators | 1x PVA v3 (165 FP32 GFLOPs / 320 FP16), OFA (optical flow / stereo), 2x NVJPEG |
| Memory | 128 GB 256-bit LPDDR5X @ 4266 MHz, 273 GB/s, Alt-link ECC |
| Storage | on-module 64 MB QSPI-NOR (boot); rootfs on NVMe (PCIe) or USB 3.2 SSD |
| Video | 2x NVDEC (H.265/AV1/VP9/H.264, up to 4x 8K30 HEVC); 2x NVENC (H.265/H.264) |
| Camera | 16 MIPI CSI-2 lanes (C-PHY 2.1 up to 164 Gbps / D-PHY 2.1 40 Gbps), up to 6 cameras (32 VC); up to 20 via Holoscan Sensor Bridge |
| Networking | 4x MGBE up to 25 GbE (XFI/USXGMII/25GAUI, TSN/AVB, MACsec) |
| Display | 4x shared HDMI 2.1 / DP 1.4a (up to 8K30) |
| USB | 3x USB 3.2 + 4x USB 2.0 (USB0 = RCM/device mode) |
| PCIe | Gen5, up to x8 (C1 x1 + C3 x2 root-only; C2 x1, C4 x8, C5 x4 root/endpoint) |
| Low-speed | 4x UART, 4x CAN (**T5000 only**), 3x SPI, 13x I2C, 5x I2S/2x AHUB, 1x DMIC, 6x PWM, JTAG (≤15 MHz) |
| Power | 70/90/120 W modes (default 120 W), MAXN to 130 W TMP; SYS_VIN_HV 7-20 V (+5 V MV, +3.3 V SV T5000-only) |
| Temp | Tj -25 to 115 °C, slowdown 109 °C; TTP surface ≤ 80 °C |
| Form factor | 699-pin B2B, 100 × 87 mm, integrated TTP with heatpipe, ~350 g |

## Internal hardware

- Dual QSPI controllers (boot + secure key storage).
- Power-sequencing handshakes: MODULE_POWER_ON / CARRIER_POWER_ON / SYS_RESET_N,
  VDDIN_PWR_BAD_N, THERMAL_ALERT_N, SYSTEM_OC_N, MODULE_SHDN_N.
- PRSNT0/1 presence + MID0/1 module-ID straps; PMIC_BBATT RTC backup input
  (non-rechargeable cell only).
- Debug: JTAG port (≤15 MHz) + debug UART.

## How to load the OS

1. **Arches build:** `thor` Yocto branch (R38.2+ toolchain container) per branch
   README; Orin machine configs must not leak into this branch.
2. **SDK path (L4T R38/R39):** Force Recovery via J81 (hold recovery → power on →
   release), confirm `lsusb` → `0955:7026`, then:
   `sudo ./l4t_initrd_flash.sh --erase-all jetson-agx-thor-devkit internal`
   (flashes QSPI-NOR + NVMe; NVMe must be > 234 GiB, else set
   `EXT_NUM_SECTORS=<bytes>/512`).
3. **Reboot the board manually** after installation completes.

## How to log in

- **First boot (stock image):** follow the on-display prompts to set up a user
  account; Arches images use the `thor` branch rootfs user policy.
- **Serial console:** 115200 8N1 (`VERIFY` exact debug connector on P4071 — see
  the AGX Thor dev kit user guide).
- **SSH:** over the 5 GbE RJ45 once networked; USB gadget address `VERIFY` on Thor.

## Module connector — 699-pin board-to-board

699-pin B2B connector; module 100 × 87 × 15.29 mm, integrated TTP with
heatpipe (~350 g). Full pinout: Jetson Thor Series Modules Design Guide
(DG-12084-001) pin-description spreadsheet (add to `datasheets/`). Verified
interface groups (DS-11945-001): 16x MIPI CSI-2 lanes (C-PHY 2.1 / D-PHY 2.1)
+ CoE via MGBE, 4x MGBE 25GbE, 3x USB 3.2 + 4x USB 2.0, PCIe Gen5 up to x8
(C1 x1, C3 x2 root-only; C2 x1, C4 x8, C5 x4 root/endpoint), 4x CAN
(T5000), 4x UART, 3x SPI, 13x I2C, 5x I2S/2x AHUB, 1x DMIC, 6x PWM, JTAG,
2x QSPI (boot + secure key), SYS_VIN_HV/MV/SV power inputs.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/` (DS-11945-001, P4071 carrier, dev kit
user guide)
