#!/usr/bin/env bash
# capture-gallery.sh — sequential screenshot capture for the Awesome PHP AI gallery.
#
# Reads gallery-routes.txt and captures every route at TWO viewports — desktop and mobile —
# one after another, writing PNGs into an output directory. Uses the established headless
# capture helper `shot-scraper` by default (pip install shot-scraper && shot-scraper install).
# Override the helper with CAPTURE_CMD if your environment uses a different one.
#
# This script starts NO server and points at the already-served .test host. Generated, not
# executed by the :prototype workflow — run it yourself when you want images.
#
# Usage:  ./capture-gallery.sh
# Env:    CAPTURE_CMD    capture command template; {url} {w} {h} {out} are substituted
#                          (default: shot-scraper "{url}" --width {w} --height {h} -o "{out}")
#         CAPTURE_OUT    output directory (default: ../screenshots, i.e. prototypes/screenshots)
#         CAPTURE_DELAY  wait (ms) before capture for paint/animation (default 600)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MANIFEST="${SCRIPT_DIR}/gallery-routes.txt"
OUT_DIR="${CAPTURE_OUT:-${SCRIPT_DIR}/../screenshots}"
DELAY="${CAPTURE_DELAY:-600}"
CAPTURE_CMD_DEFAULT='shot-scraper "{url}" --width {w} --height {h} --wait '"$DELAY"' -o "{out}"'
CAPTURE_CMD="${CAPTURE_CMD:-$CAPTURE_CMD_DEFAULT}"

if [[ ! -f "$MANIFEST" ]]; then
  echo "FAIL: manifest not found at $MANIFEST" >&2
  exit 2
fi

mkdir -p "$OUT_DIR"

# Desktop + mobile viewports, captured sequentially per route.
declare -a LABELS=(desktop mobile)
declare -a WIDTHS=(1440 390)
declare -a HEIGHTS=(900 844)

mapfile -t ROUTES < <(grep -vE '^\s*(#|$)' "$MANIFEST")

printf '==> Capturing %d routes x %d viewports -> %s\n' "${#ROUTES[@]}" "${#LABELS[@]}" "$(cd "$OUT_DIR" && pwd)"
printf '    helper: %s\n\n' "$CAPTURE_CMD"

slug_from_url() {
  # https://awesome-php-ai.test/prototypes/examples/variant-03/  ->  variant-03
  # https://awesome-php-ai.test/prototypes/                     ->  index
  local u="$1" s
  s="${u%/}"                       # strip trailing slash
  s="${s##*/}"                     # last path segment
  [[ -z "$s" ]] && s="index"
  printf '%s' "$s"
}

i=0
for url in "${ROUTES[@]}"; do
  url="${url%%[[:space:]]}"
  [[ -z "$url" ]] && continue
  slug="$(slug_from_url "$url")"

  for v in "${!LABELS[@]}"; do
    label="${LABELS[$v]}"
    w="${WIDTHS[$v]}"
    h="${HEIGHTS[$v]}"
    out="${OUT_DIR%/}/${slug}--${label}.png"
    cmd="${CAPTURE_CMD//\{url\}/$url}"
    cmd="${cmd//\{w\}/$w}"
    cmd="${cmd//\{h\}/$h}"
    cmd="${cmd//\{out\}/$out}"
    printf '  [%s] %sx%s  %s\n' "$label" "$w" "$h" "$slug"
    # shellcheck disable=SC2086  — intentional word-splitting of the command template.
    eval "$cmd" >/dev/null
    i=$((i+1))
  done
done

printf '\n==> Captured %d screenshots into %s\n' "$i" "$(cd "$OUT_DIR" && pwd)"
