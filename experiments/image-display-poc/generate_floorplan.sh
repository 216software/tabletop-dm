#!/usr/bin/env bash
# POC only: renovation needs matplotlib/numpy/PyYAML and Python >= 3.10, which
# dm.py's own hard constraints (stdlib-only, py3.9, no installs) rule out.
# This script is a content-authoring aid, not something dm.py ever calls.
# Run from this directory: ./generate_floorplan.sh [config.yml]
set -euo pipefail
cd "$(dirname "$0")"
CONFIG="${1:-dungeon.yml}"
if [ ! -x venv/bin/python ]; then
  python3 -m venv venv
  ./venv/bin/pip install -q renovation
fi
./venv/bin/python -m renovation -c "$CONFIG"
echo "Wrote PNG(s) into ./output — open with the Read tool or an image viewer."
