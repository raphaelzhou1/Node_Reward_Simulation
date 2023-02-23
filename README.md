# Node_Reward_Simulation

# General (Non-Technical) Introduction:
- The Shardeum Foundation is committed to providing (1) an auto-scalable network that can support all levels of TPS for all time, (2) a secure, robust, fair, and transparent incentivization mechanism for network security providers (i.e., validators in PoS system and potential differentiated roles among them), and (3), in order for the former 2 goals, a stable, probabilistically increasing SHM price
- An auto-scalable network requires scaling and descaling
    - Scaling: When TPS increases, each TX's processing time and price should remain roughly the same as those of previous TXs
    - Descaling: When TPS decreases, each TX's processing time and price should remain roughly the same as those of previous TXs
- A secure, robust, fair, and transparent incentivization mechanism for network security providers requires security, robustness, fairness, and transparency under scaling and descaling
    - Security: For each shard and among shards, the DLT guarantees security
    - Robustness: For each node, the APR will be strong enough for times (i.e., when high TPS) when such a node is needed 
    - Fairness: Among the nodes, if under the same scenario (i.e., TX processed, network situations, price movement), no node has a higher APR for doing less work than the node that does regular work; the network is sufficiently decentralized
    - Transparency: the incentivization mechanism and its operations are fully accessible to anyone with Internet access
- A stable, probabilistically increasing SHM price requires stability and probabilistic increase
    - This is really not the point of the Node Reward Policy Design, but a result of Shardeum value creation, tokenomics, ecosystem projects, and partners. But the point is worth mentioning because, really, the tokenomics is crucial for Shardeum’s fundraising efforts and incentivization of other stakeholders (esp. Shardeum foundation and security providers).
    - Stability: SHM price should have low volatility, skew, and kurtosis.
    - Probabilistic increase: the conditional expected value of SHM later in the time series must be higher than of that earlie
- In this Shardeum Node Reward Policy Design, we address the problem above and propose a node reward policy simulation model.
    - Specifically, we are interested in achieving the properties of scaling, descaling, and robustness with our reward policy
    - For the reward policy, we are specifically interested in the SHM_threshold_stake_per_validator_node and node_reward_policy_rate parameters and the design of node reward policy in general (i.e., burn? inflation? role-based? governed by whom?)

# Model Spec:
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
