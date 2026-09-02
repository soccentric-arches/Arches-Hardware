# Orin Nano 4GB (module P3767-0004)

| Item | Value |
|---|---|
| Family / branch | `orin` · L4T R36.4.x · JetPack 6.2.x |
| Module P/N | P3767-0004 |
| Dev kit / carrier | P3768-0000 carrier |
| Flash config (L4T) | `jetson-orin-nano-devkit` / `-super` |
| Yocto MACHINE | `jetson-orin-nano-devkit[-super]` — `VERIFY` |

## Hardware specifications (DS-11105-001, verified)

| Spec | Value |
|---|---|
| CPU | 6x Arm Cortex-A78AE @ 1.5 GHz (1.7 GHz Super) |
| GPU | Ampere, 512 CUDA cores + 16 Tensor Cores @ 625 MHz (1020 MHz Super) |
| AI perf | 20 (sparse) / 10 (dense) INT8 TOPS; 34/17 TOPS (MAXN_SUPER) |
| Memory | 4 GB 64-bit LPDDR5 @ 2133 MHz (3199 Super), 34 GB/s (51 GB/s Super) |
| Storage | **no eMMC** — external NVMe/USB |
| Power modes | 7 W / 10 W / 25 W (MAXN_SUPER) |
| Interfaces | identical to Orin Nano 8GB (3x USB 3.2 Gen2, PCIe **Gen3** 1x4+3x1, GbE, 1x CAN, 3x UART, 2x SPI, 4x I2C, 2x I2S, 4x PWM, 15x GPIO, 8 CSI lanes) |
| Display | up to 4K30 (DP 1.2/HDMI 1.4/eDP 1.4) |

## Internal hardware

Same platform as Orin Nano 8GB with half the DRAM bus width and GPU cores; QSPI-NOR
boot, no eMMC. Recovery USB ID `0955:7623`.

## How to load the OS

Same as `../orin-nano-8gb/README.md` (`jetson-orin-nano-devkit` config covers 4GB;
rootfs NVMe/USB/SD). Arches `orin` branch image.

## How to log in

Same as Orin Nano 8GB — OEM setup wizard first boot, console 115200 8N1 (USB-C
device port / 40-pin UART), SSH at `192.168.55.1`.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/`
