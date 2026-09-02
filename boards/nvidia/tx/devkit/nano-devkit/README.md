# Jetson Nano Developer Kit (carrier P3449-0000)

| Item | Value |
|---|---|
| Carrier | P3449-0000 — rev **A02** (kit 945-13450-0000-000) or rev **B01** (kit 945-13450-0000-100; B01 is compatible with the production Nano module) |
| Module | P3448-0000 (see `../som/jetson-nano-sd`) |
| Flash config | `jetson-nano` (SD image) |
| L4T / JetPack | R32.7.x / 4.6.x (`tx` branch) |
| User guide | DA_09402-004 |

## Onboard hardware (user guide DA_09402-004, verified)

| Block | Details |
|---|---|
| Display | HDMI + DP stacked connector (J6) |
| USB | 2x dual-stacked USB 3.0 Type-A (J32/J33, all 4 via onboard hub, **1 A per stack**) + Micro-USB 2.0 (J28, power or device mode) |
| Ethernet | RJ45 GbE (J43) + **PoE header (J38, IEEE 802.3af)** |
| Storage | microSD slot **on the module** (J501) |
| Camera | 15-pin CSI camera connector (J13; **J49 second camera on B01**) — IMX219-class (RPi Cam V2 compatible) |
| Wireless | M.2 Key E (J18, **under the module**: PCIe x1 + USB2 + UART + I2S + I2C) |
| Expansion | **40-pin header (J41)** — see table below |
| Buttons | A02: 8-pin button header (J40 — power-on, reset, force recovery, auto-power-on disable) · B01: **12-pin button header (J50 — adds UART console + sleep LED)** |
| Serial | A02 only: 3.3 V serial port header (J44, UART console) |
| Fan | 4-pin fan header (J15: 5 V, PWM, tach) |
| Power | **Micro-USB 5 V/2 A (J28, default)** **or** DC jack 5 V/4 A (J25, 2.1×5.5×9.5 mm plug, max 4.4 A) — **J48 power-select jumper** chooses; 40-pin 5 V pins can also power the kit (2.5 A/pin); power LED DS3 |
| Power modes | Module 5 W / 10 W (GPU/CPU-capped budgets; CORE domain not capped) |

## 40-pin expansion header (J41) — verified pinout (user guide + Nano pinout table)

All signals **3.3 V logic**. Default config: every pin GPIO except pins 3/5 and
27/28 (I2C) and 8/10 (UART). The two 5 V pins can each source 2.5 A (can power
the kit); 3.3 V pins are fixed supply.

| Pin | Signal (sysfs) | Pin | Signal (sysfs) |
|---|---|---|---|
| 1 | +3.3 V | 2 | +5.0 V |
| 3 | I2C2_SDA — I2C bus 1 | 4 | +5.0 V |
| 5 | I2C2_SCL — bus 1 | 6 | GND |
| 7 | AUDIO_MCLK (gpio216) | 8 | UART2_TX (`/dev/ttyTHS1`) |
| 9 | GND | 10 | UART2_RX (`/dev/ttyTHS1`) |
| 11 | UART2_RTS (gpio50) | 12 | I2S4_SCLK (gpio79) |
| 13 | SPI2_SCK (gpio14) | 14 | GND |
| 15 | LCD_TE (gpio194) | 16 | SPI2_CS1 (gpio232) |
| 17 | +3.3 V | 18 | SPI2_CS0 (gpio15) |
| 19 | SPI1_MOSI (gpio16) | 20 | GND |
| 21 | SPI1_MISO (gpio17) | 22 | SPI2_MISO (gpio13) |
| 23 | SPI1_SCK (gpio18) | 24 | SPI1_CS0 (gpio19) |
| 25 | GND | 26 | SPI1_CS1 (gpio20) |
| 27 | I2C1_SDA — I2C bus 0 | 28 | I2C1_SCL — bus 0 |
| 29 | CAM_AF_EN (gpio149) | 30 | GND |
| 31 | GPIO_PZ0 (gpio200) | 32 | LCD_BL_PWM (gpio168) |
| 33 | GPIO_PE6 (gpio38) | 34 | GND |
| 35 | I2S4_LRCK (gpio76) | 36 | UART2_CTS (gpio51) |
| 37 | SPI2_MOSI (gpio12) | 38 | I2S4_SDIN (gpio77) |
| 39 | GND | 40 | I2S4_SDOUT (gpio78) |

Notes: PWM/PWM-capable pins via Jetson-IO; control GPIOs with `Jetson.GPIO`
(`/opt/nvidia/jetson-gpio/`) or configure SFIOs with
`sudo /opt/nvidia/jetson-io/jetson-io.py`.

## How to load the OS

1. **Stock:** write the JetPack 4.6.x Nano SD image to a ≥16 GB UHS-1 microSD,
   insert under the module, power on.
2. **Host flash (SDK Manager / production flows):** A02: jumper J40 pins 3-4
   (force recovery) + jumper J48, power from J25 → boots straight into Force
   Recovery. Then `sudo ./flash.sh jetson-nano mmcblk0p1`.
3. Arches: `tx` Yocto branch image (microSD or flash.sh) per branch README.

## How to log in

- **First boot (stock image):** setup wizard creates user/password. Headless
  first boot: complete setup via serial console on Micro-USB (**requires J48
  jumpered + DC-jack power** — the Micro-USB port is needed for the console).
- **Serial console:** B01: J50 button-header pins 3/4 (UART RX/TX, 3.3 V,
  115200 8N1); A02: J44 serial header.
- **SSH:** Micro-USB device mode → `192.168.55.1`, or Ethernet/PoE once
  networked.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/` (DA_09402-004, carrier spec,
P3448 datasheet)
