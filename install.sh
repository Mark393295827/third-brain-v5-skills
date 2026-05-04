#!/usr/bin/env bash
set -euo pipefail

REPO="Mark393295827/third-brain-v5-skills"
BRANCH="master"
SKILLS_DIR="$(dirname "$0")/skills"

echo "=== Third Brain V5 Skills Installer ==="
echo ""

# Detect agent harness
HARNESS=""
if [ -n "$CLAUDE_CODE" ] || [ -d "$HOME/.claude" ]; then
    HARNESS="claude-code"
elif command -v codex &>/dev/null; then
    HARNESS="codex"
elif command -v gemini &>/dev/null; then
    HARNESS="gemini"
fi

# Determine install target
case "$HARNESS" in
    claude-code)
        TARGET="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
        echo "Detected: Claude Code"
        ;;
    codex)
        TARGET="$HOME/.agents/skills"
        echo "Detected: Codex CLI"
        ;;
    gemini)
        TARGET="$HOME/.gemini/skills"
        echo "Detected: Gemini CLI"
        ;;
    *)
        echo "No supported agent harness detected."
        echo "Installing to ~/.claude/skills/ by default..."
        TARGET="$HOME/.claude/skills"
        ;;
esac

# Install
mkdir -p "$TARGET"
echo "Installing to: $TARGET"
cp -r "$SKILLS_DIR"/* "$TARGET/"
echo ""
echo "✅ Installed $(ls -d "$SKILLS_DIR"/*/ | wc -l) skills"
echo ""
echo "Available skills:"
for skill in "$SKILLS_DIR"/*/; do
    name=$(basename "$skill")
    desc=$(head -5 "$skill/SKILL.md" 2>/dev/null | grep "^description:" | sed 's/^description: //')
    echo "  - $name${desc:+: $desc}"
done
