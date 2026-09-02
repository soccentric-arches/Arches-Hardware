# NVIDIA families

Arches supports all four NVIDIA Jetson generations. Generations are locked to a
distinct L4T/JetPack release → `meta-tegra` branch → Yocto/OE-Core release (see
`arches-yocto-generation-branching-requirements.md` §5.1). One build tree cannot
serve two generations; likewise keep hardware knowledge in the matching family folder.

| Family | Generation | Branch | L4T | JetPack | `meta-tegra` | Yocto | Flash path |
|---|---|---|---|---|---|---|---|
| `tx` | Tegra X1/X2 (Maxwell/Pascal) | `tx` | R32.7.x (terminal) | 4.6.x | `kirkstone-l4t-r32.7.x` | kirkstone | legacy `flash.sh` (tegraflash) |
| `xavier` | Volta Xavier | `xavier` | R35.6.x (terminal) | 5.1.x | `kirkstone` | kirkstone | legacy `flash.sh` / initrd |
| `orin` | Ampere Orin | `orin` | R36.4.x | 6.2.x | `scarthgap` | scarthgap | `flash.sh` (AGX eMMC) or `l4t_initrd_flash.sh` (NX/Nano + NVMe/USB/SD) |
| `thor` | Blackwell Thor | `thor` | R38.2.x or later | 7.x | `master`-line Thor branch — `VERIFY` | current OE-Core compat | unified `l4t_initrd_flash.sh` |

Notes (from the branching requirements, §5.1):
- `tx` (R32.7.x) is the terminal release for TX1/TX2/Nano — no further upstream releases.
- `xavier` (R35.x) is the terminal Xavier line; JetPack 6 dropped Xavier.
- L4T R38.x supports **Thor only**; Orin machines in that tree are non-functional and
  out of scope for the `thor` branch.
- `VERIFY` = confirm against the pinned `meta-tegra` branch before relying on it.

## Coverage (mirrors branching doc §5.2)

| Family | SOMs | Devkits |
|---|---|---|
| tx | TX1, TX2, TX2i, TX2 4GB, TX2 NX, Nano (SD), Nano (eMMC), Nano 2GB | TX1 dev kit, TX2 dev kit, Nano dev kit, Nano 2GB dev kit |
| xavier | AGX Xavier (8/16/32/64 GB), AGX Xavier Industrial, Xavier NX (SD), Xavier NX (eMMC) | AGX Xavier dev kit (P2972), Xavier NX dev kit (P3509) |
| orin | AGX Orin 32GB/64GB/Industrial, Orin NX 16GB/8GB, Orin Nano 8GB (incl. Super)/4GB | AGX Orin dev kit (P3737), Orin Nano dev kit (P3768) |
| thor | AGX Thor T5000, T4000 | AGX Thor dev kit (P4071) |

Every SOM row also lists the dev kit / reference carrier it is validated on — see the
family `README.md` matrix and each SOM folder.
