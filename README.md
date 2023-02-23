# Node_Reward_Simulation

APR:
(Expected-price-payoff * Node-reward-per-time) / (Variable-cost-per-TPS + Fixed-cost-per-time + Stake-for-becoming-validator)

Variable-cost-per-TPS: 
Can change only 30 days after last change
Same for standby nodes + active nodes
Variable due to FDAO

Fixed-cost-per-time:
Can change only 30 days after last change
Same for standby nodes + active nodes
Variable due to time

Stake-for-becoming-validator:
Can change 1 day after last change
Same for standby nodes + active nodes
Variable due to TPS

Expected-price-payoff:
Can change 1 day after last change
Homogeneity assumption: Same for all standby nodes + active nodes
Variable due to Brownian motion / categorical choice

Node-reward-per-time:
Can change 1 day after last change
Homogeneity assumption: Same for all active nodes; 0 for standby nodes
Variable due to FDAO 
