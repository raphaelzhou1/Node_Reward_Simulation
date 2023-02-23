import numpy as np
import pandas as pd
import plotly.express as px

from stochastic_models import Arithmetic_Brownian_Motion

if __name__ == '__main__':
    # Variables for Tests
    npaths = 50 # how many runs
    nsteps = 200 # time-steps; if assume 1 step / simulated day, then over 10 years = 3650 days
    T = 1 # scaling for the values of stochastic variables of the process
    dt = T/nsteps
    t = np.arange(0, T+dt, dt) # for expected value + variance, no other relevance
    
    # Modelled parameters: TPS
    TPS = Arithmetic_Brownian_Motion(100, 20, npaths, nsteps, t, T, 200).get_df(plot_expected=True)
    expected_price = 10

    print(TPS)