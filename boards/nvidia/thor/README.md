# thor — Blackwell Thor generation

BSP line: **L4T R38.2.x or later / JetPack 7.x** · `meta-tegra` `master`-line Thor
branch (`VERIFY` — do not use Orin machines present in R39 trees) · Yocto: current
OE-Core release matching upstream `LAYERSERIES_COMPAT` · Arches branch `thor`.
Flash path: **unified `l4t_initrd_flash.sh` flow** (QSPI-NOR + NVMe).

## SOM coverage

| SOM | Module P/N | Dev kit / carrier | Folder |
|---|---|---|---|
| AGX Thor T5000 | P3834-0008 (128 GB DRAM) — verified against L4T R39 config table | P4071-0000 carrier / AGX Thor dev kit | `som/agx-thor-t5000` |
| AGX Thor T4000 | P3834-0000 (64 GB DRAM) — verified | P4071-0000 carrier | `som/agx-thor-t4000` |

`VERIFY`: confirm the exact `meta-tegra` branch/revision pinned for `thor` exposes
`jetson-agx-thor-devkit` (T5000) and `jetson-agx-thor-t4000` machines.

## Generation facts

- Boot chain: UEFI; storage = on-module 64 MB QSPI-NOR (bootloader) + NVMe rootfs
  (BSP assumes NVMe > 234 GiB, or pass `EXT_NUM_SECTORS`).
- Force Recovery on dev kit: **J81** USB port; hold Force Recovery → press+release
  Power → release.
- USB IDs in recovery: `0955:7026` (T5000, 128 GB) / `0955:7226` (T4000, 64 GB).
- After install completes, **reboot the board** (Thor does not auto-reboot).

## Dev kits

| Dev kit | Carrier | Folder |
|---|---|---|
| AGX Thor Developer Kit (T5000, 128 GB) | P4071-0000 | `devkit/agx-thor-devkit` |
| T4000 (64 GB) | P4071-0000 | `devkit/agx-thor-devkit` (T4000 config) |
