# Xavier NX Developer Kit (P3509)

| Item | Value |
|---|---|
| Carrier | P3509 |
| Module | P3668-0000 (SD) or P3668-0001 (eMMC) — see `../som/` |
| Flash config | `jetson-xavier-nx-devkit` / `jetson-xavier-nx-devkit-emmc` |
| L4T / JetPack | R35.6.x / 5.1.x (`xavier` branch) |

## Onboard hardware

| Block | Details |
|---|---|
| Display | HDMI 2.0 + DP 1.2 |
| USB | 4x USB Type-A (USB 3.1 class `VERIFY`) + micro-USB (device/flash) |
| Ethernet | RJ45 GbE |
| Storage | microSD slot (SD SKU); eMMC on module (eMMC SKU); M.2 Key M for NVMe |
| Expansion | 40-pin header, CSI camera connector(s), M.2 Key E |
| Power | DC barrel jack (`VERIFY` 9-19 V class) |
| Buttons | Power, Force Recovery, Reset |

## 40-pin header

Same functional layout as the Nano/Xavier NX family (3.3 V/5 V/GND, UART1 8/10,
I2C 3/5, SPI 19/21/23/24/26, I2S, PWM/GPIO), 3.3 V logic — verify per-pin mapping
against the P3509 pinmux table (`VERIFY`).

## How to load the OS

1. **SD SKU:** write the JetPack 5.1.x SD image to microSD and boot.
2. **Host flash (eMMC SKU / production):** Force Recovery →
   `sudo ./flash.sh jetson-xavier-nx-devkit-emmc mmcblk0p1`.
3. Arches: `xavier` Yocto branch image per branch README.

## How to log in

First-boot OEM wizard (stock) or rootfs user (Arches); serial console 115200 8N1;
SSH via `192.168.55.1` (USB device mode) or Ethernet.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/`
