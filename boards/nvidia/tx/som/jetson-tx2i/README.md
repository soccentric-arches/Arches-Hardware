# Jetson TX2i (module P3489-0008 — doc lists P3489-0000, `VERIFY`)

| Item | Value |
|---|---|
| Family / branch | `tx` · L4T R32.7.x · JetPack 4.6.x |
| Module P/N | P3489-0008 (industrial variant) — `VERIFY` |
| Dev kit / carrier | P2771 carrier (no dedicated dev kit) |
| Flash config (L4T) | `jetson-tx2i` |
| Yocto MACHINE | `jetson-tx2i` — `VERIFY` |

## Hardware specifications

| Spec | Value |
|---|---|
| SoC | NVIDIA Tegra X2 (T186) |
| CPU | Dual Denver 2 + Quad Cortex-A57, up to 2.0 GHz |
| GPU | Pascal GP10B, 256 CUDA cores |
| Memory | 8 GB 128-bit LPDDR4, 59.7 GB/s |
| Storage | 32 GB eMMC 5.1 (`VERIFY` SKU storage) |
| Industrial | Extended temperature / industrial qualification — `VERIFY` exact range |
| Power modes | 7.5 W / 15 W |

## Interfaces / I/O

Same module interface set as Jetson TX2 (12x CSI-2 lanes, USB 3.1 + USB 2.0, GbE MAC,
HDMI 2.0 + DP 1.2, SDMMC, UART/I2C/I2S/SPI). See `../jetson-tx2/README.md` and the
module datasheet in `datasheets/`.

## Internal hardware

- TX2i variant notes: industrial connector/consumer spec, `VERIFY` presence of the
  on-module WiFi/BT solution (industrial SKUs commonly ship without it).
- Boot identical to TX2 (BCT → CBoot, eMMC).

## How to load the OS

- Force Recovery, then: `sudo ./flash.sh jetson-tx2i mmcblk0p1`
- Arches `tx` branch image; legacy tegraflash path.

## How to log in

Same as TX2 — default `nvidia`/`nvidia` on stock images (change immediately),
serial console on carrier debug UART (115200 8N1), SSH via `192.168.55.1` in USB
device mode. Arches images set the user per the `tx` branch config.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/` (P3489-0008 datasheet)
