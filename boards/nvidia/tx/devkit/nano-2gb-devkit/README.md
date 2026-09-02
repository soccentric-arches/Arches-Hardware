# Jetson Nano 2GB Developer Kit (carrier P3542-0000)

| Item | Value |
|---|---|
| Carrier | P3542-0000 (compatible string `nvidia,p3542-0000+p3448-0003`) |
| Module | P3448-0003 (see `../som/jetson-nano-2gb`) |
| Flash config | `jetson-nano-2gb-devkit` (SD image) |
| L4T / JetPack | R32.7.x / 4.6.x (`tx` branch) |

## Onboard hardware

| Block | Details |
|---|---|
| Display | HDMI output |
| USB | 1x USB 3.0 + 2x USB 2.0 Type-A |
| Ethernet | RJ45 GbE |
| Storage | microSD slot |
| Camera | 15-pin CSI camera connector (30-pin "CSI Nano connector" class) |
| Expansion | **40-pin header** — see table below (L4T expansion-header matrix confirms: Nano 2GB = 40-pin + CSI, **no M.2 Key E**) |
| Power | USB-C 5 V / 3 A |
| Buttons | Power / Force Recovery / Reset |

## 40-pin expansion header — same functional pinout as the Nano J41 header

Same T210-family 40-pin layout as the Jetson Nano dev kit (Pi-compatible
positions); all signals 3.3 V, default GPIO except I2C (3/5, 27/28) and UART
(8/10):

| Pin | Signal | Pin | Signal |
|---|---|---|---|
| 1 | +3.3 V | 2 | +5.0 V |
| 3 | I2C2_SDA | 4 | +5.0 V |
| 5 | I2C2_SCL | 6 | GND |
| 7 | AUDIO_MCLK | 8 | UART2_TX (`/dev/ttyTHS1`) |
| 9 | GND | 10 | UART2_RX |
| 11 | UART2_RTS | 12 | I2S4_SCLK |
| 13 | SPI2_SCK | 14 | GND |
| 15 | LCD_TE | 16 | SPI2_CS1 |
| 17 | +3.3 V | 18 | SPI2_CS0 |
| 19 | SPI1_MOSI | 20 | GND |
| 21 | SPI1_MISO | 22 | SPI2_MISO |
| 23 | SPI1_SCK | 24 | SPI1_CS0 |
| 25 | GND | 26 | SPI1_CS1 |
| 27 | I2C1_SDA | 28 | I2C1_SCL |
| 29 | CAM_AF_EN | 30 | GND |
| 31 | GPIO_PZ0 | 32 | LCD_BL_PWM |
| 33 | GPIO_PE6 | 34 | GND |
| 35 | I2S4_LRCK | 36 | UART2_CTS |
| 37 | SPI2_MOSI | 38 | I2S4_SDIN |
| 39 | GND | 40 | I2S4_SDOUT |

(`VERIFY` sysfs GPIO numbers against the P3542 carrier pinmux — signal
positions per the standard Nano J41 map; configure SFIOs with Jetson-IO:
`sudo /opt/nvidia/jetson-io/jetson-io.py`.)

## How to load the OS

1. Write the JetPack 4.6.x Nano 2GB SD image to microSD, insert, power on
   (USB-C 5 V/3 A).
2. Arches: `tx` Yocto branch image per branch README.

## How to log in

First boot runs the setup wizard (create user/password). Serial console 115200
8N1 (40-pin UART pins 8/10, 3.3 V); SSH over Ethernet/USB device mode
(`192.168.55.1` when in device mode — `VERIFY` gadget support on this carrier).

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/`
