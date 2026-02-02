# CartPole RL — Demo & Evaluation

Interactive demos and evaluation artifacts for trained CartPole-v1 agents (PPO, DQN, A2C) using Gymnasium and Stable-Baselines3. This repo ships pre-trained model ZIPs, a menu-driven demo script, and saved evaluation results.

## Quick start (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

You can also run `demo.py` (same interface as `main.py`).

## Usage

- Live demo (rendered): select an algorithm from the menu.
- Headless comparison: choose the performance comparison option.

## Models

Expected model ZIPs (already present in this workspace):

- `models/ppo_cartpole_final.zip`
- `models/dqn_cartpole_final.zip`
- `models/a2c_cartpole_final.zip`

If you want to verify model availability:

```powershell
python check_models.py
```

## Results

Saved evaluation artifacts:

- `results/evaluation_results.json`
- `results/*_rewards.npy`
- `results/comparison.png`

## Analysis & plots (optional)

Generate plots from logs or saved results:

```powershell
python analysis_and_plots.py
```

Outputs are saved to `plots/`.

## Notes

- Python 3.8+ recommended.
- Stable-Baselines3 requires PyTorch; use the PyTorch selector if you need CUDA support.
- Large model files are best handled with Git LFS if you plan to publish them.



