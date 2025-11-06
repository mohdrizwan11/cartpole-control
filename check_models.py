#!/usr/bin/env python3
"""check_models.py

Simple helper to verify expected model ZIP files are present under `models/`.
Prints instructions for next steps (download, place files, or use Git LFS).
"""

from pathlib import Path
import sys

EXPECTED = [
    Path("models/ppo_cartpole_final.zip"),
    Path("models/dqn_cartpole_final.zip"),
    Path("models/a2c_cartpole_final.zip"),
    Path("models/ppo/best_model.zip"),
    Path("models/dqn/best_model.zip"),
    Path("models/a2c/best_model.zip"),
]


def main():
    missing = [str(p) for p in EXPECTED if not p.exists()]

    if not missing:
        print("✅ All expected model files are present in `models/`.")
        print("You can run `python demo.py` or `python main.py` to demo agents.")
        return 0

    print("⚠️  Missing model files:")
    for m in missing:
        print("  -", m)

    print("\nNext steps:")
    print("  1) Place your model `.zip` files into the `models/` folder.")
    print("  2) If you prefer not to store large models in git, host them externally (Google Drive, S3) and download when needed.")
    print("  3) To include model binaries in this repo use Git LFS:\n     git lfs install && git lfs track \"*.zip\"")
    print("\nIf you want, I can enable Git LFS tracking and commit the model files for you.")
    return 1


if __name__ == "__main__":
    rc = main()
    sys.exit(rc)
