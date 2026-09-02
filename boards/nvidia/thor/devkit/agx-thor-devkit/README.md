# AGX Thor Developer Kit (P4071-0000 carrier)

| Item | Value |
|---|---|
| Carrier | P4071-0000 reference carrier |
| Module | P3834-0008 T5000 (128 GB) or P3834-0000 T4000 (64 GB) |
| Flash config | `jetson-agx-thor-devkit` / `jetson-agx-thor-t4000` |
| L4T / JetPack | R38.2.x+ / 7.x (`thor` branch) |
| Power | 40-130 W |

## Onboard hardware (NVIDIA Thor spec, verified)

| Block | Details |
|---|---|
| Display | 1x HDMI 2.0b + 1x DisplayPort 1.4a |
| USB | 2x USB-A (3.2 Gen2) + 2x USB-C (3.1) |
| Networking | 1x 5GbE RJ45 + 1x QSFP28 (4x 25GbE, Holoscan Sensor Bridge capable) |
| Storage | 1 TB NVMe on M.2 Key M (x4 PCIe Gen5) |
| Expansion | M.2 Key E (x1 PCIe Gen5, USB2, UART, I2C, I2S — WLAN/BT); PCIe x4/x2 lanes; 2x 13-pin CAN header; 2x 6-pin automation header; audio panel header (2x5) |
| Debug | JTAG connector (2x5 header); LED |
| Power | MicroFit power jack; RTC backup battery connector (2-pin); fan connector (12 V, PWM, tach) |
| Recovery | Force Recovery button + **J81 USB recovery port** |
| Mechanical | 243.19 × 112.40 × 56.88 mm (TTP + optional fan/heat sink) |

## Expansion headers (complete list) — **no 40-pin header on this dev kit**

The AGX Thor dev kit does **not** provide a Raspberry-Pi-style 40-pin header
(verified against the dev-kit I/O list). Low-speed expansion is via these
headers instead:

| Header / connector | Size | Signals |
|---|---|---|
| CAN headers (x2) | 13-pin | 4x CAN (T5000; **inert on T4000** — no CAN controllers) — `VERIFY` pinout in user guide |
| Automation headers (x2) | 6-pin | power / reset / force-recovery / auto-power-on control — `VERIFY` pinout |
| Audio panel header | 2x5 | HD-audio front-panel signals |
| JTAG connector | 2x5 | TCK/TMS/TDI/TDO/TRST (module JTAG, ≤15 MHz) |
| M.2 Key E | 75-pin | WLAN/BT: x1 PCIe **Gen5**, USB 2.0, UART, I2C, I2S |
| M.2 Key M | 75-pin | NVMe x4 PCIe **Gen5** (+ I2C, x2 PCIe lane) |
| QSFP28 | — | 4x 25GbE (Holoscan Sensor Bridge capable) |
| Fan connector | — | 12 V, PWM, tach |
| RTC backup battery | 2-pin | RTC backup |

`VERIFY` exact header pinouts against the Jetson AGX Thor Developer Kit User
Guide and carrier design files — add to `datasheets/`.

## Notes

- M.2 Key M: x4 PCIe **Gen5**; M.2 Key E: x1 PCIe Gen5.
- CAN headers are wired to the T5000's 4x CAN; the T4000 module has no CAN
  controllers, so the header is inert on T4000 (`VERIFY`).
- Dev kit is 0-35 °C-class non-production hardware.

## How to load the OS

1. **Arches build:** `thor` Yocto branch per branch README (unified initrd flow).
2. **SDK path (L4T R38/R39):** connect host USB to **J81**; power off → hold Force
   Recovery → press+release Power → release; `lsusb` → `0955:7026` (T5000) /
   `7226` (T4000); then:
   `sudo ./l4t_initrd_flash.sh --erase-all jetson-agx-thor-devkit internal`
   (T4000: `jetson-agx-thor-t4000`). NVMe must be > 234 GiB or set
   `EXT_NUM_SECTORS`.
3. **Reboot manually** after installation completes.

## How to log in

- **First boot:** on-display user setup (stock image).
- **Serial console:** 115200 8N1 (`VERIFY` exact connector in the AGX Thor dev kit
  user guide — add to `datasheets/`).
- **SSH:** over the 5 GbE RJ45 once networked; USB gadget address `VERIFY`.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/` (AGX Thor dev kit user guide + carrier
design files)
