# AGX Xavier Developer Kit (P2972-0000, carrier P2822)

| Item | Value |
|---|---|
| Carrier | P2822 (inside P2972-0000 dev kit) |
| Module | P2888 (see `../som/agx-xavier`) |
| Flash config | `jetson-agx-xavier-devkit` |
| L4T / JetPack | R35.6.x / 5.1.x (`xavier` branch) |

## Onboard hardware

| Block | Details |
|---|---|
| Display | HDMI 2.0 + DP 1.2 output |
| USB | 4x USB 3.1 Type-A + 1x USB-C (`VERIFY` speed split via hub) |
| Ethernet | RJ45 (GbE/10GbE-class `VERIFY` PHY) |
| Storage | eMMC (module); M.2 Key M (PCIe SSD); SD card slot; SATA data+power (`VERIFY`) |
| Expansion | 40-pin header (GPIO/I2C/I2S/SPI/PWM/CAN `VERIFY`), CSI camera connector, M.2 Key E (WiFi/BT), PCIe x4/x16 slot (`VERIFY`) |
| Debug | USB micro-B debug UART (115200 8N1) |
| Power | DC barrel jack (~19 V class `VERIFY`) or USB-C PD; power/reset/recovery buttons; fan |
| Mechanical | Wedge dev-kit enclosure |

Exact reference designators/pin tables: P2822/P2972 carrier schematic + user guide —
add to `datasheets/`.

## 40-pin header

Functional layout shared with the Xavier generation: 3.3 V/5 V rails, GND, UART1
(8/10), I2C (3/5), SPI1 (19/21/23/24/26), I2S, PWM/GPIO — 3.3 V logic. Resolve exact
per-pin mapping via Jetson-IO and the carrier pinmux table (`VERIFY`).

## How to load the OS

1. Force Recovery: hold recovery → power on (release after power press).
2. `sudo ./flash.sh jetson-agx-xavier-devkit mmcblk0p1` (L4T R35.6.x).
3. Arches: `xavier` Yocto branch image; legacy flash path per branch README.

## How to log in

- First boot: OEM setup wizard creates the user (stock image).
- Serial console: USB debug port, 115200 8N1.
- SSH: USB device mode → `192.168.55.1`, or Ethernet once configured.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/`
