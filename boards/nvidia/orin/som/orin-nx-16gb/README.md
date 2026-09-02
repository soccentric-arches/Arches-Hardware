# Orin NX 16GB (module P3767-0000)

| Item | Value |
|---|---|
| Family / branch | `orin` · L4T R36.4.x · JetPack 6.2.x |
| Module P/N | P3767-0000 |
| Dev kit / carrier | P3768 Orin Nano carrier; P3509 Xavier NX carrier |
| Flash config (L4T) | `jetson-orin-nano-devkit` (NX on P3768 — same config as Nano) |
| Yocto MACHINE | `jetson-orin-nano-devkit` (NX on P3768) / P3509 variant — `VERIFY` |

## Hardware specifications (DS-10712-001, verified)

| Spec | Value |
|---|---|
| SoC | NVIDIA Orin NX (low-power Orin) |
| CPU | 8x Arm Cortex-A78AE v8.2 @ 2 GHz |
| GPU | Ampere, 1024 CUDA cores + 32 Tensor Cores, up to 918 MHz (1173 MHz Super) |
| DLA / PVA | 2x NVDLA v2.0 (up to 40 TOPS sparse) / 1x PVA v2.0 |
| AI perf | 100 (sparse) / 50 (dense) INT8 TOPS; 157/78 TOPS (MAXN_SUPER) |
| Memory | 16 GB 128-bit LPDDR5, 102.4 GB/s (3200 MHz) |
| Storage | **no eMMC** — external NVMe (PCIe) or USB 3.2 SSD; boot from on-module QSPI-NOR |
| Camera | 8x MIPI CSI-2 lanes (2x4 or 4x2, D-PHY 2.1, 20 Gbps) |
| Video | decode 1x 8K30 / 2x 4K60 (H.265); encode 1x 4K60 (H.265/AV1) |
| Display | 1x shared HDMI 2.1 / DP 1.4a (up to 8K30) |
| Power modes | 10 W / 15 W / 25 W / 40 W (MAXN_SUPER; needs ≥8 V VDD_IN) |
| Form factor | 260-pin SODIMM, 69.6 × 45 mm |

## Interfaces / I/O (module, verified)

| Interface | Value |
|---|---|
| USB | 3x USB 3.2 Gen2 (10 Gbps) + 3x USB 2.0 (USB0 = RCM/device mode) |
| PCIe | 4 controllers: 1x4 + 3x1 (or 1x2+1x1 + 1x4) **Gen4** |
| Ethernet | 1x GbE MAC |
| CAN | 1x CAN (M_TTCAN 3.2, up to 8 Mbps) |
| Low-speed | 3x UART, 2x SPI, 4x I2C, 2x I2S, 4x PWM, 15x dedicated GPIO |
| GPIO voltages | most I/O 1.8 V CMOS; I2C0/1 3.3 V open-drain; CAN 3.3 V |
| Power input | VDD_IN 5-20 V (MODULE_ID strap; ≥8 V for MAXN_SUPER) |

## Internal hardware

- On-module PMIC/sequencer + RTC (PMIC_BBAT input, non-rechargeable cell only).
- 64 MB QSPI-NOR boot device (no eMMC on this module family).
- Force Recovery strap (pin 214); MODULE_ID strap (pin 217).
- 15 dedicated GPIOs (GPIO00-GPIO14); GPIO08 = fan tach capable; 4x PWM-capable pins.

## How to load the OS

1. **Arches build:** `orin` Yocto branch → initrd-flash path (NX/Nano use
   `l4t_initrd_flash.sh`, not plain `flash.sh`).
2. **SDK path (JetPack 6.2.x):** Force Recovery, then rootfs on NVMe/USB/SD:
   `sudo ./l4t_initrd_flash.sh --erase-all jetson-orin-nano-devkit internal` (NVMe)
   — same config carries Orin NX on the P3768 carrier; select the flashed media in
   the UEFI menu.
3. Rootfs storage must be ≥64 GB for SD/USB flows.
4. Confirm recovery mode via `lsusb` (`0955:7323`).

## How to log in

- First boot: on-display OEM setup wizard creates the user (stock image).
- Serial console: 115200 8N1 — via USB-C device port (ttyGS0) on the P3768 carrier
  or the 40-pin UART pins (`VERIFY` routing per carrier).
- SSH: USB device mode → `192.168.55.1`; or Ethernet once configured.

## 260-pin SODIMM module connector — complete verified pin list (module datasheet pin list)

Odd-numbered pins on top, even on bottom. `X → Y` = SODIMM signal name → Orin
function (pinmux). Voltage classes: GPIO00–14, I2S, SPI0/1, UART0/1 = 1.8 V
CMOS; CAN = 3.3 V; I2C0/1 + CAM_I2C = 3.3 V open-drain; I2C2 = 1.8 V
open-drain; GBE = MDI; USB/PCIe/DP = dedicated PHYs. MODULE_ID strap (pin 217)
selects VDD_IN 5 V (Nano, tied low) vs 5–20 V (NX, floating).

