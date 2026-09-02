# Jetson TX2i (industrial, module P3489 — doc lists P3489-0000, `VERIFY` SKU suffix)

| Item | Value |
|---|---|
| Family / branch | `tx` · L4T R32.7.x · JetPack 4.6.x |
| Module P/N | P3489-0000 per branching doc §5.2 (`VERIFY` — NVIDIA marketing lists P3489-0008 for TX2i) |
| Dev kit / carrier | P2771 carrier (P2597 carrier board; no dedicated dev kit) |
| Flash config (L4T) | `jetson-tx2i` |
| Yocto MACHINE | `jetson-tx2i` — `VERIFY` |

## Hardware specifications

Same Tegra X2 platform as Jetson TX2 (dual Denver 2 + quad A57, 256-core Pascal
GPU, 8 GB 128-bit LPDDR4 @ 59.7 GB/s, 32 GB eMMC) with **industrial**
qualification: extended temperature range and industrial connector/consumer
grade — `VERIFY` exact range on the P3489-0008 datasheet. Power modes 7.5/15 W.
DRAM ECC is present **only** on TX2i within the TX2 series (L4T adaptation
guide; other TX2 variants reserve flash partitions for ECC that can be removed
from the flash layout).

## Interfaces / I/O

Same module interface set as TX2 (12 CSI-2 lanes, USB 3.0 + 2.0, PCIe Gen2
configurable, GbE, HDMI 2.0 + DP 1.2, SATA, CAN, UART/I2C/I2S/SPI). Industrial
SKU note: `VERIFY` presence of the on-module WiFi/BT (industrial SKUs commonly
ship without it; use carrier M.2 Key E if needed).

## Internal hardware

On-module PMIC + 32 GB eMMC; boot BCT → CBoot; recovery via USB OTG. Same
P2597-carrier electricals as TX2 (see `../jetson-tx2`).

## How to load the OS

- Force Recovery (same button sequence as TX2), then:
  `sudo ./flash.sh jetson-tx2i mmcblk0p1`
- Arches `tx` branch image; legacy tegraflash path.

## How to log in

Same as TX2 — stock default `ubuntu`/`ubuntu` (change immediately), serial
console 115200 8N1 on the carrier serial header (3.3 V) or debug connector
(1.8 V), SSH at `192.168.55.1` via USB device mode.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/` (P3489-0008 datasheet)
