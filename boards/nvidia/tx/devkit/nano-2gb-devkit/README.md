# Jetson Nano 2GB Developer Kit (P3541)

| Item | Value |
|---|---|
| Carrier | P3541 |
| Module | P3448-0003 (see `../som/jetson-nano-2gb`) |
| Flash config | `jetson-nano-2gb-devkit` (SD image) |
| L4T / JetPack | R32.7.x / 4.6.x (`tx` branch) |

## Onboard hardware

| Block | Details |
|---|---|
| Display | HDMI `VERIFY` |
| USB | 1x USB 3.0 + 2x USB 2.0 Type-A |
| Ethernet | RJ45 GbE |
| Storage | microSD slot |
| Expansion | 40-pin header, 15-pin CSI camera connector |
| Power | USB-C (5 V / 3 A) |
| Buttons | Power, Recovery, Reset (`VERIFY` layout) |

## 40-pin header

Same functional layout as the Nano dev kit (3.3 V/5 V/GND, UART1 on 8/10, I2C 3/5,
SPI 19/21/23/24/26, I2S, PWM/GPIO); 3.3 V logic. Confirm per-pin mapping with the
P3541 pinmux table (`VERIFY`).

## How to load the OS

1. Write the JetPack 4.6.x Nano 2GB SD image to microSD, insert, power on.
2. Arches: `tx` Yocto branch image per branch README.

## How to log in

First boot setup wizard creates the user. Serial console 115200 8N1 (40-pin UART
pins 8/10, 3.3 V); SSH over Ethernet/USB device mode (`192.168.55.1` when in device
mode — `VERIFY` gadget support on this carrier).

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/`