| Odd | Signal | Even | Signal |
|---|---|---|---|
| 1 | GND | 2 | GND |
| 3 | CSI1_D0_N | 4 | CSI0_D0_N |
| 5 | CSI1_D0_P | 6 | CSI0_D0_P |
| 7 | GND | 8 | GND |
| 9 | CSI1_CLK_N | 10 | CSI0_CLK_N |
| 11 | CSI1_CLK_P | 12 | CSI0_CLK_P |
| 13 | GND | 14 | GND |
| 15 | CSI1_D1_N | 16 | CSI0_D1_N |
| 17 | CSI1_D1_P | 18 | CSI0_D1_P |
| 19 | GND | 20 | GND |
| 21 | CSI3_D0_N | 22 | CSI2_D0_N |
| 23 | CSI3_D0_P | 24 | CSI2_D0_P |
| 25 | GND | 26 | GND |
| 27 | CSI3_CLK_N | 28 | CSI2_CLK_N |
| 29 | CSI3_CLK_P | 30 | CSI2_CLK_P |
| 31 | GND | 32 | GND |
| 33 | CSI3_D1_N | 34 | CSI2_D1_N |
| 35 | CSI3_D1_P | 36 | CSI2_D1_P |
| 37 | GND | 38 | GND |
| 39 | DP0_TXD0_N → USBSS1_RX_N | 40 | CSI4_D2_N → PCIE2_RX0_N |
| 41 | DP0_TXD0_P → USBSS1_RX_P | 42 | CSI4_D2_P → PCIE2_RX0_P |
| 43 | GND | 44 | GND |
| 45 | DP0_TXD1_N → USBSS1_TX_N | 46 | CSI4_D0_N → PCIE2_TX0_N |
| 47 | DP0_TXD1_P → USBSS1_TX_P | 48 | CSI4_D0_P → PCIE2_TX0_P |
| 49 | GND | 50 | GND |
| 51 | DP0_TXD2_N → USBSS2_RX_N | 52 | CSI4_CLK_N → PCIE2_CLK_N |
| 53 | DP0_TXD2_P → USBSS2_RX_P | 54 | CSI4_CLK_P → PCIE2_CLK_P |
| 55 | GND | 56 | GND |
| 57 | DP0_TXD3_N → USBSS2_TX_N | 58 | CSI4_D1_N → PCIE2_RX1_N (NX alt: PCIE3_RX0_N) |
| 59 | DP0_TXD3_P → USBSS2_TX_P | 60 | CSI4_D1_P → PCIE2_RX1_P (NX alt: PCIE3_RX0_P) |
| 61 | GND | 62 | GND |
| 63 | DP1_TXD0_N | 64 | CSI4_D3_N → PCIE2_TX1_N (NX alt: PCIE3_TX0_N) |
| 65 | DP1_TXD0_P | 66 | CSI4_D3_P → PCIE2_TX1_P (NX alt: PCIE3_TX0_P) |
| 67 | GND | 68 | GND |
| 69 | DP1_TXD1_N | 70 | DSI_D0_N → RSVD |
| 71 | DP1_TXD1_P | 72 | DSI_D0_P → RSVD |
| 73 | GND | 74 | GND |
| 75 | DP1_TXD2_N | 76 | DSI_CLK_N → RSVD |
| 77 | DP1_TXD2_P | 78 | DSI_CLK_P → RSVD |
| 79 | GND | 80 | GND |
| 81 | DP1_TXD3_N | 82 | DSI_D1_N → RSVD |
| 83 | DP1_TXD3_P | 84 | DSI_D1_P → RSVD |
| 85 | GND | 86 | GND |
| 87 | GPIO00 | 88 | DP0_HPD → RSVD |
| 89 | SPI0_MOSI | 90 | DP0_AUX_N → RSVD |
| 91 | SPI0_SCK | 92 | DP0_AUX_P → RSVD |
| 93 | SPI0_MISO | 94 | HDMI_CEC |
| 95 | SPI0_CS0# | 96 | DP1_HPD |
| 97 | SPI0_CS1# | 98 | DP1_AUX_N |
| 99 | UART0_TXD | 100 | DP1_AUX_P |
| 101 | UART0_RXD | 102 | GND |
| 103 | UART0_RTS# | 104 | SPI1_MOSI |
| 105 | UART0_CTS# | 106 | SPI1_SCK |
| 107 | GND | 108 | SPI1_MISO |
| 109 | USB0_D_N | 110 | SPI1_CS0# |
| 111 | USB0_D_P | 112 | SPI1_CS1# |
| 113 | GND | 114 | CAM0_PWDN |
| 115 | USB1_D_N | 116 | CAM0_MCLK |
| 117 | USB1_D_P | 118 | GPIO01 (generic clock) |
| 119 | GND | 120 | CAM1_PWDN |
| 121 | USB2_D_N | 122 | CAM1_MCLK |
| 123 | USB2_D_P | 124 | GPIO02 |
| 125 | GND | 126 | GPIO03 |
| 127 | GPIO04 | 128 | GPIO05 |
| 129 | GND | 130 | GPIO06 |
| 131 | PCIE0_RX0_N | 132 | GND |
| 133 | PCIE0_RX0_P | 134 | PCIE0_TX0_N |
| 135 | GND | 136 | PCIE0_TX0_P |
| 137 | PCIE0_RX1_N | 138 | GND |
| 139 | PCIE0_RX1_P | 140 | PCIE0_TX1_N |
| 141 | GND | 142 | PCIE0_TX1_P |
| 143 | CAN_RX | 144 | GND |
| 145 | CAN_TX | 146 | GND |
| 147 | GND | 148 | PCIE0_TX2_N |
| 149 | PCIE0_RX2_N | 150 | PCIE0_TX2_P |
| 151 | PCIE0_RX2_P | 152 | GND |
| 153 | GND | 154 | PCIE0_TX3_N |
| 155 | PCIE0_RX3_N | 156 | PCIE0_TX3_P |
| 157 | PCIE0_RX3_P | 158 | GND |
| 159 | GND | 160 | PCIE0_CLK_N |
| 161 | USBSS0_RX_N | 162 | PCIE0_CLK_P |
| 163 | USBSS0_RX_P | 164 | GND |
| 165 | GND | 166 | USBSS0_TX_N |
| 167 | PCIE1_RX0_N | 168 | USBSS0_TX_P |
| 169 | PCIE1_RX0_P | 170 | GND |
| 171 | GND | 172 | PCIE1_TX0_N |
| 173 | PCIE1_CLK_N | 174 | PCIE1_TX0_P |
| 175 | PCIE1_CLK_P | 176 | GND |
| 177 | GND | 178 | MOD_SLEEP# |
| 179 | PCIE_WAKE# | 180 | PCIE0_CLKREQ# |
| 181 | PCIE0_RST# | 182 | PCIE1_CLKREQ# |
| 183 | PCIE1_RST# | 184 | GBE_MDI0_N |
| 185 | I2C0_SCL (3.3 V, 1.5 kΩ PU) | 186 | GBE_MDI0_P |
| 187 | I2C0_SDA | 188 | GBE_LED_LINK |
| 189 | I2C1_SCL (3.3 V, 2.2 kΩ PU) | 190 | GBE_MDI1_N |
| 191 | I2C1_SDA | 192 | GBE_MDI1_P |
| 193 | I2S0_DOUT | 194 | GBE_LED_ACT |
| 195 | I2S0_DIN | 196 | GBE_MDI2_N |
| 197 | I2S0_FS | 198 | GBE_MDI2_P |
| 199 | I2S0_SCLK | 200 | GND |
| 201 | GND | 202 | GBE_MDI3_N |
| 203 | UART1_TXD | 204 | GBE_MDI3_P |
| 205 | UART1_RXD | 206 | GPIO07 (PWM) |
| 207 | UART1_RTS# | 208 | GPIO08 (fan tach) |
| 209 | UART1_CTS# | 210 | CLK_32K_OUT |
| 211 | GPIO09 | 212 | GPIO10 |
| 213 | CAM_I2C_SCL (3.3 V) | 214 | FORCE_RECOVERY# |
| 215 | CAM_I2C_SDA | 216 | GPIO11 (generic clock) |
| 217 | GND → MODULE_ID strap | 218 | GPIO12 (PWM) |
| 219 | SDMMC_DAT0 → PCIE2_RST# | 220 | I2S1_DOUT |
| 221 | SDMMC_DAT1 → PCIE2_CLKREQ# | 222 | I2S1_DIN |
| 223 | SDMMC_DAT2 → PCIE3_RST# | 224 | I2S1_FS |
| 225 | SDMMC_DAT3 → PCIE3_CLKREQ# | 226 | I2S1_SCLK |
| 227 | SDMMC_CMD → PCIE3_CLK_N | 228 | GPIO13 (PWM) |
| 229 | SDMMC_CLK → PCIE3_CLK_P | 230 | GPIO14 (PWM) |
| 231 | GND | 232 | I2C2_SCL (1.8 V, OD) |
| 233 | SHUTDOWN_REQ# | 234 | I2C2_SDA (1.8 V, OD) |
| 235 | PMIC_BBAT (RTC backup) | 236 | UART2_TXD |
| 237 | POWER_EN | 238 | UART2_RXD |
| 239 | SYS_RESET# | 240 | SLEEP/WAKE# |
| 241 | GND | 242 | GND |
| 243 | GND | 244 | GND |
| 245 | GND | 246 | GND |
| 247 | GND | 248 | GND |
| 249 | GND | 250 | GND |
| 251 | VDD_IN | 252 | VDD_IN |
| 253 | VDD_IN | 254 | VDD_IN |
| 255 | VDD_IN | 256 | VDD_IN |
| 257 | VDD_IN | 258 | VDD_IN |
| 259 | VDD_IN | 260 | VDD_IN |

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/` (DS-10712-001, NX Product Design
Guide, P3768 carrier)
