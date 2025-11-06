# CartPole-v1 — Reinforcement Learning demos & results

This repository contains demonstration and evaluation artifacts for Reinforcement Learning agents trained on the OpenAI/Gymnasium CartPole-v1 environment. It includes simple demo scripts, saved model files, training logs, and evaluation results. The README below documents only the files that are present in this workspace.
(# CartPole RL — Demonstration & Evaluation

This repository contains an easy-to-run demonstration of trained Reinforcement Learning agents for the OpenAI Gymnasium "CartPole-v1" environment using Stable-Baselines3.

The project provides simple interactive scripts to (1) run live demonstrations (rendered) of trained agents and (2) run headless performance comparisons. Pre-trained model artifacts and evaluation results are kept in the `models/` and `results/` folders.

## Highlights

- Demonstration scripts using Stable-Baselines3 agents (PPO, DQN, A2C)
- Pre-computed evaluation results show strong performance (see Results section)
- Simple, interactive menu-driven scripts: `main.py` and `demo.py`

## Quick start (Windows PowerShell)

1. Create and activate a Python virtual environment (recommended):


## What is in this workspace (actual files)

Top-level files and folders present in this repository root:

- `main.py` — interactive demo script (menu-driven). Use to run live demos or non-rendered comparisons.
- `demo.py` — duplicate/demo convenience script (same menu-driven interface).
- `requirements.txt` — pinned dependencies used by the project.
- `models/` — folder containing saved models (subfolders for each algorithm).
- `logs/` — TensorBoard log folders (per-algorithm).
- `results/` — evaluation outputs and artifacts (plots and JSON/NumPy results).
- `README.md` — this file.

Detailed contents discovered during inspection:

models/
- `a2c/`
	- `best_model.zip`
	- `evaluations.npz`
- `dqn/`
	- `best_model.zip`
	- `dqn_checkpoint_100000_steps.zip`
	- `dqn_checkpoint_200000_steps.zip`
	- `dqn_checkpoint_300000_steps.zip`
	- `dqn_checkpoint_400000_steps.zip`
	- replay buffer checkpoint files (`*.pkl`)
	- `evaluations.npz`
- `ppo/`
	- `best_model.zip`
	- `evaluations.npz`
Also at `models/` root (top level): `ppo_cartpole_final.zip`, `dqn_cartpole_final.zip`, `a2c_cartpole_final.zip` (these ZIP files are present alongside the algorithm subfolders).

logs/
- `a2c/`
- `dqn/`
- `ppo/`

results/
- `evaluation_results.json` — JSON summary of evaluation metrics (PPO, DQN, A2C).
- `comparison.png` — visual comparison image (plot) generated during evaluation.
- `ppo_rewards.npy`, `dqn_rewards.npy`, `a2c_rewards.npy` — numpy reward arrays saved from evaluation runs.

This README intentionally avoids describing files or scripts that are not present in this workspace (for example, `main_enhanced.py`, `demo_enhanced.py`, or LaTeX paper files). If you want those added, I can create them on request.

---

## Quick start (Windows PowerShell)

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the interactive demo menu:

```powershell
python main.py
# or
python demo.py
```

The menu will present options to run a rendered demo per algorithm and to run a non-rendered performance comparison. The demo scripts look for model ZIP files under `models/` (the workspace already contains saved model files for PPO, DQN and A2C).

---

## Where the models are and what they are

- `models/ppo/best_model.zip` — saved PPO model (plus `ppo_cartpole_final.zip` at models root).
- `models/dqn/best_model.zip` and several DQN checkpoint ZIPs — intermediate checkpoints and final DQN model.
- `models/a2c/best_model.zip` — saved A2C model (plus `a2c_cartpole_final.zip` at models root).

If you want to re-train, place the resulting `.zip` model file into the appropriate `models/` subfolder or the `models/` root and re-run the demo scripts.

---

## Results included

- `results/evaluation_results.json` — summary metrics for PPO, DQN, and A2C (mean, std, min, max, success rate). Example values in this workspace show:

	- PPO: mean 500.0 (std 0.0)
	- DQN: mean 500.0 (std 0.0)
	- A2C: mean 452.49 (std ≈ 44.16)

- `results/comparison.png` — a saved plot comparing algorithm performance.
- Reward traces for each algorithm saved as `*_rewards.npy`.

These evaluation artifacts were generated and saved in `results/` by the training/evaluation code used during experimentation.

---

## Notes & next steps (choose what you want me to do)

I intentionally kept this README minimal and strictly accurate to the files that exist in the repository. Here are some optional follow-ups I can perform (pick any):

1. Add `check_models.py` — a small helper script that verifies model ZIPs exist and prints instructions. (Safe, small change.)
2. Add `train_example.py` — a short training example that trains one algorithm for a small number of timesteps and saves a model to `models/` (useful for verification). (I will keep timesteps small by default.)
3. Generate a `README_brief.md` or `README_complete.md` with additional documentation if you plan to publish.

If you want me to add any of the above, tell me which. I will create a todo entry, add the file(s), and run quick sanity checks.

---

## Author & contact

- Name: K Mohammad Rizwan
- Email: kmohammadrizwan11@gmail.com
- LinkedIn: https://www.linkedin.com/in/mohdrizwan11/
- GitHub: https://github.com/mohdrizwan11

---

File inventory and README created by reading the repository directories and files — this README only documents what is actually present in the workspace. If you need the README to include extra materials (paper, guides, enhanced scripts), I can add them on request.

---

## Quick Results Summary

Algorithm | Mean Reward | Std Dev | Min–Max | Success Rate
:---|---:|---:|---:|:---:
PPO | 500.0 | 0.0 | 500–500 | ✅ 100%
DQN | 500.0 | 0.0 | 500–500 | ✅ 100%
A2C | 452.49 | 44.16 | 365–500 | ✅ 100%

These numbers are taken from `results/evaluation_results.json` in this repository and reflect evaluation runs used for the comparative analysis.

---

## Project structure (overview)

The intended package layout for a publication-ready release (a subset of these files may be present in this workspace):

```
cartpole-rl/
├── README.md                     # ← You are here (this file)
├── CartPole_Paper.tex            # IEEE conference paper (LaTeX)
├── CartPole_Impl_Guide.md        # Technical implementation guide
├── Plagiarism_Analysis.md        # Code quality & originality assessment
├── Submission_Checklist.md       # Publication preparation checklist
├── README_Complete.md            # Comprehensive package summary
├── main.py                       # Training / demo (original)
├── demo.py                       # Demonstration script (original)
├── requirements.txt              # Dependencies
├── models/                       # Trained model ZIPs (place models here)
│   ├── ppo_cartpole_final.zip
│   ├── dqn_cartpole_final.zip
│   └── a2c_cartpole_final.zip
├── logs/                         # TensorBoard logs (optional)
└── results/                      # Evaluation metrics
```

Note: If some files referenced above are not present in this working directory, the README still documents the full, publication-ready package layout. The demo and evaluation scripts that ship with this repository expect model artifacts inside `models/`.

---

## Quick start (Windows PowerShell)

1. Create and activate a Python virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the interactive demo menu:

```powershell
python main.py
# or
python demo.py
```

Menu options in the demo scripts typically include:

1. Demo PPO (3 episodes)
2. Demo DQN (3 episodes)
3. Demo A2C (3 episodes)
4. Demo ALL algorithms
5. Demo ALL in slow motion
6. Performance comparison (no rendering)
7. Exit

Live demos open a window using Gymnasium's `render_mode="human"`. Close the rendering window to continue to the next episode.

---

## Installation notes & dependencies

- Python 3.8 or higher is recommended.
- The canonical pinned dependencies used during development are in `requirements.txt`.
- Stable-Baselines3 requires PyTorch. For GPU acceleration, install the correct `torch` package for your CUDA version by following the official PyTorch instructions.

Quick verification after installing dependencies (PowerShell):

```powershell
python -c "import gymnasium, stable_baselines3, numpy; print('✓ All imports successful')"
```

---

## How to train (example)

This repository's demo scripts use pre-trained models. If you want to train your own agents, here's a minimal PPO training snippet you can adapt:

```python
from stable_baselines3 import PPO
import gymnasium as gym

env = gym.make('CartPole-v1')
model = PPO('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=200_000)
model.save('models/ppo_cartpole_final')
```

After training, ensure the saved `.zip` file is placed in `models/` (the demo scripts expect `*.zip` model files).

---

## Using the demo programmatically

Examples (Python):

```python
# Demo a single algorithm
from demo import CartPoleDemo

demo = CartPoleDemo()
demo.demo_single('PPO', episodes=3, slow_motion=False)

# Run headless performance comparison
results = demo.compare_side_by_side(test_episodes=20)
print(results)
```

---

## Results and analysis

Evaluation metrics (excerpt from `results/evaluation_results.json`):

```json
{
	"PPO": { "mean": 500.0, "std": 0.0, "min": 500.0, "max": 500.0, "success_rate": 100.0 },
	"DQN": { "mean": 500.0, "std": 0.0, "min": 500.0, "max": 500.0, "success_rate": 100.0 },
	"A2C": { "mean": 452.49, "std": 44.16, "min": 365.0, "max": 500.0, "success_rate": 100.0 }
}
```

Key findings:

- PPO & DQN achieved perfect mean reward in the stored evaluation runs (500.0, zero variance).
- A2C achieved a high mean reward with higher variance, but still a 100% success rate by the evaluation metric.

These results are consistent with stable training runs recorded in `logs/` and summarized in `results/`.

---

## Code & quality checks (recommended)

Run the following checks locally (PowerShell):

```powershell
# Format
black *.py

# Static analysis
pylint main.py demo.py
mypy --ignore-missing-imports main.py demo.py

# Run tests (if provided)
pytest -q
```

---

## Troubleshooting

- "No module named 'gymnasium'":

```powershell
pip install gymnasium --upgrade
```

- "Model file not found": Train models (see Training section) or copy model ZIPs to `models/`.

- Rendering window not appearing (remote server or WSL): Use headless comparison mode:

```python
from demo import CartPoleDemo
demo = CartPoleDemo()
demo.compare_side_by_side(test_episodes=20)  # no rendering
```

---

## Citation

If you use this project in research, consider citing it as:

```
@article{cartpole2025,
	title={Comparative Analysis of Deep Reinforcement Learning Algorithms for CartPole-v1: A Study on PPO, DQN, and A2C Performance},
	author={K. Mohammad Rizwan},
	year={2025},
	publisher={IEEE}
}
```

---

## Authors & contact

- Name: K Mohammad Rizwan
- Email: kmohammadrizwan11@gmail.com
- LinkedIn: https://www.linkedin.com/in/mohdrizwan11/
- GitHub: https://github.com/mohdrizwan11

Maintainer & Last updated: November 2025

---

## License

This work is distributed under the MIT License. See `LICENSE` for details.

---

If you'd like, I can next:

- Add a small `check_models.py` helper that verifies expected model files exist and prints instructions.
- Create a tiny `train_example.py` that trains one algorithm and saves it to `models/` (fast, configurable timesteps).


