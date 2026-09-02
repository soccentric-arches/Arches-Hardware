# Jetson TX1 Developer Kit (P2371-2180)

| Item | Value |
|---|---|
| Carrier | P2371-2180 (TX1 dev kit carrier) |
| Module | P2180 (see `../som/jetson-tx1`) |
| Flash config | `jetson-tx1-devkit` |
| L4T / JetPack | R32.7.x / 4.6.x (`tx` branch) |

## Onboard hardware

| Block | Details |
|---|---|
| Display | HDMI 2.0 + DP 1.2 output |
| USB | 4x USB 3.0 Type-A (`VERIFY` port grouping via hub) |
| Ethernet | RJ45 GbE |
| Storage | microSD slot (`VERIFY`); eMMC on module |
| Expansion | 40-pin header (GPIO/I2C/I2S/SPI/PWM, Pi-compatible positions), CSI camera connector, M.2 slots (`VERIFY` key types) |
| Wireless | 802.11ac 2x2 WiFi + BT 4.1 module fitted |
| Debug | USB OTG/micro-B debug UART (115200 8N1) |
| Power | DC barrel jack (`VERIFY` voltage, ~12-19 V class) + power button |
| Buttons/LED | Power, Force Recovery, Reset; power LED |
| Mechanical | Handheld dev-kit form factor with fan (`VERIFY` dimensions) |

Full connector pinouts: see the TX1 Developer Kit user guide / carrier schematic in
`datasheets/` and `schematics/`.

## 40-pin header

Pi-compatible 40-pin layout on TX-generation dev kits: 3.3 V / 5 V rails, GND,
UART1 (TX/RX), I2C, I2S, SPI, PWM and GPIO. Exact per-pin mapping differs from
Raspberry Pi — use Jetson-IO / the carrier pinmux table in `datasheets/`
(`VERIFY` per-pin table before wiring).

## How to load the OS

1. Force Recovery: hold the recovery button while powering on.
2. `sudo ./flash.sh jetson-tx1-devkit mmcblk0p1` (L4T R32.7.x BSP) or via SDK Manager.
3. Arches: build on the `tx` Yocto branch and flash with the branch's documented
   legacy tegraflash command.

## How to log in

- First boot (stock image): default `nvidia` / `nvidia` (or OEM wizard on 4.6.x
  dev-kit images) — change credentials immediately.
- Serial console: USB debug port, 115200 8N1.
- SSH over USB device mode: `ssh nvidia@192.168.55.1`.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/`
