#!/bin/bash

# Uninstall via pipx if available
if command -v pipx >/dev/null 2>&1; then
	if pipx uninstall cipherman >/dev/null 2>&1; then
		echo "Removed cipherman via pipx"
	else
		echo "cipherman not installed via pipx or pipx uninstall failed"
	fi
else
	echo "pipx not found, skipping pipx uninstall"
fi

# Uninstall via pip3 if available
if command -v pip3 >/dev/null 2>&1; then
	if pip3 uninstall -y cipherman >/dev/null 2>&1; then
		echo "Removed cipherman via pip3"
	else
		echo "pip3 uninstall failed or cipherman not installed via pip3"
	fi
else
	echo "pip3 not found, skipping pip3 uninstall"
fi

# Remove executable if present in PATH
CMD_PATH=$(command -v cipherman || true)
if [ -n "$CMD_PATH" ]; then
	echo "Removing executable at $CMD_PATH"
	rm -f "$CMD_PATH"
else
	if [ -n "$PREFIX" ] && [ -f "$PREFIX/bin/cipherman" ]; then
		echo "Removing $PREFIX/bin/cipherman"
		rm -f "$PREFIX/bin/cipherman"
	else
		echo "No cipherman executable found in PATH or PREFIX"
	fi
fi

sed -i '/eval "$(register-python-argcomplete cipherman)"/d' ~/.bashrc
echo "Uninstall complete."

