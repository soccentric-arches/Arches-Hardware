# CLAUDE.md - Arches-Hardware

See [project_specs.md](project_specs.md) for what this repo is.

## Notes

* For the Loop Engine: listing this repo in a loop's `repos:` is a scope violation, and it has no `.claude/validate.sh` because it has no build. It does receive the fleet-wide feature branch like every other repo (spec section-8.2) — read-only governs file content, not refs.
