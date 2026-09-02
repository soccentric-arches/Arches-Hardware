# boards/ — Arches supported hardware (single point of source)

This tree is the **single point of source for all hardware supported by the Arches
system**. Everything hardware-related about a supported SOM or developer kit lives
here: electrical specs, I/O, GPIO, pinouts, memory/storage, power, thermal,
mechanical, flashing procedure, and first-boot login.

## Layout

```
boards/nvidia/<family>/
├── README.md            # family overview: branch pins, coverage matrix, flash path
├── som/<module>/        # one folder per SOM (system-on-module)
└── devkit/<devkit>/     # one folder per NVIDIA developer kit / reference carrier
```

Families mirror the Arches Yocto generation branches (`arches-yocto-generation-branching-requirements.md`):
`tx`, `xavier`, `orin`, `thor`. Generations are BSP-incompatible; do not mix hardware
facts across family folders.

## What each board folder stores

The **main file is `README.md`** and contains, in order:

1. Identity — module/carrier part numbers, flash config name, L4T/JetPack, status
2. Hardware specifications — CPU/GPU/DLA/PVA, memory, storage, power, thermal
3. Interfaces / I/O — CSI, USB, PCIe, Ethernet, display, CAN, UART/I2C/I2S/SPI, GPIO
4. Devkits: onboard connectors, 40-pin header pinout, buttons/LEDs, power input
5. Internal hardware — PMIC/RTC, onboard WiFi/BT, storage, fan, debug ports
6. How to load the OS — SDK Manager + `flash.sh`/`l4t_initrd_flash.sh` command
   for the exact board config, plus the Arches Yocto branch that builds it
7. How to log in — first-boot user setup, serial console, SSH over USB

Subfolders (populate as design data becomes available):

| Folder | Contents |
|---|---|
| `schematics/` | revisioned schematic sources (PDF + EDA project) |
| `pcb/` | PCB layout + fabrication/assembly outputs (Gerber, ODB++, pick&place) |
| `bom/` | bill of materials |
| `datasheets/` | NVIDIA module/carrier datasheets, design guides, user guides |

## Honesty rule

Unverified values are marked **`VERIFY`** — do not silently fabricate part numbers,
machine names, or specs. The Arches Yocto requirement doc (§9.4) makes fabrication a
failure condition. A missing artifact is not evidence that a capability exists.

## Arches custom carrier

The Arches carrier board (Jetson SOM + STM32 real-time co-processor) is a separate,
human-owned design. Its design files live with the hardware owner; the SOM folders
here document the module interfaces that carrier must implement.
