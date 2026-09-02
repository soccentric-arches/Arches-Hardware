# Jetson TX2 Developer Kit (P2771-0000, carrier P3310)

| Item | Value |
|---|---|
| Carrier | P3310 (inside P2771-0000 dev kit) |
| Module | P3489-0000 TX2 (also carries TX2i / TX2 4GB — see `../som/`) |
| Flash config | `jetson-tx2-devkit` / `jetson-tx2i` / `jetson-tx2-4gb` |
| L4T / JetPack | R32.7.x / 4.6.x (`tx` branch) |

## Onboard hardware

| Block | Details |
|---|---|
| Display | HDMI 2.0 + DP 1.2 output |
| USB | 4x USB 3.0 Type-A (`VERIFY` hub grouping) |
| Ethernet | RJ45 GbE |
| Storage | eMMC (module); M.2 Key M; M.2 Key E (WiFi/BT); SATA data+power (`VERIFY`); SD card slot (`VERIFY`) |
| Expansion | 40-pin header (GPIO/I2C/I2S/SPI/PWM), CSI camera connector, fan header |
| Debug | USB micro-B debug UART (115200 8N1) |
| Power | DC barrel jack (`VERIFY` ~19 V class), power/reset/recovery buttons |
| Wireless | 802.11ac + BT module via M.2 Key E |

Exact connector reference designators and pin tables: P2771/P3310 carrier schematic
and user guide — add to `datasheets/`.

## 40-pin header

Pi-compatible functional layout (3.3 V/5 V/GND/UART1/I2C/I2S/SPI/PWM/GPIO) shared
across TX-generation dev kits; per-pin SoC mapping via Jetson-IO / carrier pinmux
(`VERIFY` before wiring).

## How to load the OS

1. Force Recovery: hold recovery button while powering on.
2. `sudo ./flash.sh jetson-tx2-devkit mmcblk0p1`
3. Arches: `tx` Yocto branch image, legacy tegraflash per branch README.

## How to log in

- First boot: default `nvidia`/`nvidia` (or OEM wizard on 4.6.x dev-kit images).
- Serial console: USB micro-B debug port, 115200 8N1.
- SSH: USB device mode → `192.168.55.1`.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/`
