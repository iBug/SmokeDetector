#!/bin/bash

set -e

ORIGIN=https://github.com/iBug/SmokeDetector.git
UPSTREAM=https://github.com/Charcoal-SE/SmokeDetector.git

if [ -z "$GH_TOKEN" ]; then
  echo "\$GH_TOKEN not set. Abort." >&2
  exit 1
fi

git clone "$UPSTREAM" build
SAVE_PWD=$PWD
cd build

git remote add upload "https://$GH_TOKEN@github.com/iBug/SmokeDetector.git" &>/dev/null
git push upload master --force &>/dev/null

cd "$SAVE_PWD"
rm -rf build
