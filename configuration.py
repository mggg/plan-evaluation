## Constants
SUPPORTED_STATES = ["Michigan", "Virginia", "Wisconsin", "Wisconsin_blocks", "Utah", "Utah_blocks", "Pennsylvania", "Missouri", "North_Carolina"]
SUPPORTED_PLAN_TYPES = ["congress", "state_senate", "state_house", "school_board"]

DUAL_GRAPH_DIR = "dual_graphs"
STATE_SPECS_DIR = "state_specifications"
CHAIN_DIR = "raw_chains"
STATS_DIR = "ensemble_stats"

SUPPORTED_METRICS = {
    "col_tally": "district_level",
    "num_cut_edges": "plan_wide",
    "num_county_pieces": "plan_wide",
    "num_split_counties": "plan_wide",
    "num_municipal_pieces": "plan_wide",
    "num_split_municipalities": "plan_wide",
    "num_traversals": "plan_wide",
    "seats": "election_level",
    "efficiency_gap": "election_level",
    "mean_median": "election_level",
    "partisan_bias": "election_level",
    "eguia_county": "election_level",
    "num_swing_districts": "plan_wide",
    "num_competitive_districts": "plan_wide",
    "num_party_districts": "plan_wide",
    "num_op_party_districts": "plan_wide",
    "num_party_wins_by_district": "plan_wide",
    "num_double_bunked": "plan_wide",
    "num_zero_bunked": "plan_wide"
}

SUPPORTED_MAP_TYPES = ["ensemble_plan", "citizen_plan", "proposed_plan"]
