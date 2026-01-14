#!/usr/bin/env python3
"""
Sample Size Calculator for Clinical Trial Protocols
Based on standard statistical methods for clinical trials.
"""

import math
from typing import Optional

def calculate_sample_size_continuous(
    effect_size: float,
    std_dev: float,
    alpha: float = 0.05,
    power: float = 0.80,
    two_sided: bool = True,
    ratio: float = 1.0
) -> dict:
    """
    Calculate sample size for continuous outcomes (two-sample t-test).
    
    Args:
        effect_size: Expected difference between groups
        std_dev: Standard deviation
        alpha: Significance level (default 0.05)
        power: Statistical power (default 0.80)
        two_sided: Two-sided test (default True)
        ratio: Allocation ratio (n2/n1, default 1.0)
    
    Returns:
        Dictionary with sample sizes per group and total
    """
    from scipy import stats
    
    if two_sided:
        z_alpha = stats.norm.ppf(1 - alpha/2)
    else:
        z_alpha = stats.norm.ppf(1 - alpha)
    
    z_beta = stats.norm.ppf(power)
    
    # Sample size formula
    n1 = ((z_alpha + z_beta)**2 * std_dev**2 * (1 + 1/ratio)) / (effect_size**2)
    n2 = n1 * ratio
    
    return {
        "n_per_group_1": math.ceil(n1),
        "n_per_group_2": math.ceil(n2),
        "total_n": math.ceil(n1) + math.ceil(n2),
        "parameters": {
            "effect_size": effect_size,
            "std_dev": std_dev,
            "alpha": alpha,
            "power": power,
            "two_sided": two_sided,
            "ratio": ratio
        }
    }


def calculate_sample_size_proportion(
    p1: float,
    p2: float,
    alpha: float = 0.05,
    power: float = 0.80,
    two_sided: bool = True,
    ratio: float = 1.0
) -> dict:
    """
    Calculate sample size for binary outcomes (two-proportion z-test).
    
    Args:
        p1: Expected proportion in group 1
        p2: Expected proportion in group 2
        alpha: Significance level
        power: Statistical power
        two_sided: Two-sided test
        ratio: Allocation ratio
    
    Returns:
        Dictionary with sample sizes
    """
    from scipy import stats
    
    if two_sided:
        z_alpha = stats.norm.ppf(1 - alpha/2)
    else:
        z_alpha = stats.norm.ppf(1 - alpha)
    
    z_beta = stats.norm.ppf(power)
    
    p_pooled = (p1 + ratio * p2) / (1 + ratio)
    
    numerator = (z_alpha * math.sqrt(p_pooled * (1 - p_pooled) * (1 + 1/ratio)) +
                 z_beta * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2) / ratio))**2
    denominator = (p1 - p2)**2
    
    n1 = numerator / denominator
    n2 = n1 * ratio
    
    return {
        "n_per_group_1": math.ceil(n1),
        "n_per_group_2": math.ceil(n2),
        "total_n": math.ceil(n1) + math.ceil(n2),
        "parameters": {
            "p1": p1,
            "p2": p2,
            "alpha": alpha,
            "power": power,
            "two_sided": two_sided,
            "ratio": ratio
        }
    }


if __name__ == "__main__":
    # Example usage
    print("Sample Size Calculator for Clinical Trials")
    print("=" * 50)
    
    # Example: Continuous outcome
    result = calculate_sample_size_continuous(
        effect_size=5.0,
        std_dev=10.0,
        alpha=0.05,
        power=0.80
    )
    print(f"\nContinuous outcome example:")
    print(f"  N per group: {result['n_per_group_1']}")
    print(f"  Total N: {result['total_n']}")
    
    # Example: Binary outcome
    result = calculate_sample_size_proportion(
        p1=0.30,
        p2=0.50,
        alpha=0.05,
        power=0.80
    )
    print(f"\nBinary outcome example:")
    print(f"  N per group: {result['n_per_group_1']}")
    print(f"  Total N: {result['total_n']}")
