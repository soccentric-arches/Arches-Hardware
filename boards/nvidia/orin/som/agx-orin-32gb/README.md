# AGX Orin 32GB (module P3701-0004)

| Item | Value |
|---|---|
| Family / branch | `orin` · L4T R36.4.x · JetPack 6.2.x |
| Module P/N | P3701-0004 |
| Dev kit / carrier | P3737-0000 carrier / AGX Orin dev kit |
| Flash config (L4T) | `jetson-agx-orin-devkit` |
| Yocto MACHINE | `jetson-agx-orin-devkit` — `VERIFY` against `meta-tegra@scarthgap` |

## Hardware specifications

| Spec | Value |
|---|---|
| SoC | NVIDIA Orin (T234) |
| CPU | 12x Arm Cortex-A78AE v8.2 @ 2.2 GHz |
| GPU | Ampere, 1792 CUDA cores + 56 Tensor Cores |
| DLA / PVA | 2x NVDLA v2.0 / PVA v2.0 |
| AI perf | up to 200 (sparse) INT8 TOPS |
| Memory | 32 GB 256-bit LPDDR5, 204.8 GB/s |
| Storage | 64 GB eMMC 5.1 (module) |
| Video | NVDEC 1x 8K30 / 3x 4K60 (H.265); NVENC 2x 4K60 (H.265) |
| Power modes | 15 W / 30 W / 50 W / 60 W (MAXN) |
| Form factor | 699-pin B2B connector, 100 × 87 mm, integrated thermal transfer plate |

## Interfaces / I/O (module)

| Interface | Value |
|---|---|
| Camera | up to 16 MIPI CSI-2 lanes (6x2 or 4x4, DPHY/CPHY) |
| USB | 3x USB 3.2 Gen2 + 3x USB 2.0 (USB0 = RCM/device capable) |
| PCIe | up to Gen4, multiple controllers (M.2 x4 Gen4 + PCIe x8 + M.2 Key E x1 on dev kit) |
| Networking | MGBE up to 10 GbE + GbE (RJ45 on dev kit, up to 10GBASE-T) |
| Display | 1x DP 1.4a (+MST) output on dev kit; HDMI/DP capable SoC |
| CAN | 2x CAN (CAN0/CAN1 exposed on 40-pin header) |
| Low-speed | multiple UART/I2C/SPI/I2S, PWM, GPIO — full map in Orin Product Design Guide (`datasheets/`) |

## Internal hardware

- On-module PMIC/power sequencer + RTC (PMIC_BBAT backup input).
- 64 MB QSPI-NOR boot device + 64 GB eMMC.
- Security: secure boot (PKC/fuses), Platform Security Controller, SE.
- Debug: JTAG header on dev kit + USB device-mode recovery.

## How to load the OS

1. **Arches build:** `orin` Yocto branch (L4T R36.4.x / `meta-tegra@scarthgap`);
   flash per branch README.
2. **SDK path (stock JetPack 6.2.x):**
   - eMMC rootfs (default dev kit): `sudo ./flash.sh --erase-all jetson-agx-orin-devkit internal`
   - NVMe rootfs: `sudo ./l4t_initrd_flash.sh --external-device nvme0n1p1 -c tools/kernel_flash/flash_l4t_t234_nvme.xml --erase-all jetson-agx-orin-devkit external`
   - USB/SD rootfs: same initrd flow with `--external-device sda1|mmcblk0p1`.
3. Force Recovery: power off → hold recovery button → press+release power → release.
   Confirm with `lsusb` (`0955:7023`/`7223`).
4. After flashing, select the flashed boot media in the UEFI boot menu.

## How to log in

- **First boot (stock image):** follow the on-display setup wizard to create the
  user account; log in on the DP display, serial console, or SSH.
- **Serial console:** USB micro-B debug port on the dev kit, 115200 8N1.
- **SSH over USB:** connect the device-mode USB-C port → `ssh <user>@192.168.55.1`;
  or over Ethernet once configured.
- **Arches images:** user policy comes from the `orin` branch rootfs config.

## Module connector — 699-pin board-to-board

699-pin (11×65) B2B connector; module 100 × 87 mm with integrated thermal
transfer plate. Full pinout: Jetson AGX Orin Product Design Guide (add to
`datasheets/`). Verified interface groups: 16x MIPI CSI-2 lanes (DPHY/CPHY,
6x2 or 4x4), USB 3.2 Gen2 + USB 2.0 ports (USB0 = RCM/device), multiple PCIe
Gen4 controllers (dev-kit map: M.2 Key M x4, PCIe x16-slot x8, M.2 Key E x1),
MGBE (up to 10 GbE) + GbE, 2x CAN, HDMI/DP display, eMMC 5.1 + QSPI-NOR,
UART/I2C/I2S/SPI/PWM/DMIC/GPIO banks, 15–60 W power envelope, PMIC_BBAT,
FORCE_RECOVERY, JTAG.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/` (P3701 module datasheet, Orin Product
Design Guide, P3737 carrier spec)
