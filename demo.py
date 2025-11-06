"""
Load trained models and display live demonstrations.
No retraining needed - uses your existing saved models!
"""

import gymnasium as gym
import numpy as np
from stable_baselines3 import PPO, DQN, A2C
from pathlib import Path
import time

class CartPoleDemo:
    def __init__(self):
        self.models_dir = Path("models")
        self.algorithms = {
            "PPO": (PPO, self.models_dir / "ppo_cartpole_final.zip"),
            "DQN": (DQN, self.models_dir / "dqn_cartpole_final.zip"),
            "A2C": (A2C, self.models_dir / "a2c_cartpole_final.zip")
        }
    
    def demo_single(self, algo_name="PPO", episodes=3, slow_motion=False):
        """Show live demonstration of a specific algorithm."""
        
        if algo_name not in self.algorithms:
            print(f"❌ Algorithm {algo_name} not found!")
            return
        
        model_class, model_path = self.algorithms[algo_name]
        
        if not model_path.exists():
            print(f"❌ Model file not found: {model_path}")
            print("   Please run main.py first to train the models.")
            return
        
        # Load the saved model
        print(f"{'='*60}")
        print(f"Loading {algo_name} from {model_path}")
        model = model_class.load(model_path)
        
        # Create environment with rendering
        env = gym.make("CartPole-v1", render_mode="human")
        
        print(f"Starting {algo_name} demonstration - {episodes} episodes")
        print("Close the window to continue to next episode")
        print(f"{'='*60}")
        
        for ep in range(episodes):
            obs, _ = env.reset()
            done = False
            total_reward = 0
            steps = 0
            
            print(f"Episode {ep+1}/{episodes}: ", end="", flush=True)
            
            while not done:
                # Get action from trained model
                action, _ = model.predict(obs, deterministic=True)
                
                # Take action
                obs, reward, terminated, truncated, _ = env.step(action)
                total_reward += reward
                steps += 1
                done = terminated or truncated
                
                # Slow motion mode for better visualization
                if slow_motion:
                    time.sleep(0.02)  # 50 FPS slow motion
            
            print(f"Reward = {total_reward:.0f}, Steps = {steps}")
            
            if total_reward >= 500:
                print("   🏆 PERFECT SCORE!")
            elif total_reward >= 475:
                print("   🌟 ELITE PERFORMANCE!")
            elif total_reward >= 195:
                print("   ✅ SOLVED!")
        
        env.close()
        print(f"✅ {algo_name} demonstration complete!")
    
    def demo_all(self, episodes_per_algo=2, slow_motion=False):
        """Demo all trained algorithms."""
        print("="*60)
        print("DEMONSTRATING ALL TRAINED AGENTS")
        print("="*60)
        
        for algo_name in ["PPO", "DQN", "A2C"]:
            self.demo_single(algo_name, episodes=episodes_per_algo, slow_motion=slow_motion)
            time.sleep(1)  # Pause between algorithms
    
    def compare_side_by_side(self, test_episodes=20):
        """Run quick performance comparison without rendering."""
        print("" + "="*60)
        print("PERFORMANCE COMPARISON (NO RENDERING)")
        print("="*60)

        results = {}
        
        for algo_name, (model_class, model_path) in self.algorithms.items():
            if not model_path.exists():
                print(f"⚠️  Skipping {algo_name} - model not found")
                continue
            
            print(f"Testing {algo_name}...", end="", flush=True)
            model = model_class.load(model_path)
            env = gym.make("CartPole-v1")  # No rendering for speed
            
            rewards = []
            for _ in range(test_episodes):
                obs, _ = env.reset()
                done = False
                total_reward = 0
                
                while not done:
                    action, _ = model.predict(obs, deterministic=True)
                    obs, reward, terminated, truncated, _ = env.step(action)
                    total_reward += reward
                    done = terminated or truncated
                
                rewards.append(total_reward)
            
            env.close()
            results[algo_name] = {
                "mean": np.mean(rewards),
                "std": np.std(rewards),
                "min": np.min(rewards),
                "max": np.max(rewards),
                "perfect": sum(r >= 500 for r in rewards),
                "solved": sum(r >= 195 for r in rewards)
            }
            print(" Done!")
        
        # Display results
        print(f"Results from {test_episodes} test episodes:")
        print(f"{'Algorithm':<10} {'Mean±Std':<20} {'Min-Max':<15} {'Perfect/Solved':<15}")
        print("-"*60)
        for algo, stats in sorted(results.items()):
            mean_std = f"{stats['mean']:.1f}±{stats['std']:.1f}"
            min_max = f"{stats['min']:.0f}-{stats['max']:.0f}"
            perfect_solved = f"{stats['perfect']}/{stats['solved']}"
            print(f"{algo:<10} {mean_std:<20} {min_max:<15} {perfect_solved:<15}")
        print()

    def interactive_menu(self):
        """Interactive menu for choosing demo options."""
        while True:
            print("="*60)
            print("CARTPOLE RL DEMO - MAIN MENU")
            print("="*60)
            print("1. Demo PPO (3 episodes)")
            print("2. Demo DQN (3 episodes)")
            print("3. Demo A2C (3 episodes)")
            print("4. Demo ALL algorithms (2 episodes each)")
            print("5. Demo ALL in slow motion")
            print("6. Performance comparison (no video)")
            print("7. Exit")
            print("-"*60)
            
            choice = input("Select option (1-7): ").strip()
            
            if choice == "1":
                self.demo_single("PPO", episodes=3)
            elif choice == "2":
                self.demo_single("DQN", episodes=3)
            elif choice == "3":
                self.demo_single("A2C", episodes=3)
            elif choice == "4":
                self.demo_all(episodes_per_algo=2, slow_motion=False)
            elif choice == "5":
                self.demo_all(episodes_per_algo=1, slow_motion=True)
            elif choice == "6":
                self.compare_side_by_side(test_episodes=20)
            elif choice == "7":
                print("Goodbye! 👋")
                break
            else:
                print("❌ Invalid option. Please try again.")
            
            if choice in ["1", "2", "3", "4", "5", "6"]:
                input("Press Enter to continue...")


if __name__ == "__main__":
    demo = CartPoleDemo()
    
    # Run interactive menu
    demo.interactive_menu()
    
    # Or use these direct methods:
    # demo.demo_single("PPO", episodes=3)
    # demo.demo_single("DQN", episodes=3)
    # demo.demo_single("A2C", episodes=3)
    # demo.demo_all(episodes_per_algo=2)
    # demo.compare_side_by_side(test_episodes=50)