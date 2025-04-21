#!/bin/bash
set -e

file_exists() {
    mpremote ls | grep -q "$1"
}

echo "🔄 Deleting..."
if file_exists "boot.py"; then
    mpremote rm boot.py
fi

if file_exists "main.py"; then
    mpremote rm main.py
fi

if file_exists "lib"; then
    mpremote rm -r lib/
fi

echo "🧹 Triggering garbage collection..."
mpremote exec "import gc; gc.collect()"

echo "⬆️ Uploading files..."
mpremote cp boot.py :
mpremote cp main.py :
mpremote cp -r lib/ :

echo "🔁 Resetting device..."
mpremote reset

echo "✅ Done!"
mpremote ls lib/
mpremote ls
