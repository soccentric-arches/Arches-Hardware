# Orin Nano 8GB (module P3767-0003 / -0005, incl. Super)

| Item | Value |
|---|---|
| Family / branch | `orin` · L4T R36.4.x · JetPack 6.2.x |
| Module P/N | P3767-0003 (production) / P3767-0005 (dev-kit module, microSD-capable) |
| Dev kit / carrier | P3768-0000 dev kit carrier |
| Flash config (L4T) | `jetson-orin-nano-devkit` / `jetson-orin-nano-devkit-super` (MAXN_SUPER) |
| Yocto MACHINE | `jetson-orin-nano-devkit[-super]` — `VERIFY` |

## Hardware specifications (DS-11105-001, verified)

| Spec | Value |
|---|---|
| CPU | 6x Arm Cortex-A78AE @ 1.5 GHz (1.7 GHz MAXN_SUPER) |
| GPU | Ampere, 1024 CUDA cores + 32 Tensor Cores @ 625 MHz (1020 MHz Super) |
| DLA / PVA | none (no DLA, no PVA on Nano) |
| AI perf | 40 (sparse) / 20 (dense) INT8 TOPS; 67/33 TOPS (MAXN_SUPER) |
| Memory | 8 GB 128-bit LPDDR5 @ 2133 MHz (3199 Super), 68 GB/s (102 GB/s Super) |
| Storage | **no eMMC** — external NVMe/USB; microSD on P3767-0005 dev-kit module |
| Display | 1x shared DP 1.2 (+MST) / HDMI 1.4 / eDP 1.4, up to 4K30 (388 MHz PCLK) |
| Video | decode 1x 4K60 (H.265); encode 1080p30 via CPU (software) |
| Power modes | 7 W / 15 W / 25 W (MAXN_SUPER) |
| Form factor | 260-pin SODIMM, 69.6 × 45 mm, 28 g |

## Interfaces / I/O (module, verified)

| Interface | Value |
|---|---|
| USB | 3x USB 3.2 Gen2 + 3x USB 2.0 (internal hub shares 10 Gbps on ports 0/1) |
| PCIe | **Gen3 only**: 1x4 + 3x1 (or 1x2+1x1 + 1x4), 7 lanes |
| Ethernet | 1x GbE MAC (MDI) |
| CAN | 1x CAN (M_TTCAN 3.2, up to 15 Mbps controller rate) |
| Low-speed | 3x UART, 2x SPI, 4x I2C, 2x I2S, 4x PWM (GPIO07/12/13/14), 15x GPIO |
| Camera ctrl | 2x CAM MCLK, 2x CAM PWDN, CAM_I2C |
| Power input | VDD_IN 5 V (Nano strap) / 5-20 V (NX strap) — see MODULE_ID pin 217 |
| Temp | Tj -25 °C to 105 °C (v1.7 datasheet) |

## Internal hardware

- 64 MB-class QSPI-NOR boot device (BootROM → BCT/loader); **no eMMC**.
- RTC backup via PMIC_BBAT (pin 235, non-rechargeable lithium cell only).
- 15 dedicated GPIOs (GPIO00-GPIO14, 1.8 V); Force Recovery strap pin 214.
- 260-pin SODIMM edge — full pin list in the datasheet (`datasheets/`).

## How to load the OS

1. **Arches build:** `orin` Yocto branch → `l4t_initrd_flash.sh` path.
2. **SDK path (JetPack 6.2.x):**
   - NVMe: `sudo ./l4t_initrd_flash.sh --erase-all jetson-orin-nano-devkit internal`
   - USB: add `--external-device sda1`
   - microSD (P3767-0005): add `--external-device mmcblk0p1`
   - Super mode: use `jetson-orin-nano-devkit-super`
3. Force Recovery on the dev kit: power off → jumper REC–GND on the 12-pin button
   header → power on. Confirm `lsusb` → `0955:7523` (8GB) / `7623` (4GB).
4. Select the flashed media in the UEFI boot menu.

## How to log in

- First boot: on-display OEM setup wizard (stock image) creates the user.
- Serial console: 115200 8N1 via USB-C device port (ttyGS0) after boot, or the
  40-pin UART pins (`VERIFY` routing on P3768).
- SSH: USB device mode → `192.168.55.1`, or Ethernet once configured.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/` (DS-11105-001, P3768 carrier spec)
