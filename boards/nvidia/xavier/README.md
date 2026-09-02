# xavier — Volta Xavier generation

BSP line: **L4T R35.6.x (terminal — JetPack 6 dropped Xavier) / JetPack 5.1.x** ·
`meta-tegra` `kirkstone` · Yocto `kirkstone` · Arches branch `xavier`.
Flash path: legacy `flash.sh` (eMMC) — see per-board READMEs.

## SOM coverage

| SOM | Module P/N | Dev kit / carrier | Folder |
|---|---|---|---|
| AGX Xavier 8/16/32/64 GB | P2888 variants (`VERIFY` exact P/N per SKU, e.g. P2888-0004 16 GB / -0006 32 GB) | P2972-0000 dev kit (carrier P2822) | `som/agx-xavier` |
| AGX Xavier Industrial | P2888-0008 | P2972 carrier | `som/agx-xavier` (industrial row) |
| Xavier NX (SD) | P3668-0000 | P3509 dev kit | `som/xavier-nx-sd` |
| Xavier NX (eMMC) | P3668-0001 (production; **P3668-0003 = 16 GB RAM variant**, verified) | P3509 / P3449 carrier | `som/xavier-nx-emmc` |

Part numbers mirrored from the branching doc §5.2; `VERIFY` flags mark values to
reconcile against NVIDIA datasheets and the pinned `meta-tegra` branch.

## Generation facts

- CPU: NVIDIA Carmel (custom ARMv8.2) cores; GPU: Volta with Tensor Cores; DLA v1
  and PVA v1 accelerators.
- UEFI/CBoot boot chain (R35); eMMC on AGX/Xavier NX eMMC SKU, microSD on NX SD SKU.
- Dev-kit first boot (JetPack 5.1.x): OEM setup wizard creates the user; legacy
  default `nvidia`/`nvidia` on older images.
- Serial console: dev-kit debug USB (micro-B/USB-C) at 115200 8N1; SSH over USB
  device mode at `192.168.55.1`.

## Dev kits

| Dev kit | Carrier | Folder |
|---|---|---|
| AGX Xavier Developer Kit | P2972-0000 (carrier P2822) | `devkit/agx-xavier-devkit` |
| Xavier NX Developer Kit | P3509 | `devkit/xavier-nx-devkit` |

AGX Xavier Industrial has no dedicated dev kit — validated on the P2972 carrier.
