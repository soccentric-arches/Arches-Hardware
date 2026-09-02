# Orin Nano Developer Kit (P3768-0000 carrier)

| Item | Value |
|---|---|
| Carrier | P3768-0000 |
| Module | P3767-0003/-0005 (Orin Nano 8GB), P3767-0004 (4GB), **or P3767-0000/-0001 (Orin NX)** |
| Flash config | `jetson-orin-nano-devkit` / `jetson-orin-nano-devkit-super` (also flashes Orin NX on this carrier) |
| L4T / JetPack | R36.4.x / 6.2.x (`orin` branch) |

## Onboard hardware

| Block | Details |
|---|---|
| Display | HDMI + DP output (SoC shared HDMI/DP pins) `VERIFY` per user guide |
| USB | 4x USB Type-A 3.2 (Gen1/Gen2 split `VERIFY`) + 1x USB-C (device/flash + power option) |
| Ethernet | RJ45 GbE |
| Storage | microSD slot (usable with P3767-0005 dev module); M.2 Key M for NVMe |
| Expansion | 40-pin header (I2C/SPI/UART/I2S/PWM/GPIO, 3.3 V), CSI camera connector(s), 12-pin button header |
| Power | DC barrel jack (`VERIFY` 5.5/2.5 mm, 9-19 V class) or USB-C |
| Buttons | Power, Reset; **Force Recovery via REC-GND jumper on 12-pin button header** (no button) |
| Wireless | M.2 Key E slot for optional WiFi/BT module (none fitted by default — `VERIFY`) |

## 40-pin header

Functional layout matches the Jetson 40-pin standard used on AGX Orin (3.3 V/5 V
rails, GND, UART1 on 8/10, I2C on 3/5, SPI1 on 19/21/23/24/26, I2S, PWM/CAN/GPIO
per pinmux), 3.3 V logic. Resolve exact per-pin mapping from the P3768 pinmux
table in the carrier/user guide (`VERIFY` before wiring).

## How to load the OS

1. **Arches build:** `orin` Yocto branch → `l4t_initrd_flash.sh` path (NX/Nano do
   not use plain `flash.sh`).
2. **SDK path (JetPack 6.2.x):**
   - NVMe: `sudo ./l4t_initrd_flash.sh --erase-all jetson-orin-nano-devkit internal`
   - USB rootfs: add `--external-device sda1`
   - microSD (P3767-0005 only): add `--external-device mmcblk0p1`
   - Super: `jetson-orin-nano-devkit-super`
3. Force Recovery: power off → place jumper REC–GND on the 12-pin button header →
   power on. `lsusb` → `0955:7523` (Nano 8GB) / `7623` (4GB) / `7323`/`7423` (NX).
4. Select the flashed media in the UEFI boot menu.

## How to log in

- **First boot (stock image):** follow the on-display setup wizard.
- **Serial console:** 115200 8N1 via USB-C device port (ttyGS0) after flashing, or
  the 40-pin UART pins (`VERIFY`).
- **SSH:** USB device mode → `ssh <user>@192.168.55.1`; or Ethernet once configured.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/` (P3768 carrier + dev kit user guide)
