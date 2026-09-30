#!/data/data/com.termux/files/usr/bin/bash
# CyberPulse installer for Android Termux (rootless)
set -e

echo "=============================================="
echo "  CyberPulse - Termux Installer"
echo "=============================================="

# Detect Termux-ish environment (optional; works on normal Linux too)
if [ -d "/data/data/com.termux" ] || [ -n "$TERMUX_VERSION" ]; then
  echo "[*] Termux environment detected."
  pkg update -y || true
  pkg install -y python git || true
else
  echo "[*] Non-Termux shell detected — ensure python3 and pip are installed."
fi

# Ensure pip
python3 -m ensurepip --upgrade 2>/dev/null || true
python3 -m pip install --upgrade pip 2>/dev/null || true

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo "[*] Installing Python dependencies..."
python3 -m pip install -r requirements.txt

echo "[*] Making cyberpulse.py executable..."
chmod +x cyberpulse.py

# Optional: install a convenience launcher in ~/.local/bin or $PREFIX/bin
BIN_DIR=""
if [ -n "$PREFIX" ] && [ -d "$PREFIX/bin" ]; then
  BIN_DIR="$PREFIX/bin"
elif [ -d "$HOME/.local/bin" ]; then
  BIN_DIR="$HOME/.local/bin"
  mkdir -p "$BIN_DIR"
elif [ -d "$HOME/bin" ]; then
  BIN_DIR="$HOME/bin"
  mkdir -p "$BIN_DIR"
fi

if [ -n "$BIN_DIR" ]; then
  LAUNCHER="$BIN_DIR/cyberpulse"
  cat > "$LAUNCHER" << EOF
#!/data/data/com.termux/files/usr/bin/bash
# Fallback shebang for non-Termux:
# !/usr/bin/env bash
cd "$SCRIPT_DIR"
exec python3 "$SCRIPT_DIR/cyberpulse.py" "\$@"
EOF
  # Fix shebang for non-Termux
  if [ -z "$TERMUX_VERSION" ] && [ ! -d "/data/data/com.termux" ]; then
    sed -i '1s|.*|#!/usr/bin/env bash|' "$LAUNCHER" 2>/dev/null || true
  fi
  chmod +x "$LAUNCHER"
  echo "[+] Launcher installed: cyberpulse"
  echo "    (If command not found, add $BIN_DIR to your PATH)"
else
  echo "[*] Could not find a bin directory for launcher."
  echo "    Run with: python3 $SCRIPT_DIR/cyberpulse.py"
fi

echo ""
echo "[+] Installation complete."
echo "    Start with:  python cyberpulse.py"
echo "            or:  cyberpulse"
echo "=============================================="
