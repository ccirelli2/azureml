"""Script to test loading workplace from config file
"""
###############################################################################
# Libraries
###############################################################################
import sys
import logging
from azureml.core import Workspace
from azureml.core import Experiment
from decouple import config as d_config

logging.basicConfig(level=logging.INFO)

###############################################################################
# Paths
###############################################################################
DIR_ROOT = d_config('DIR_ROOT')
sys.path.append(DIR_ROOT)


###############################################################################
# Variables 
###############################################################################
MY_WORKSPACE = Workspace.from_config()


###############################################################################
# Code 
###############################################################################
def test_experiment(my_workspace: Workspace):
    '''Function to generate a test experiment.
    '''
    # Create an experiment
    my_experiment = Experiment(workspace=my_workspace,
                               name='my-first-experiment')
    # start the experiment
    run = my_experiment.start_logging()

    # Experiment Code
    var_1 = 1
    var_2 = 2
    var_3 = var_1 * var_2

    # Logging
    logging.info(f'Solution => {var_3}')
    run.log(name='solution', value=var_3)

    # End Experiment
    run.complete()

    # Result
    return var_3


if __name__ == '__main__':
    test_experiment(my_workspace=MY_WORKSPACE)
