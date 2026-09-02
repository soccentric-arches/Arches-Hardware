# Jetson Nano (SD variant, module P3448-0000)

| Item | Value |
|---|---|
| Family / branch | `tx` · L4T R32.7.x · JetPack 4.6.x |
| Module P/N | P3448-0000 (no eMMC — boots microSD) |
| Dev kit / carrier | P3450 dev kit |
| Flash config (L4T) | `jetson-nano` (image written to microSD) |
| Yocto MACHINE | `jetson-nano` — `VERIFY` |

## Hardware specifications

| Spec | Value |
|---|---|
| SoC | NVIDIA Tegra X1 (T210) |
| CPU | Quad-core Arm Cortex-A57 @ 1.43 GHz |
| GPU | Maxwell, 128 CUDA cores @ 921 MHz (472 GFLOPS FP16) |
| Memory | 4 GB 64-bit LPDDR4, 25.6 GB/s |
| Storage | none on module — microSD on carrier (16 GB+ UHS-1 recommended) |
| Power modes | 5 W / 10 W |

## Interfaces / I/O

| Interface | Value |
|---|---|
| Camera | 1x MIPI CSI-2 (4-lane, 15-pin camera connector on dev kit) |
| USB | 1x USB 3.0 + 3x USB 2.0 (module exposes 1x USB3 + 3x USB2 — `VERIFY` per-carrier mapping) |
| Ethernet | GbE MAC (RGMII) |
| Display | HDMI 2.0 + DP 1.2 |
| Low-speed | 40-pin header: UART, I2C, I2S, SPI, PWM, GPIO (see `devkit/nano-devkit`) |
| Form factor | 260-pin SODIMM, 69.6 × 45 mm |

## Internal hardware

- On-module PMIC; boot from microSD (BootROM → CBoot); no eMMC.
- WiFi/BT: none — dev kit provides M.2 Key E slot for wireless module.
- Recovery: force-recovery via jumper/button on carrier + USB OTG.

## How to load the OS

- **Stock JetPack:** write the Nano SD-card image to a microSD (SD Card Image from
  JetPack 4.6.x) and boot — no host flashing needed. SDK Manager can also flash via
  `flash.sh jetson-nano mmcblk0p1` for eMMC-rooted flows.
- **Arches build:** `tx` Yocto branch produces the image; deploy to microSD or flash
  per the branch README (legacy tegraflash path).

## How to log in

- **First boot (stock dev-kit image):** OEM setup wizard creates the user; legacy
  images default `nvidia`/`nvidia`.
- **Serial console:** micro-USB debug port on the dev kit, 115200 8N1.
- **SSH:** USB device mode → `192.168.55.1`, or over Ethernet/WiFi once configured.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/` (P3448 datasheet, Nano dev kit user guide)
