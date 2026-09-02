# Jetson TX1 (module P2180)

| Item | Value |
|---|---|
| Family / branch | `tx` · L4T R32.7.x · JetPack 4.6.x |
| Module P/N | P2180 (FCC: VOB-P2180) |
| Dev kit / carrier | P2371-2180 dev kit (module + P2597-class carrier) |
| Flash config (L4T) | `jetson-tx1-devkit` |
| Yocto MACHINE (`meta-tegra`) | `jetson-tx1-devkit` — `VERIFY` against pinned branch |

## Hardware specifications (TX1 module product sheet, verified)

| Spec | Value |
|---|---|
| SoC | NVIDIA Tegra X1 (T210) |
| CPU | Quad-core 64-bit Arm Cortex-A57 |
| GPU | Maxwell, 256 CUDA cores, 1 TFLOP/s |
| Memory | 4 GB LPDDR4, 25.6 GB/s |
| Storage | 16 GB eMMC 5.1 |
| Camera | 12x MIPI CSI-2 D-PHY 1.1 lanes, dual ISP @ 1.5 Gb/s |
| Video | 4K 60 Hz decode / 4K 30 Hz encode |
| Display | Dual pipeline: HDMI / eDP / DSI |
| PCIe | Gen2, 1x1 + 1x4 (full x4 slot) |
| Networking | 10/100/1000BASE-T Ethernet |
| Connectivity | 802.11ac WLAN + Bluetooth (radio on module; dev-kit carrier exposes dual U.FL antenna connectors) |
| Power | VDD_IN 5.5–19.6 V DC; module 6.5–15 W |
| Form factor | 87 × 50 mm module, 88 g incl. thermal transfer plate (TTP) |

## Module I/O (product sheet)

USB 3.0 + USB 2.0 · HDMI/eDP/DSI · PCIe x4 · GbE · Full-size SD · **SATA data
and power** · GPIOs/I2C/I2S/SPI · TTL UART with flow control · display +
camera expansion headers (120-pin 2×60, 0.5 mm each — DSI 2×4 / eDP / CSI
6×2 or 3×4).

## Internal hardware

- On-module PMIC + power sequencer; carrier supplies VDD_IN (5.5–19.6 V).
- RTC with PMIC_BBAT backup input.
- WiFi/BT radio on module — antennas attach via dual U.FL connectors on the
  dev-kit wireless connector assembly.
- Boot: BCT/BootROM → CBoot from eMMC; recovery via USB OTG micro-AB.

## How to load the OS

1. **Arches build**: `tx` Yocto branch image; legacy tegraflash via the branch's
   documented `flash.sh` command.
2. **SDK path (stock JetPack 4.6.x)**: SDK Manager or L4T R32.7.x BSP. Force
   Recovery: power off → connect USB micro-B to the recovery port → power on →
   hold RECOVERY FORCE → press+release RESET → release after 2 s. Then:
   `sudo ./flash.sh jetson-tx1-devkit mmcblk0p1`

## How to log in

- **Stock dev-kit image:** default user `ubuntu`, password `ubuntu` (TX1 dev-kit
  user guide). Later JetPack 4.6.x images may run a setup wizard — change the
  default before network exposure.
- **Serial console:** carrier serial port header (1×6, J17: UART1 TX/RX/RTS/CTS
  at 3.3 V, needs TTL→RS232 or USB-serial) or the 2×30 debug connector (J10,
  UART0 @ 1.8 V) — 115200 8N1.
- **SSH over USB:** USB 2.0 Micro-AB port (device mode) → `192.168.55.1`.

## Module connector — 400-pin board-to-board

400-pin (8×50), 1.27 mm pitch B2B connector (carrier-side Samtec
REF-186137-01 mating); full pinout in the Jetson TX1 OEM Product Design Guide
(add to `datasheets/`). Interface groups on the connector:

- Camera: 12x MIPI CSI-2 D-PHY 1.1 lanes (up to 6x2 / 3x4 groupings)
- USB: 1x USB 3.0 + USB 2.0 (OTG on port 0)
- PCIe: Gen2 — 1x4 + 1x1 (full x4 slot on dev kit)
- Ethernet: GbE MDI (4 pairs) + link LEDs
- Display: HDMI/eDP/DP lanes + DSI (2x4) with backlight/touch control
- Storage: SDMMC (SDR104) + SATA data/power
- Low-speed: UART (flow-control), I2C (x2 general + CAM I2C), I2S (x3+),
  SPI, PWM, GPIO banks, DMIC
- Power/control: VDD_IN (5.5–19.6 V), POWER_EN/SYS_RESET/shutdown handshake,
  PMIC_BBAT, FORCE_RECOVERY, JTAG

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/` (P2180 module datasheet, TX1
OEM Product Design Guide, TX1/TX2 Developer Kit Carrier Board Specification)
