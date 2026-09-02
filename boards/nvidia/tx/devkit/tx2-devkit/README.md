# Jetson TX2 Developer Kit (P2771-0000, carrier P2597)

| Item | Value |
|---|---|
| Carrier | P2597 (developer board; shared TX1/TX2 carrier spec) |
| Module | P3310 TX2 (also carries TX2i / TX2 4GB — see `../som/`) |
| Kit P/N | 945-82771-0000-000 (US) |
| Flash config | `jetson-tx2-devkit` / `jetson-tx2i` / `jetson-tx2-4gb` |
| L4T / JetPack | R32.7.x / 4.6.x (`tx` branch) |
| Mechanical | 170 × 170 mm board; 1.03 lb kit; 0–50 °C operating |

## Onboard hardware (verified — TX2 dev-kit datasheet + carrier spec)

| Block | Details |
|---|---|
| USB | 1x USB 3.0 Type-A (host only, J19) + 1x USB 2.0 Micro-AB (host + device/recovery, J20) |
| Display | HDMI Type-A (J16, HDMI 2.0 class); display expansion connector (eDP/DP + DSI 2×4, backlight/touch) |
| Storage | 32 GB eMMC (module); full-size SD slot (SDR104); **SATA data + power** (22-pin incl. 5 V/12 V rails; TX2-only `SATA_DEV_SLP`) |
| Network | RJ45 GbE |
| Wireless | 802.11ac + BT on module; dual U.FL antennas |
| Expansion | M.2 Key E (PCIe x1 + USB2 + UART + I2S + I2C; SDIO not routed on TX2); **PCIe x4 connector** (Gen2); 40-pin header; 30-pin GPIO header |
| Debug | JTAG 2×10 header (J7); debug connector 2×30 (J10: JTAG, UART, I2C ×3, reset/recovery/power control); serial header 1×6 (J17, 3.3 V) |
| Power | DC jack 5.5–19.6 V (J25, Singatron 2DC-213); 19 V AC adapter in kit (90 W-rated supply); power/reset/recovery/volume buttons; LEDs VDD_IN, power, SOC-enable, M.2, PCIe/SATA 12 V |
| Rails | VDD_5V0_IO_SYS 7 A, VDD_3V3_SYS 7 A, VDD_1V8 2 A, 12 V boost 2.3 A (PCIe/SATA), camera 2.8/1.8/1.2 V rails |
| Auto-power-on | TX2 only: tie CHARGER_PRSNT# to GND (R313) to power on without button press |

## 40-pin expansion header (J21, verified functions)

| Pins | Function |
|---|---|
| 1, 17 | +3.3 V; 2, 4 +5 V |
| 3, 5 | I2C GP0 (open-drain, 3.3 V) |
| 8, 10, 11, 36 | UART1 TX/RX/RTS/CTS (3.3 V) |
| 7, 12, 35, 38, 40 | Audio MCLK, I2S0 SCLK/FS/DIN/DOUT (level via J24) |
| 19/21/23/24/26 | SPI1 MOSI/MISO/SCK/CS0/CS1 |
| 27, 28 | I2C GP1 SDA/SCL |
| 13, 16, 29, 31–33, 37 | GPIO/DMIC/MDM_WAKE/AP_WAKE_BT/SAR per pinmux |
| 6, 9, 14, 20, 25, 30, 34, 39 | GND |

J24 jumper selects 1.8 V vs 3.3 V for translated signals. Per-pin Tegra ball +
GPIO-port tables (TX1 and TX2) are in the carrier spec — add to `datasheets/`.

## GPIO expansion header (J26, 30-pin) — TX2 features

CAN0 RX/TX/ERR (5/7/9), CAN1 RX/TX/ERR (15/17/19) + CAN1_STBY (13), CAN_WAKE (1),
I2S1 (23–26), I2C_GP2/GP3 @ 1.8 V (12/14/18/20), DSPK out (27/29), WDT output (16),
SLEEP indicator (22). **This is where the 2x CAN bus is exposed on TX2.**

## How to load the OS

1. Force Recovery: power on → hold RECOVERY FORCE → press+release RESET →
   release after 2 s (USB micro-B to host for flashing).
2. `sudo ./flash.sh jetson-tx2-devkit mmcblk0p1` (eMMC; or `sda1`/`mmcblk1p1`/
   `eth0` for USB/SD/NFS rootfs).
3. Arches: `tx` Yocto branch image, legacy tegraflash per branch README. UPHY
   lane map via `ODMDATA` (`p2771-0000.conf.common`).

## How to log in

- **Stock dev-kit image:** user `ubuntu` / `ubuntu`; newer JetPack 4.6.x images
  run the OEM setup wizard (create user).
- **Serial console:** J17 serial header (3.3 V) at 115200 8N1; UART0 @ 1.8 V on
  the 2×30 debug connector.
- **SSH:** USB 2.0 Micro-AB device mode → `ssh ubuntu@192.168.55.1`.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/` (P2597 carrier spec, P2597_C02
schematic design files, P3310 datasheet)
