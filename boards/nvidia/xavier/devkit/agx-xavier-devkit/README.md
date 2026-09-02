# AGX Xavier Developer Kit (P2972-0000, carrier P2822)

| Item | Value |
|---|---|
| Carrier | P2822 (inside P2972-0000 dev kit; kit P/N 945-82972-0000-000) |
| Module | P2888 (see `../som/agx-xavier`) |
| Flash config | `jetson-agx-xavier-devkit` |
| L4T / JetPack | R35.6.x / 5.1.x (`xavier` branch) |

## Onboard hardware (dev-kit datasheet + user guide DA_09403-003, verified)

| Block | Details |
|---|---|
| PCIe | PCIe x16 connector (J6) → **x8 PCIe Gen4** controller; same lanes route **8x SLVS-EC** for cameras |
| Ethernet | RJ45 GbE |
| USB-C | **2x USB-C** (USB 3.1 Gen2 10 Gb/s; DP optional on both, PD optional) — **J512 is the flash port**; either port can power the kit from a listed USB-C PD supply |
| Hybrid port | 1x eSATA **or** USB 3.0 Type-A (J507; eSATA can supply 5 V — 2.5″ SATA drives) |
| Display | HDMI 2.0 (J504); HDMI + both USB-C DP → up to 3 displays |
| Camera | Camera connector (J509): **16x CSI-2 lanes**, up to 6 direct cameras / 16 via virtual channels |
| Storage | **microSD/UFS card slot (J4 — accepts SD or UFS card)**; M.2 Key M (J1) for NVMe (under module+thermal); M.2 Key E (J505: PCIe x1 + USB2 + UART + I2S + I2C for WiFi/LTE) |
| 40-pin header | UART + SPI + **CAN** + I2C + I2S + DMIC + GPIOs |
| Audio | HD Audio header |
| Debug | Micro-USB (J501) = **UART console** |
| Power | DC jack + 65 W AC adapter in kit; USB-C PD alternative; peripheral power budget ≈ 65 W − dev-kit draw (≤30 W default) |
| Buttons | Power On/Off, Force Recovery, Reset |
| Mechanical | 105 × 105 × 65 mm |

## Interface map (dev kit I/O → module)

| Dev-kit port | Module interface |
|---|---|
| PCIe x16 | x8 PCIe Gen4 / x8 SLVS-EC |
| RJ45 | GbE |
| 2x USB-C | 2x USB 3.1 (+DP/PD optional); flashing on 1 port |
| Camera connector | 16x CSI-2 lanes |
| M.2 Key M | NVMe x4 |
| M.2 Key E | PCIe x1 + USB2 + UART + I2S/PCM |
| 40-pin | UART, SPI, CAN, I2C, I2S, DMIC, GPIOs |
| eSATAp + USB 3.0 | SATA via PCIe x1 bridge + USB 3.0 |
| HDMI | HDMI 2.0 / eDP 1.2a / DP 1.4 |
| microSD/UFS | SD/UFS |

## 40-pin expansion header (J30) — verified pinout (carrier spec Table 18)

Levels 1.8/3.3 V selectable via **J514** (except UART pins and power = 3.3 V);
power pins 1 A max each. Sysfs GPIO numbers shown for GPIO-mode use.

| Pin | Signal (sysfs) | Pin | Signal (sysfs) |
|---|---|---|---|
| 1 | +3.3 V (1 A) | 2 | +5.0 V (1 A) |
| 3 | I2C_GP5_DAT — I2C bus 8 | 4 | +5.0 V (1 A) |
| 5 | I2C_GP5_CLK — bus 8 | 6 | GND |
| 7 | MCLK05 audio master clock (gpio422) | 8 | UART1_TX (3.3 V) |
| 9 | GND | 10 | UART1_RX (3.3 V) |
| 11 | UART1_RTS (gpio428) | 12 | I2S2_CLK (gpio351) |
| 13 | PWM01 (gpio424) | 14 | GND |
| 15 | GPIO27 / PWM2 (gpio393) | 16 | GPIO8 / DMIC data (gpio256, 3.3 V) |
| 17 | +3.3 V (1 A) | 18 | GPIO35 / PWM3 (gpio344) |
| 19 | SPI1_MOSI (gpio493) | 20 | GND |
| 21 | SPI1_MISO (gpio492) | 22 | GPIO17 (gpio417) |
| 23 | SPI1_SCLK (gpio491) | 24 | SPI1_CS0 (gpio494) |
| 25 | GND | 26 | SPI1_CS1 (gpio495) |
| 27 | I2C_GP2_DAT — I2C bus 1 | 28 | I2C_GP2_CLK — bus 1 |
| 29 | CAN0_DIN (gpio251, 3.3 V) | 30 | GND |
| 31 | CAN0_DOUT (gpio250, 3.3 V) | 32 | GPIO9 / DMIC clock (gpio257, 3.3 V) |
| 33 | CAN1_DOUT (gpio248, 3.3 V) | 34 | GND |
| 35 | I2S2_FS (gpio354) | 36 | UART1_CTS (gpio429) |
| 37 | CAN1_DIN (gpio249, 3.3 V) | 38 | I2S2_SDIN (gpio353) |
| 39 | GND | 40 | I2S2_SDOUT (gpio352) |

Notes:
- Default pinmux sets all non-power/UART/I2C pins to **GPIO**; enabling SFIOs
  (CAN, I2S, PWM, SPI) via Jetson-IO (`sudo /opt/nvidia/jetson-io/jetson-io.py`)
  or the alternate pinmux config (`tegra19x-mb1-pinmux-p2888-slvs-...-p2822-...`).
- **CAN caution:** CAN[1:0]_DIN/DOUT pins (29/31/33/37) carry internal 3.3 V
  pull-ups at power-on — connect only 3.3 V-tolerant devices.
- I2C bus check: `i2cdetect -y -r 8` (pins 3/5) and `-r 1` (pins 27/28).

## How to load the OS

1. **Arches build:** `xavier` Yocto branch; flash per branch README (legacy
   tegraflash / initrd path for R35).
2. **SDK path (JetPack 5.1.x):** connect host USB-C to **J512** (front port);
   Force Recovery: power off → press and hold Force Recovery → press and hold
   Power → release both. Then flash `jetson-agx-xavier-devkit` (eMMC rootfs via
   `flash.sh ... mmcblk0p1`, NVMe/USB via initrd flow per branch docs).
3. After flash the module reboots into first-boot configuration; with no display
   attached setup is **headless** — use the micro-USB serial console.

## How to log in

- **First boot (stock image):** on-display setup creates the user (language,
  keyboard, username/password); **headless setup**: connect a terminal emulator
  to the **micro-USB (J501) UART console** and complete setup there.
- **Serial console:** micro-USB J501, 115200 8N1.
- **SSH:** over GbE once networked, or via the USB device-mode port
  (`192.168.55.1`).

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/` (AGX Xavier dev-kit user guide
DA_09403-003, datasheet, P2822/P2972 carrier spec + design files)
