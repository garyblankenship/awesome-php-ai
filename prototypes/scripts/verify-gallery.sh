#!/usr/bin/env bash
# verify-gallery.sh — route-aware structural verification for the Awesome PHP AI gallery.
#
# For every route in gallery-routes.txt it checks, against the already-served .test host:
#   1. the URL answers HTTP 200, and
#   2. the served HTML carries the ownership marker  <meta name="generator" content="prototype-skill">
#   3. (variants only) the page links back to the selector (relative '../../index.html').
#
# This script starts NO server. Point a local static server / Valet at the repo so that
# https://awesome-php-ai.test/prototypes/ resolves, then run this. Generated, not executed
# by the :prototype workflow — run it yourself when you want to verify.
#
# Usage:  ./verify-gallery.sh
# Env:    GALLERY_TIMEOUT   per-request curl timeout in seconds (default 15)
#         GALLERY_HOST      override the expected host (default awesome-php-ai.test)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MANIFEST="${SCRIPT_DIR}/gallery-routes.txt"
TIMEOUT="${GALLERY_TIMEOUT:-15}"
HOST="${GALLERY_HOST:-awesome-php-ai.test}"

if [[ ! -f "$MANIFEST" ]]; then
  echo "FAIL: manifest not found at $MANIFEST" >&2
  exit 2
fi

pass=0
fail=0
failures=()

# Read non-comment, non-blank routes.
mapfile -t ROUTES < <(grep -vE '^\s*(#|$)' "$MANIFEST")

printf '==> Verifying %d routes against host %s (timeout %ss)\n\n' "${#ROUTES[@]}" "$HOST" "$TIMEOUT"

for url in "${ROUTES[@]}"; do
  url="${url%%[[:space:]]}"
  [[ -z "$url" ]] && continue

  code="$(curl -fsS --max-time "$TIMEOUT" -o /dev/null -w '%{http_code}' "$url" 2>/dev/null || true)"
  body="$(curl -fsS --max-time "$TIMEOUT" "$url" 2>/dev/null || true)"

  reasons=()
  [[ "$code" == "200" ]] || reasons+=("HTTP ${code:-no-response}")
  grep -q 'name="generator" content="prototype-skill"' <<<"$body" \
    || reasons+=("missing generator meta")
  # Variants live under /examples/variant-NN/ and link back to the selector.
  if [[ "$url" == */examples/variant-* ]]; then
    grep -q '\.\./\.\./index\.html' <<<"$body" || reasons+=("missing selector back-link")
  fi

  if (( ${#reasons[@]} == 0 )); then
    printf '  PASS  %s\n' "$url"
    pass=$((pass+1))
  else
    printf '  FAIL  %s  [%s]\n' "$url" "${reasons[*]}"
    fail=$((fail+1))
    failures+=("$url")
  fi
done

printf '\n==> %d passed, %d failed of %d\n' "$pass" "$fail" "${#ROUTES[@]}"
if (( fail > 0 )); then
  printf 'Failed routes:\n'
  printf '  %s\n' "${failures[@]}"
  exit 1
fi
