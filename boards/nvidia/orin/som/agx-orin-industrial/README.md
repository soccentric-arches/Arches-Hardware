# AGX Orin Industrial 64GB (module P3701-0008)

| Item | Value |
|---|---|
| Family / branch | `orin` · L4T R36.4.x · JetPack 6.2.x |
| Module P/N | P3701-0008 |
| Dev kit / carrier | P3737-0000 carrier |
| Flash config (L4T) | `jetson-agx-orin-devkit-industrial` |
| Yocto MACHINE | `jetson-agx-orin-devkit-industrial` — `VERIFY` |

## Hardware specifications

| Spec | Value |
|---|---|
| SoC | NVIDIA Orin (T234) |
| CPU / GPU | 12x A78AE; 2048 CUDA cores + 64 Tensor Cores (per 64 GB class — `VERIFY` bin) |
| Memory | 64 GB 256-bit LPDDR5 |
| Storage | 64 GB eMMC 5.1 |
| Industrial | extended temperature / industrial qualification — `VERIFY` exact range vs commercial SKUs |
| Power modes | 15-60 W class (`VERIFY`) |

## Interfaces / I/O

Same as AGX Orin modules (see `../agx-orin-32gb/README.md`); confirm any
industrial-specific derating/qualification deltas in the P3701-0008 datasheet
(`VERIFY` — add to `datasheets/`).

## How to load the OS

- Force Recovery → `sudo ./flash.sh --erase-all jetson-agx-orin-devkit-industrial internal`
  (eMMC) or the initrd NVMe flow with the industrial config.
- Arches `orin` branch image per branch README.

## How to log in

Same as AGX Orin dev kit — OEM setup wizard first boot, serial console 115200 8N1,
SSH at `192.168.55.1`.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/`
