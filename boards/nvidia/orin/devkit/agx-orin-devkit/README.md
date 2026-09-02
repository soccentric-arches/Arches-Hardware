# AGX Orin Developer Kit (P3737-0000 carrier)

| Item | Value |
|---|---|
| Carrier | P3737-0000 (699-pin B2B module connector J3) |
| Module | P3701-0000 dev-kit module, P3701-0004 32GB, P3701-0005 64GB, P3701-0008 Industrial |
| Flash config | `jetson-agx-orin-devkit` / `jetson-agx-orin-devkit-industrial` |
| L4T / JetPack | R36.4.x / 6.2.x (`orin` branch) |
| Operating temp | 0-35 °C (dev kit, non-production) |

## Onboard hardware (SP-10900-001, verified)

| Block | Details |
|---|---|
| Display | DisplayPort 1.4a output (J18) — **only display out**; supports SST/MST/DSC, up to 8K30 / 4K120; DP→HDMI adapter for HDMI monitors |
| USB | 2x USB-C (one UFP+DFP incl. flashing, one DFP-only; both USB 3.2 Gen2) + 4x USB-A (2x Gen2, 2x Gen1, via hub; 2 A/stack VBUS) + USB micro-B debug (J26) |
| Ethernet | RJ45 MGBE — 1/2.5/5/10 GbE (AQR113C-class PHY) |
| Storage | microSD (UHS-1, J10); M.2 Key M x4 PCIe Gen4 2280 (J1, NVMe); M.2 Key E x1 PCIe + USB2/UART/I2S (J505, WiFi/BT) |
| PCIe | x16 slot (lower x8 = PCIe Gen4 C5, J6); 12 V rail (NCP81599) |
| Camera | 120-pin (2x60, 0.5 mm) expansion (J509): 16 CSI-2 lanes (6x2/4x4, DPHY/CPHY), 2.8 V/1.8 V camera rails |
| Expansion | 40-pin header (J30, 2x20, 2.54 mm); 12-pin automation header (J42); audio panel header (J511); JTAG 2x5 header (J502) |
| Power | DC jack 5.5 mm OD / 2.5 mm ID center-positive, 7-20 V (J41) or USB-C PD (19 V adapter included); power/reset/force-recovery buttons; white LED |
| Misc | 4-pin fan connector (5 V, PWM, tach — J9); RTC backup battery connector (J13) |
| Rails | VDD_5V (11 A), VDD_3V3 (10 A), VDD_1V8 (3.5 A), VDD_12V (5.5 A), AVDD_CAM_2V8 |
| Mechanical | 110 × 110 × 71.65 mm (with feet/thermal), ~872 g |

## 40-pin expansion header (J30) — verified pinout, 3.3 V logic

| Pin | Signal | Pin | Signal |
|---|---|---|---|
| 1 | +3.3 V (1 A) | 2 | +5 V (1 A) |
| 3 | I2C5_SDA | 4 | +5 V |
| 5 | I2C5_SCL | 6 | GND |
| 7 | AUD_MCLK (MCLK05) / GPIO | 8 | UART1_TX |
| 9 | GND | 10 | UART1_RX |
| 11 | UART1_RTS | 12 | I2S2_SCLK |
| 13 | PWM01 / GPIO | 14 | GND |
| 15 | GPIO27 / PWM1 | 16 | GPIO08 (DMIC data) |
| 17 | +3.3 V | 18 | GPIO35 / PWM |
| 19 | SPI1_MOSI | 20 | GND |
| 21 | SPI1_MISO | 22 | GPIO17 |
| 23 | SPI1_SCLK | 24 | SPI1_CS0_N |
| 25 | GND | 26 | SPI1_CS1_N |
| 27 | I2C2_SDA | 28 | I2C2_SCL |
| 29 | CAN0_DIN | 30 | GND |
| 31 | CAN0_DOUT | 32 | GPIO09 (DMIC clock) |
| 33 | CAN1_DOUT | 34 | GND |
| 35 | I2S2_FS | 36 | UART1_CTS |
| 37 | CAN1_DIN | 38 | I2S2_DIN |
| 39 | GND | 40 | I2S2_DOUT |

Notes: SFIOs (I2S, SPI, PWM, CAN, I2C) are configured with Jetson-IO
(`sudo /opt/nvidia/jetson-io/jetson-io.py`); compatible strings
`nvidia,p3737-0000+p3701-000x`. I2C pins are open-drain (1 mA drive through level shifter); many pins route
via TI TXB0108 translators (weak drivers, overdriveable for bidirectional use);
some pins are direct 1 mA SoC I/O. Full electrical detail: SP-10900-001 Table 3-4
(`datasheets/`). Pin 1 = white triangle on PCB.

## Automation header (J42, 2x6)

Pins 1/12 GND; 2 = Force Recovery; 3 = Reset; 4 = Power; 5-6 jumpered = Auto
Power-On enable; 7 = MODULE_SLEEP_N; 8 = SYSTEM_OC_N; 9-10 jumpered = Wake-on-LAN
from off; 11 = JTAG_TRST.

## How to load the OS

1. **Arches build:** `orin` Yocto branch; flash per branch README.
2. **SDK path (JetPack 6.2.x):**
   - eMMC: `sudo ./flash.sh --erase-all jetson-agx-orin-devkit internal`
   - NVMe: `sudo ./l4t_initrd_flash.sh --external-device nvme0n1p1 -c tools/kernel_flash/flash_l4t_t234_nvme.xml --erase-all jetson-agx-orin-devkit external`
   - USB/SD rootfs: same initrd flow with `--external-device sda1|mmcblk0p1`
3. Force Recovery: power off → hold Force Recovery button → press+release Power →
   release. `lsusb` → `0955:7023` (dev/32GB) / `7223` (32GB P3701-0004) / `7023` (64GB).
4. Select the flashed boot media in the UEFI menu.

## How to log in

- **First boot (stock image):** follow the on-display setup wizard to create the
  user; log in on DP display, serial console, or SSH.
- **Serial console:** USB micro-B debug port (J26) — 115200 8N1, 8 data bits,
  no parity, 1 stop bit.
- **SSH over USB:** connect the flashing USB-C port (J40, device-mode capable) →
  `ssh <user>@192.168.55.1`. Or over Ethernet (RJ45) once networked.
- **Arches images:** user policy from the `orin` branch rootfs config.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/` (SP-10900-001 carrier spec, AGX Orin
dev kit user guide, module datasheet)
