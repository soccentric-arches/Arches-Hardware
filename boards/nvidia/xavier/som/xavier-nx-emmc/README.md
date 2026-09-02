# Xavier NX (eMMC variant, module P3668-0001)

| Item | Value |
|---|---|
| Family / branch | `xavier` · L4T R35.6.x · JetPack 5.1.x |
| Module P/N | P3668-0001 (16 GB eMMC on module) |
| Dev kit / carrier | P3509 dev kit / P3449 carrier |
| Flash config (L4T) | `jetson-xavier-nx-devkit-emmc` |
| Yocto MACHINE | `jetson-xavier-nx-devkit-emmc` — `VERIFY` |

## Hardware specifications

Same compute as the SD variant (6x Carmel, 384-core Volta GPU, 8 GB LPDDR4x) with
**16 GB eMMC 5.1** on module instead of microSD-only. See
`../xavier-nx-sd/README.md` for the full spec and interface tables.

## Internal hardware

On-module PMIC + 16 GB eMMC; boot BCT → UEFI/CBoot from eMMC; recovery via USB OTG.

## How to load the OS

- Force Recovery → `sudo ./flash.sh jetson-xavier-nx-devkit-emmc mmcblk0p1`
- Arches `xavier` branch image; flash path per branch README.

## How to log in

Same as Xavier NX SD — first-boot wizard (stock) or Arches rootfs user; serial
console 115200 8N1; SSH at `192.168.55.1` in USB device mode.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/`
