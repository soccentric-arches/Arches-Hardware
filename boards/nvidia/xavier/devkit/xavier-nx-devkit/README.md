# Xavier NX Developer Kit (carrier P3509-0000)

| Item | Value |
|---|---|
| Carrier | P3509-0000 (SP-09765-001) |
| Module | P3668-0000 (SD) or P3668-0001 (eMMC) — see `../som/` |
| Flash config | `jetson-xavier-nx-devkit` / `jetson-xavier-nx-devkit-emmc` |
| L4T / JetPack | R35.6.x / 5.1.x (`xavier` branch) |
| Dev-kit operating temp | 0–35 °C |
| Mechanical | 103 × 90.5 × 31 mm |

## Onboard hardware (carrier spec SP-09765-001, verified)

| Block | Details |
|---|---|
| Module connector | 260-pin SO-DIMM (TE 2309413-1) |
| USB | USB 2.0 Micro-B (J5, **device only** incl. recovery) + **4x USB 3.1 Gen2 Type-A** (2x stacked dual connectors J6/J7, via hub; host only, shared 2 A VBUS) |
| Ethernet | RJ45 GbE (J15, with PoE VC pins broken out) |
| Display | Stacked **HDMI 2.0a/b + DisplayPort 1.4** connector (J8) |
| Camera | **2x 15-position 1.0 mm flex connectors** (J1 = CSI0, J9 = CSI2; 1x2-lane each @ 2.5 Gbps/pair, CAM I2C + MCLK + control; positions swapped vs Jetson Nano B01) |
| Storage | microSD (SD SKU, UHS-1); M.2 **Key M: PCIe Gen4 x4 NVMe** (J11, 2280 single-sided); M.2 **Key E: PCIe Gen3 x1 + USB2 + I2S + UART + optional I2C** (J10, 75-pin single-sided — WiFi/BT module preinstalled in kit with antenna) |
| 40-pin header | I2C ×2, SPI ×2, UART, I2S, audio clock, GPIOs, PWM (all 3.3 V) |
| Buttons | 12-pin button header (J14): power LED ±, **UART2 debug TX/RX (3.3 V)**, auto-power-on disable (pins 5/6), SYS_RESET (7/8), FORCE_RECOVERY (9/10), SLEEP/WAKE (11/12) |
| Optional | CAN bus header J17 (CAN_TX/RX, 3.3 V); RTC backup **CR1225 coin-cell holder J3** (PMIC_BBAT, pin 235); **PoE header J19 + PoE backpower header J18** (38–60 V PoE → 9–20 V converter required) |
| Power | DC jack **9–20 V** (5.5 mm OD / 2.5 mm pin, center +, 3.5 A max; 19 V supply in kit); rails: VDD_5V 8 A, VDD_3V3 6 A, VDD_1V8 300 mA, 3V3_AO 500 mA; budgets: 40-pin 0.5 A @5 V / 0.1 A @3.3 V, M.2 E/M 0.8 A each, camera 0.26 A each, fan 0.15 A |
| Fan | 4-pin header (J13): 5 V, **tach = GPIO08 (pin 208)**, **PWM = GPIO14 (pin 230)** |

## 40-pin expansion header (J12) — verified pinout, all 3.3 V

| Pin | Signal | Pin | Signal |
|---|---|---|---|
| 1 | +3.3 V | 2 | +5 V |
| 3 | I2C1_SDA (open-drain) | 4 | +5 V |
| 5 | I2C1_SCL | 6 | GND |
| 7 | GPIO09 / AUD_MCLK | 8 | UART1_TXD |
| 9 | GND | 10 | UART1_RXD |
| 11 | UART1_RTS* | 12 | I2S0_SCLK |
| 13 | SPI1_SCK | 14 | GND |
| 15 | GPIO12 (TOUCH_CLK) | 16 | SPI1_CS1* |
| 17 | +3.3 V | 18 | SPI1_CS0* |
| 19 | SPI0_MOSI | 20 | GND |
| 21 | SPI0_MISO | 22 | SPI1_MISO |
| 23 | SPI0_SCK | 24 | SPI0_CS0* |
| 25 | GND | 26 | SPI0_CS1* |
| 27 | I2C0_SDA (open-drain) | 28 | I2C0_SCL |
| 29 | GPIO01 (GP clock 0) | 30 | GND |
| 31 | GPIO11 (GP clock 1) | 32 | GPIO07 (PWM) |
| 33 | GPIO13 (PWM) | 34 | GND |
| 35 | I2S0_FS | 36 | UART1_CTS* |
| 37 | SPI1_MOSI | 38 | I2S0_DIN |
| 39 | GND | 40 | I2S0_DOUT |

Notes: I2C pins ±2 mA open-drain (2.2 kΩ PU on carrier); most other pins via
TI TXB0108 translators (weak drivers, overdriveable); pull-ups on non-I2C
signals must be weak (>50 kΩ).

## How to load the OS

1. **SD SKU (stock):** write the JetPack 5.1.x SD image to a ≥32 GB UHS-1
   microSD, insert under the module, power on — boots automatically.
2. **Host flash (eMMC SKU / production):** Force Recovery (jumper/button per
   user guide; the module ships in the kit with fansink attached), then
   `sudo ./flash.sh jetson-xavier-nx-devkit-emmc mmcblk0p1` (SD SKU:
   `jetson-xavier-nx-devkit`, board name `p3509-0000+p3668-0000`).
3. Arches: `xavier` Yocto branch image per branch README.

## How to log in

- **First boot (stock image):** OEM setup — EULA, language/keyboard/timezone,
  WiFi, **create username/password/computer name**. Green LED next to Micro-USB
  lights at power-on.
- **Serial console:** UART2 debug on the button header (J14 pins 3/4), 3.3 V,
  115200 8N1.
- **SSH:** via GbE once networked; USB device mode (Micro-B is device-only on
  this carrier) → `192.168.55.1`.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/` (SP-09765-001 carrier spec +
P3509 design files, dev-kit user guide)
