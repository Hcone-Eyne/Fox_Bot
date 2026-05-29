# import required library
import torch

# check if mps is available
if torch.backends.mps.is_available():
    print("All Good 🦇")
else:
    print("Attention Needed!")