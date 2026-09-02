# Jetson TX2 (module P3310)

| Item | Value |
|---|---|
| Family / branch | `tx` · L4T R32.7.x · JetPack 4.6.x |
| Module P/N | **P3310** (confirmed — L4T adaptation guide: "The Jetson TX2 module consists of a P3310 SOM connected to a P2597 carrier board"; dev-kit P/N P2771; FCC: VOB-P3310) |
| Dev kit / carrier | P2771-0000 dev kit (carrier board **P2597**, shared with TX1) |
| Flash config (L4T) | `jetson-tx2-devkit` |
| Yocto MACHINE | `jetson-tx2-devkit` — `VERIFY` against pinned branch |

## Hardware specifications (TX2 dev-kit datasheet, verified)

| Spec | Value |
|---|---|
| SoC | NVIDIA Tegra X2 (T186, "Parker", Pascal generation) |
| CPU | Dual NVIDIA Denver 2 (2 MB L2) + Quad Arm Cortex-A57 (2 MB L2), HMP, 64-bit |
| GPU | Pascal, 256 CUDA cores |
| Memory | 8 GB 128-bit LPDDR4, 59.7 GB/s |
| Storage | 32 GB eMMC 5.1 |
| Camera | up to 6 cameras (2-lane), CSI-2 D-PHY 1.2 (2.5 Gbps/lane) — 12 lanes total (2×4 + 2×2 groupings) |
| Video | 4K60-class decode/encode (HEVC; H.264 encode up to 4K30 class — see datasheet) |
| PCIe | Gen2, 1x4 + 1x1 **or** 2x1 + 1x2 (UPHY-configurable) |
| USB | USB 3.0 + USB 2.0 |
| Networking | GbE; 802.11ac WLAN + Bluetooth on module |
| Power | VDD_IN 5.5–19.6 V (dev kit: 19 V adapter); module 7.5 W / 15 W modes |

## Module I/O

USB 3.0 + USB 2.0 · HDMI + DP · PCIe Gen2 · GbE · SATA (data + power;
`SATA_DEV_SLP` signal is TX2-only) · CSI (12 lanes) · GPIOs/I2C/I2S/SPI ·
**CAN (2x)** · TTL UART with flow control · digital mic (DMIC) + DSPK.

## Internal hardware

- On-module PMIC/sequencer; RTC backup input; 802.11ac + BT radio on module.
- Boot: BCT/BootROM → CBoot from eMMC; recovery via USB OTG micro-AB.
- Note: Jetson TX2 NX is **not** compatible with this carrier (L4T adaptation
  guide) — see `../jetson-tx2-nx`.

## How to load the OS

1. **Arches build**: `tx` Yocto branch image; legacy tegraflash.
2. **SDK path**: Force Recovery (hold RECOVERY FORCE → press+release RESET
   while powered on → release after 2 s), then:
   `sudo ./flash.sh jetson-tx2-devkit mmcblk0p1`
   (rootfs alternatives: `sda1` USB/SATA, `mmcblk1p1` SD card, or NFS `eth0`).
   UPHY lane map is set via `ODMDATA` in `p2771-0000.conf.common` (default
   config 2: 1x USB3.0 + 1x4 PCIe + SATA).

## How to log in

- **Stock dev-kit image:** default user `ubuntu`, password `ubuntu` (TX2 dev-kit
  user guide); JetPack 4.6.x images run an OEM setup wizard on first boot.
- **Serial console:** serial port header J17 (1×6, 3.3 V, UART1 with flow
  control) at 115200 8N1; debug connector J10 exposes UART0 @ 1.8 V.
- **SSH over USB:** USB 2.0 Micro-AB device mode → `192.168.55.1`.

## Module connector — 400-pin board-to-board

Same 400-pin (8×50), 1.27 mm B2B connector family as TX1 (P2597 carrier);
full pinout in the Jetson TX2 OEM Product Design Guide. UPHY lane map is
ODMDATA-configurable (6 lanes: PEX0/1/2/RFU, SATA, USB-SS) — verified
configurations in the L4T adaptation guide, e.g. default = 1x USB 3.0 +
1x PCIe x4 + SATA. Interface groups: 12x CSI-2 D-PHY 1.2 lanes, USB 3.1 +
USB 2.0, PCIe Gen2 (1x4+1x1 or 2x1+1x2), GbE MDI, HDMI 2.0 + DP 1.2 +
DSI, SATA, SDMMC, CAN (2x), DMIC/DSPK, UART/I2C/I2S/SPI/PWM/GPIO banks,
VDD_IN 5.5–19.6 V, PMIC_BBAT, FORCE_RECOVERY, JTAG.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/` (P3310 datasheet, TX2 OEM
Product Design Guide, P2597/P2771 carrier spec + design files)
