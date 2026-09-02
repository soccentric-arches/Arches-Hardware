# Jetson Nano Developer Kit (P3450)

| Item | Value |
|---|---|
| Carrier | P3450 |
| Module | P3448-0000 (Nano SD; P3448-0002 eMMC variant on P3449 carrier — see `../som/`) |
| Flash config | `jetson-nano` (SD image) |
| L4T / JetPack | R32.7.x / 4.6.x (`tx` branch) |

## Onboard hardware

| Block | Details |
|---|---|
| Display | HDMI 2.0 + DP 1.2 |
| USB | 4x USB Type-A: 1x USB 3.0 + 3x USB 2.0; micro-USB (device/flash) |
| Ethernet | RJ45 GbE |
| Storage | microSD slot (UHS-1) |
| Expansion | 40-pin header, 15-pin CSI camera connector, M.2 Key E slot |
| Debug | serial console via 40-pin UART pins (no dedicated USB-serial chip — `VERIFY`) |
| Power | DC barrel jack 5 V/4 A (5.5 × 2.1 mm) or micro-USB 5 V/2 A with J48 jumper disabled |
| Buttons | Power, Recovery, Reset buttons; jumper header (J48 etc.) |

## 40-pin header (functional layout)

| Pins | Function |
|---|---|
| 1, 17 | +3.3 V (max ~1 A combined) |
| 2, 4 | +5 V (input rail) |
| 3, 5 | I2C (SDA/SCL, 3.3 V) |
| 8, 10 | UART1 TX/RX (3.3 V, 115200 console-capable) |
| 19, 21, 23, 24, 26 | SPI1 MOSI/MISO/SCLK/CS0/CS1 |
| 12, 35, 38 | I2S (SCLK/FS/DIN-DOUT) |
| 7, 11, 13, 15, 16, 18, 22, 29, 31, 32, 33, 36, 37, 40 | GPIO / PWM / DMIC per pinmux |
| 6, 9, 14, 20, 25, 30, 34, 39 | GND |

All header I/O is 3.3 V logic. Exact SoC-GPIO numbers via Jetson-IO; verify against
the P3450 pinmux table in `datasheets/` before wiring.

## How to load the OS

1. **No host needed (stock):** write the JetPack 4.6.x Nano SD image to a ≥16 GB
   microSD, insert, power on.
2. **Host flash (eMMC/production flows):** Force Recovery, then
   `sudo ./flash.sh jetson-nano mmcblk0p1`.
3. Arches: `tx` Yocto branch image (microSD or flash.sh) per branch README.

## How to log in

- First boot (stock image): setup wizard creates the user; headless images default
  `nvidia`/`nvidia` — change immediately.
- Serial console: 40-pin UART pins 8/10 at 115200 8N1 (3.3 V).
- SSH: USB device mode via micro-USB → `192.168.55.1`, or Ethernet once networked.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/` (P3450 user guide + carrier schematic)
