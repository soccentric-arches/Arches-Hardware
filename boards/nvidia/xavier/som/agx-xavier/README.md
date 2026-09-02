# AGX Xavier (module P2888 — 8/16/32/64 GB variants + Industrial)

| Item | Value |
|---|---|
| Family / branch | `xavier` · L4T R35.6.x · JetPack 5.1.x |
| Module P/N | P2888 variants (`VERIFY` SKU suffixes); Industrial = P2888-0008 |
| Dev kit / carrier | P2972-0000 dev kit (carrier P2822) |
| Flash config (L4T) | `jetson-agx-xavier-devkit` |
| Yocto MACHINE | `jetson-agx-xavier-devkit` — `VERIFY` |

## Hardware specifications (per SKU)

| Spec | Value |
|---|---|
| SoC | NVIDIA Xavier (T194) |
| CPU | 8x NVIDIA Carmel ARMv8.2 64-bit, 8 MB L2 + 4 MB L3 (dev-kit datasheet) |
| GPU | Volta, 512 CUDA cores + 64 Tensor Cores |
| DLA | 2x NVDLA v1 |
| PVA | 1x PVA v1 |
| AI perf | up to 32 TOPS (INT8, sparse) |
| Memory | 8/16/32/64 GB 256-bit LPDDR4x, 137 GB/s (dev-kit SKU: 16 GB) |
| Storage | eMMC 5.1 up to 64 GB (`VERIFY` per SKU) |
| | Power modes | 10 W / 15 W / 30 W (MAXN) — verified |
| Industrial SKU | extended temp (-25 °C class) + industrial qualification (`VERIFY` range) |
| Form factor | 699-pin B2B connector, 100 × 87 mm class w/ thermal transfer plate |

## Interfaces / I/O (module)

| Interface | Value |
|---|---|
| Camera | 16x MIPI CSI-2 lanes (up to 6 direct cameras / 16 virtual channels); 8x SLVS-EC |
| USB | 3x USB 3.1 Gen2 + 4x USB 2.0 (design guide; USB-C ports on dev kit are USB 3.1 Gen2) |
| PCIe | up to Gen4, x1/x2/x4/x8 + x16 root/endpoint capable (`VERIFY` controller map) |
| Networking | 1x GbE MAC (RJ45 on dev kit) |
| Display | 1x shared HDMI 2.0 / DP 1.4 (+MST) + eDP |
| Low-speed | up to 9x UART, 9x I2C, 6x SPI, I2S/AHUB, CAN `VERIFY`, PWM, GPIOs — full map in the Xavier Product Design Guide (`datasheets/`) |

## Internal hardware

- On-module PMIC/power sequencer; RTC with PMIC_BBAT backup input; 64 MB QSPI-NOR
  boot device (`VERIFY`) alongside eMMC.
- Boot: BootROM → UEFI → CBoot/L4T; Force Recovery strap + USB device mode.
- Security: secure boot (PKC/fuses), SE crypto engine.
- Thermal: integrated thermal transfer plate (TTP); dev kit adds fan.

## How to load the OS

1. **Arches build:** `xavier` Yocto branch → flash per branch README (legacy
   tegraflash/initrd path for R35).
2. **SDK path:** SDK Manager or L4T R35.6.x BSP:
   - eMMC rootfs: `sudo ./flash.sh jetson-agx-xavier-devkit mmcblk0p1`
   - NVMe/USB rootfs: `l4t_initrd_flash.sh` with the Xavier config (`VERIFY` exact
     command in the branch flash docs).
3. Force Recovery: power off → hold recovery button → press+release power → release
   recovery. Confirm via `lsusb` (`0955:` NVIDIA).

## How to log in

- **First boot (stock dev-kit image):** follow the on-display OEM setup wizard to
  create the user; older images default `nvidia`/`nvidia` (change immediately).
- **Serial console:** dev-kit debug USB port, 115200 8N1.
- **SSH:** USB device mode → `ssh <user>@192.168.55.1`; or over Ethernet/WiFi.
- **Arches images:** user policy from the `xavier` branch rootfs config.

## Module connector — 699-pin board-to-board

699-pin high-density B2B connector; module 100 × 87 mm with integrated
thermal transfer plate. Full pinout: Jetson AGX Xavier Product Design Guide
(add to `datasheets/`). Verified interface groups: 16x MIPI CSI-2 lanes
(≤6 direct cameras / 16 VC) + 8x SLVS-EC, 5x PCIe Gen4 controllers
(1×8, 1×4, 1×2, 2×1; root + endpoint), 3x USB 3.1 Gen2 + 4x USB 2.0, GbE
MDI, HDMI 2.0/eDP/DP display lanes, eMMC + QSPI boot, UART/I2C/I2S/SPI/
CAN/PWM/DMIC/GPIO banks, VDD_IN, PMIC_BBAT, power-sequencing handshakes.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/` (P2888 datasheet, Xavier Product
Design Guide, P2972/P2822 carrier spec)
