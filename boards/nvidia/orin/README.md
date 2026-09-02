# orin — Ampere Orin generation (primary Arches platform)

BSP line: **L4T R36.4.x / JetPack 6.2.x** · `meta-tegra` `scarthgap` · Yocto
`scarthgap` · Arches branch `orin`.
Flash path: `flash.sh` (AGX Orin eMMC) or `l4t_initrd_flash.sh` (Orin NX/Nano;
NVMe/USB/SD rootfs). The Arches carrier is an **AGX Orin + STM32** design — the
custom carrier wiring itself is owned by the hardware engineer; these folders
document the module/dev-kit interfaces that carrier builds on.

## SOM coverage

| SOM | Module P/N | Dev kit / carrier | Folder |
|---|---|---|---|
| AGX Orin 32GB | P3701-0004 | P3737 carrier / AGX Orin dev kit | `som/agx-orin-32gb` |
| AGX Orin 64GB | P3701-0005 | P3737 carrier | `som/agx-orin-64gb` |
| AGX Orin Industrial 64GB | P3701-0008 | P3737 carrier | `som/agx-orin-industrial` |
| Orin NX 16GB | P3767-0000 | P3768 Orin Nano carrier; P3509 Xavier NX carrier | `som/orin-nx-16gb` |
| Orin NX 8GB | P3767-0001 | P3768 / P3509 carrier | `som/orin-nx-8gb` |
| Orin Nano 8GB (incl. Super) | P3767-0003 / -0005 | P3768 dev kit carrier | `som/orin-nano-8gb` |
| Orin Nano 4GB | P3767-0004 | P3768 carrier | `som/orin-nano-4gb` |

Notes verified against NVIDIA module datasheets (DS-10712 / DS-11105):
- **Orin NX and Orin Nano modules have no eMMC** — rootfs is NVMe, USB, or
  (dev-kit module only) microSD; boot device is on-module QSPI-NOR.
- Orin Nano PCIe is Gen3-capable only (no Gen4 despite module PHY).
- "Super" = MAXN_SUPER mode config (`jetson-orin-nano-devkit-super`).

## Generation facts

- UEFI boot chain (R36); boot media selectable in UEFI menu.
- Dev-kit first boot (JetPack 6.x): OEM setup wizard on the display creates the user.
- Serial console: dev-kit debug UART (AGX Orin: USB micro-B J26) at 115200 8N1.
- SSH over USB device mode: board answers at `192.168.55.1`.
- Force Recovery confirmed via `lsusb` → `0955:` with ID `7023`/`7223` (AGX Orin),
  `7323`/`7423` (Orin NX), `7523`/`7623` (Orin Nano).

## Dev kits

| Dev kit | Carrier | Folder |
|---|---|---|
| AGX Orin Developer Kit | P3737-0000 | `devkit/agx-orin-devkit` |
| Orin Nano Developer Kit | P3768-0000 | `devkit/orin-nano-devkit` (also carries Orin NX) |
