import hashlib
import os
import retro
rom_path = "roms/Mortal_Kombat_(World).md"
env = retro.make(game="MortalKombat-Genesis")

obs = env.reset()

while True:
    action = env.action_space.sample()  # Random actions
    obs, reward, done, info = env.step(action)
    env.render()
    if done:
        break

env.close()