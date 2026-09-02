# tx — Tegra X1 / X2 generation

BSP line: **L4T R32.7.x (terminal) / JetPack 4.6.x** · `meta-tegra`
`kirkstone-l4t-r32.7.x` · Yocto `kirkstone` · Arches branch `tx`.
Flash path: legacy tegraflash via `flash.sh`.

## SOM coverage

| SOM | Module P/N | Dev kit / carrier | Folder |
|---|---|---|---|
| Jetson TX1 | P2180 | P2371-2180 dev kit | `som/jetson-tx1` |
| Jetson TX2 | P3310 (`VERIFY` — NVIDIA lists TX2 module as P3489-0000; P3310 is the dev-kit carrier) | P2771-0000 dev kit | `som/jetson-tx2` |
| Jetson TX2i | P3489-0000 (`VERIFY` — NVIDIA lists P3489-0008 for TX2i) | P2771 carrier | `som/jetson-tx2i` |
| Jetson TX2 4GB | P3489-0888 | P2771 carrier | `som/jetson-tx2-4gb` |
| Jetson TX2 NX | P3636 (`VERIFY` — NVIDIA lists P3449-0000 for TX2 NX) | P3509 / Nano dev kit carrier | `som/jetson-tx2-nx` |
| Jetson Nano (SD) | P3448-0000 | P3450 dev kit | `som/jetson-nano-sd` |
| Jetson Nano (eMMC) | P3448-0002 | P3449 carrier | `som/jetson-nano-emmc` |
| Jetson Nano 2GB | P3448-0003 | P3541 dev kit | `som/jetson-nano-2gb` |

Part numbers above are mirrored from `arches-yocto-generation-branching-requirements.md`
§5.2; the `VERIFY` flags record where the NVIDIA module datasheets differ. Resolve
against the pinned `meta-tegra` branch and NVIDIA datasheets before committing machine
names downstream.

## Generation facts

- No module in this generation has LPDDR5, NVMe-only boot, or UEFI boot — all use
  legacy CBoot/BCT flow flashed with `flash.sh`.
- Dev-kit first boot: JetPack 4.x images ship default user `nvidia` / password
  `nvidia` with auto-login on dev kits; change it on first network exposure.
- Serial console on dev kits: USB micro-B OTG port exposes the debug UART,
  115200 8N1.
- SSH over USB device mode: host enumerates RNDIS/NCM; board answers on
  `192.168.55.1`.

## Dev kits

| Dev kit | Carrier | Folder |
|---|---|---|
| Jetson TX1 Developer Kit | P2371-2180 | `devkit/tx1-devkit` |
| Jetson TX2 Developer Kit | P2771-0000 (carrier P3310) | `devkit/tx2-devkit` |
| Jetson Nano Developer Kit | P3450 | `devkit/nano-devkit` |
| Jetson Nano 2GB Developer Kit | P3541 | `devkit/nano-2gb-devkit` |

TX2i / TX2 4GB / TX2 NX / Nano eMMC have no dedicated dev kit — they are validated on
the carrier listed in the matrix (TX2i/4GB on the P2771 carrier, TX2 NX on P3509 /
Nano dev kit carrier, Nano eMMC on P3449).
