"""Script to test loading workplace from config file
"""
from azureml.core import Workspace


# Get Workspace
MY_WORKSPACE = Workspace.from_config()

# Get list of compute targets
for compute_name in MY_WORKSPACE.compute_targets:
    compute = MY_WORKSPACE.compute_targets[compute_name]
    print(compute.name, ":", compute.type)


