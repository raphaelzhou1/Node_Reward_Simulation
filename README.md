# Node_Reward_Simulation

## Author: Omar Syed, Dan Ingamells, Andrey Gorlin, Tianyu "Raphael" Zhou

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

# Simple Story:
- Assumptions:
    - Omar: User must stake more than a threshold amount to become validator
    - Omar: Validator reward paid as unit of time, not of TPS (as in Bitcoin, Ethereum1.0) / token holding (as in Algorand) / registration status (as in Cardano + Polkadot) / participation (as in NEAR, Cosmos, Solana)
    - Omar: Validator reward paid only to active nodes, not standby nodes; but standby and active nodes are all burning fixed costs
    - Omar: Validator fixed cost is linearly increasing (i.e., AWS EC2 per type increases price)
    - Omar: Validator variable cost due to TPS can be modeled
    - Omar: Shardeum Foundation (for first months of Shardeum mainnet) holds private key to adjust node reward per time and staking threshold to solve the following "problems"
    - Omar: Total SHM issued is fixed; no matter how node reward per time is adjusted, must not give inflate too much

- Problems:
    - Ok case (security): Intra-shard and inter-shard
    - Ok case (fairness): Due to staking cost + node reward adjustments to prevent bad and worst cases, some nodes will get more money than others; they must not get too much more
    - Ok case (descaling): TPS goes down -> Validators can't scale down s.t. they waste money in fixed + variable cost as standby nodes
    - Regular case (scaling): TPS goes up -> Validators not paid more due to higher TPS demand, so either more validators can join or some validators are willing to expand variable cost to process more TX, otherwise, collateral damage due to network outages like Solana
    - Bad case (robustness): Price at current time goes down -> validators have less incentive to mine and quit network -> collateral damage due to network outages like Solana -> Shardeum will lack economic incentive for people to join again
    - Worst case (robustness): Price at current time goes down while TPS goes up -> validators have no incentive to mine (higher TPS cost and lower expected payoff) and quit network 

- Our Approach:
    - We only care about the regular, bad, and worst cases for now
    - Treat APR as a stochastic process, at each time t for some omega, we 
    - Run the following algorithm:

# Model Spec:
- Monte Carlo:
Calculate a n_step x n_path ndarray s.t. at each grid, it represents the APR of the network given a certain trajectory at certain time step

Then, each APR is based on selections from other n_step x n_path ndarray of component variables that the APR is made of

Based on this, we aggregate all the APR to assess, given certain modeled parameters, how well the network has done

- APR:
$ /frac{Expected-price-payoff * Node-reward-per-time}{Variable-cost-per-TPS + Fixed-cost-per-time + Stake-for-becoming-validator} $

- Variable-cost-per-TPS: 
Can change only 30 days after last change
Same for standby nodes + active nodes
Variable due to FDAO

- Fixed-cost-per-time:
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

# Interviews
- Flavian: (1) Network for some TPS range, the necessary # of validators; (2) Bware Labs: reward full nodes (3) Blast https://houston.blastapi.io/ (4) Bare metal machine: better performance; cloud (5) Sui scaling: increase in TPS, not by increasing hardware, but entity composed by multiple machines (parallel processing) (6) Large validator companies: If bullish on Shardeum, may run based on expected price; retail: cash out quick (7) APR need 100% to cover loss if valued at 1b and goes down by 50%

- Ravi Chamria !: (1) Node cost: hourly (not accounting for S:A), choose fixed monthly cost (not accounting for S:A); Zeeve considering making node cost variable (when price low, node price low s.t. network is APR-viable) (2) Node revenue: Inflationary / deflationary impact (burn)