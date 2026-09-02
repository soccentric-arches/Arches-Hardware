# Jetson TX2 (module P3489-0000; doc lists P3310 — `VERIFY`)

| Item | Value |
|---|---|
| Family / branch | `tx` · L4T R32.7.x · JetPack 4.6.x |
| Module P/N | P3489-0000 (`VERIFY`; branching doc §5.2 lists P3310, which is the dev-kit carrier P/N) |
| Dev kit / carrier | P2771-0000 dev kit (carrier board P3310) |
| Flash config (L4T) | `jetson-tx2-devkit` |
| Yocto MACHINE | `jetson-tx2-devkit` — `VERIFY` |

## Hardware specifications

| Spec | Value |
|---|---|
| SoC | NVIDIA Tegra X2 (T186, "Pascal") |
| CPU | Dual NVIDIA Denver 2 + Quad Arm Cortex-A57 (HMP), up to 2.0 GHz |
| GPU | Pascal GP10B, 256 CUDA cores |
| Memory | 8 GB 128-bit LPDDR4, 59.7 GB/s |
| Storage | 32 GB eMMC 5.1 |
| Power modes | 7.5 W / 15 W |
| Operating temp | `VERIFY` |

## Interfaces / I/O (module)

| Interface | Value |
|---|---|
| Camera | 12x MIPI CSI-2 lanes (2x4 + 2x2 or 6x2 groupings — `VERIFY`) |
| USB | 1x USB 3.1 + 3x USB 2.0 (module `VERIFY`; dev kit exposes 4x USB 3.0-class ports via hub) |
| Ethernet | 1x GbE MAC |
| Display | HDMI 2.0 + DP 1.2 |
| Storage | SDMMC; SATA supported on TX2 dev-kit carrier (`VERIFY`) |
| Low-speed | UART, I2C, I2S, SPI, PWM, CAN `VERIFY` (module pinout: TX2 Product Design Guide in `datasheets/`) |

## Internal hardware

- On-module PMIC/sequencer; RTC backup input; WiFi/BT on dev kit via M.2 Key E module.
- Boot: BCT/BootROM → CBoot from eMMC; Force Recovery via strap + USB OTG.
- Dev kit: 40-pin expansion header (GPIO/I2C/I2S/SPI/PWM), M.2 Key M + Key E,
  SD card slot, fan, power/reset/recovery buttons — details in `devkit/tx2-devkit`.

## How to load the OS

1. **Arches build**: `tx` Yocto branch image → legacy tegraflash.
2. **SDK path**: SDK Manager / L4T R32.7.x; Force Recovery (hold recovery while
   powering on), then:
   `sudo ./flash.sh jetson-tx2-devkit mmcblk0p1`
3. TX2i / TX2 4GB flash with `jetson-tx2i` / `jetson-tx2-4gb` on the same carrier.

## How to log in

- **First boot (stock dev-kit image):** default `nvidia` / `nvidia`; JetPack 4.6.x
  dev kits run an OEM setup wizard on first boot — create your user there.
- **Serial console:** USB micro-B debug port on the dev kit, 115200 8N1.
- **SSH over USB:** `ssh <user>@192.168.55.1` once the board is in device mode.
- **Arches images:** user policy set by the `tx` branch rootfs config.

## Artifacts

`schematics/` · `pcb/` · `bom/` · `datasheets/` (P3489 datasheet, TX2 OEM Product
Design Guide, P2771/P3310 carrier spec)
