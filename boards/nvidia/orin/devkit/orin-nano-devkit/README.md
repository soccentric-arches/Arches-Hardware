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

## 40-pin expansion header — full pin table

Functional layout identical to the standard NVIDIA Jetson 40-pin expansion
(verified positions for AGX Xavier/AGX Orin; Pi-compatible). All signals
3.3 V; default GPIO except I2C (3/5, 27/28) and UART (8/10).

| Pin | Signal | Pin | Signal |
|---|---|---|---|
| 1 | +3.3 V | 2 | +5.0 V |
| 3 | I2C_SDA (open-drain) | 4 | +5.0 V |
| 5 | I2C_SCL | 6 | GND |
| 7 | AUD_MCLK | 8 | UART1_TX |
| 9 | GND | 10 | UART1_RX |
| 11 | UART1_RTS | 12 | I2S0_SCLK |
| 13 | PWM | 14 | GND |
| 15 | GPIO / PWM | 16 | GPIO / DMIC data |
| 17 | +3.3 V | 18 | GPIO / PWM |
| 19 | SPI1_MOSI | 20 | GND |
| 21 | SPI1_MISO | 22 | GPIO |
| 23 | SPI1_SCLK | 24 | SPI1_CS0# |
| 25 | GND | 26 | SPI1_CS1# |
| 27 | I2C_SDA (open-drain) | 28 | I2C_SCL |
| 29 | GPIO (CAN-capable — `VERIFY`) | 30 | GND |
| 31 | GPIO (CAN-capable — `VERIFY`) | 32 | GPIO / DMIC clock |
| 33 | GPIO (CAN-capable — `VERIFY`) | 34 | GND |
| 35 | I2S0_FS | 36 | UART1_CTS |
| 37 | GPIO (CAN-capable — `VERIFY`) | 38 | I2S0_DIN |
| 39 | GND | 40 | I2S0_DOUT |

Notes:
- Configure SFIOs (i2s, spi, pwm, i2c) with Jetson-IO:
  `sudo /opt/nvidia/jetson-io/jetson-io.py` (Orin NX/Nano header + the
  **22-pin CSI connector** both configurable; overlay `compatible` strings:
  `nvidia,p3768-0000+p3767-000x`).
- Exact per-pin SoC GPIO numbers: P3768 carrier pinmux table (`VERIFY`).
- Orin NX/Nano modules expose **1x CAN** on the SODIMM (M_TTCAN 3.2); its
  routing to this header is pinmux-dependent (`VERIFY`).

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
