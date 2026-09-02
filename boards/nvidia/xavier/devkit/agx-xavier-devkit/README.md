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
