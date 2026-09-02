# Jetson TX1 Developer Kit (P2371-2180)

| Item | Value |
|---|---|
| Carrier | P2597-class developer board (shared TX1/TX2 carrier) |
| Module | P2180 (see `../som/jetson-tx1`) |
| Flash config | `jetson-tx1-devkit` |
| L4T / JetPack | R32.7.x / 4.6.x (`tx` branch) |
| Dev-kit operating temp | 0–50 °C (carrier spec) |

## Onboard hardware (TX1 dev-kit product sheet + carrier spec, verified)

| Block | Details |
|---|---|
| USB | 1x USB 3.0 Type-A (host only, J19) + 1x USB 2.0 Micro-AB (host **and** device/recovery, J20) |
| Display | HDMI Type-A (J16); display expansion connector (2×60) exposes eDP/DP + DSI 2×4 with backlight/touch |
| Storage | 16 GB eMMC (module); full-size SD slot (SDR104/UHS-1, J12); **SATA data + power** (22-pin, J1) |
| Network | RJ45 GbE (J5) |
| Wireless | 802.11ac + BT radio on module; dual U.FL antenna connectors (2 antennas in kit) |
| Expansion | M.2 Key E (J18: PCIe x1 + **SDIO (TX1 only)** + USB2 + UART + I2S + I2C); **PCIe x4 connector** (J2, Gen2); 40-pin expansion header (J21); 30-pin GPIO expansion header (J26) |
| Debug | 60-pin (2×30) debug connector (J10: JTAG, UART0 @ 1.8 V, I2C); JTAG 2×10 header (J7); serial port header 1×6 (J17, UART1 3.3 V w/ flow control) |
| Power | DC jack 5.5–19.6 V (J25); external 19 V AC adapter in kit (90 W-rated supply); charge-control 10-pin flex receptacle (J27) |
| UI | Power (S4), Reset (S1), Force Recovery (S3), Volume-down/Sleep (S2) buttons; LEDs: VDD_IN (red), Power, SOC-enable, M.2 ×2, PCIe/SATA 12 V |
| Fan | 4-pin header (5 V, PWM, tach) |

## 40-pin expansion header (J21, verified pin functions)

| Pins | Function |
|---|---|
| 1, 17 | +3.3 V (1 A/pin) |
| 2, 4 | +5 V (1 A/pin) |
| 3, 5 | I2C #0 (SDA/SCL, open-drain, 3.3 V default; level via J24) |
| 8, 10, 11, 36 | UART1 TX/RX/RTS/CTS (3.3 V, 24 mA buffers) |
| 7 | AUDIO_MCLK; 12 I2S0 SCLK; 35 I2S0 LRCLK; 38/40 I2S0 DIN/DOUT |
| 19/21/23/24/26 | SPI1 MOSI/MISO/SCK/CS0/CS1 (1.8/3.3 V via J24) |
| 13, 15, 18, 22, 29, 31, 32, 33, 37, 38, 40 | GPIO / DMIC / codec-int / AP_WAKE_BT / SAR per pinmux |
| 6, 9, 14, 20, 25, 30, 34, 39 | GND |

Note: J24 (3-pin) selects 1.8 V vs 3.3 V for the TXB0108 level-shifted pins.
Full per-pin Tegra ball/GPIO tables in the carrier spec (`datasheets/`).

## GPIO expansion header (J26, 30-pin)

I2S1 (23/24/25/26), CAN0 RX/TX/ERR (5/7/9) and CAN1 RX/TX/ERR (15/17/19)
(**CAN is TX2-only** — pins inert with TX1), I2C_GP2/GP3 @ 1.8 V (12/14/18/20),
DSPK out (27/29, TX2-only), WDT output, AP2MDM_READY, sleep indicator.

## How to load the OS

1. Force Recovery: power off → USB micro-B to recovery port → power on →
   hold RECOVERY FORCE → press+release RESET → release after 2 s.
2. `sudo ./flash.sh jetson-tx1-devkit mmcblk0p1` (eMMC); `sda1`/`mmcblk1p1` for
   USB/SD rootfs.
3. Arches: `tx` Yocto branch image, legacy tegraflash per branch README.

## How to log in

- **Stock dev-kit image:** user `ubuntu` / password `ubuntu` (user guide);
  change before network exposure. OEM wizard runs on newer JetPack 4.6.x images.
- **Serial console:** J17 serial header (3.3 V) or J10 debug connector (1.8 V),
  115200 8N1.
- **SSH over USB:** USB 2.0 Micro-AB in device mode → `ssh ubuntu@192.168.55.1`.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/` (TX1 dev-kit user guide,
TX1/TX2 Developer Kit Carrier Board Specification + carrier design files)
