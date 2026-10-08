#!/usr/bin/env bash
# Haalt de afbeeldingen van de oude site op, ter vergelijking en hergebruik.
# Draai dit op je eigen computer: bash scripts/download-originals.sh
set -u
cd "$(dirname "$0")/.." || exit 1
mkdir -p images/original
base="https://slimmobiel.nl/site/wp-content/uploads/2016/03"
for f in slimmobiel.png slimmobiel-ellectra-1.png banner_bellier-2-1600x291.jpg banner_bellier-2.jpg button-bellier8.jpg ellectra-modellen.png; do
  if curl -fsSL "$base/$f" -o "images/original/$f"; then echo "ok   $f"; else echo "mis  $f"; rm -f "images/original/$f"; fi
done
if curl -fsSL "https://slimmobiel.nl/site/bellier/wp-content/uploads/sites/2/2016/03/logo-slimmobiel.png" -o images/original/logo-slimmobiel.png; then
  echo "ok   logo-slimmobiel.png"
else
  echo "mis  logo-slimmobiel.png"; rm -f images/original/logo-slimmobiel.png
fi
echo "Klaar. Bekijk images/original/ (deze map wordt niet mee-gecommit)."
