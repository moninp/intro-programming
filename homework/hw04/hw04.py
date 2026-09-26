"""
Homework 4: Numerical Computing with NumPy

This homework focuses on NumPy fundamentals, vectorization, and numerical
integration with applications to epidemic modeling.

Instructions:
- Complete all functions according to their docstrings
- Do not modify function signatures
- Use NumPy operations instead of loops wherever possible
- Test your code as you go
- Submit this file with your solutions

Author: [Your Name]
Date: [Date]
"""

import numpy as np
from typing import Tuple, Optional


# =============================================================================
# Problem 1: Array Fundamentals (15 points)
# =============================================================================

def array_statistics(arr: np.ndarray) -> dict:
    """
    Compute comprehensive statistics for a NumPy array.
    
    Calculate and return a dictionary containing:
    - 'mean': arithmetic mean
    - 'median': median value
    - 'std': standard deviation
    - 'min': minimum value
    - 'max': maximum value
    - 'q25': 25th percentile
    - 'q75': 75th percentile
    - 'iqr': interquartile range (Q75 - Q25)
    
    Parameters
    ----------
    arr : np.ndarray
        Input array of numerical values
    
    Returns
    -------
    dict
        Dictionary with statistical summaries
    
    Examples
    --------
    >>> arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    >>> stats = array_statistics(arr)
    >>> stats['mean']
    5.5
    >>> stats['iqr']
    4.5
    """
    pass


def normalize_array(arr: np.ndarray, method: str = 'zscore') -> np.ndarray:
    """
    Normalize an array using specified method.
    
    Supported methods:
    - 'zscore': (x - mean) / std (standardization)
    - 'minmax': (x - min) / (max - min) (scales to [0, 1])
    - 'robust': (x - median) / IQR (robust to outliers)
    
    Parameters
    ----------
    arr : np.ndarray
        Input array to normalize
    method : str, default='zscore'
        Normalization method
    
    Returns
    -------
    np.ndarray
        Normalized array
    
    Examples
    --------
    >>> arr = np.array([1, 2, 3, 4, 5])
    >>> normalized = normalize_array(arr, method='minmax')
    >>> normalized[0]  # Should be 0
    0.0
    >>> normalized[-1]  # Should be 1
    1.0
    """
    pass


# =============================================================================
# Problem 2: Indexing and Boolean Masking (15 points)
# =============================================================================

def filter_outliers(arr: np.ndarray, n_std: float = 2.0) -> np.ndarray:
    """
    Remove outliers from an array using the z-score method.
    
    An outlier is defined as a value whose z-score exceeds n_std
    standard deviations from the mean.
    
    Parameters
    ----------
    arr : np.ndarray
        Input array
    n_std : float, default=2.0
        Number of standard deviations for outlier threshold
    
    Returns
    -------
    np.ndarray
        Array with outliers removed
    
    Examples
    --------
    >>> arr = np.array([1, 2, 3, 4, 5, 100])  # 100 is outlier
    >>> filtered = filter_outliers(arr, n_std=2.0)
    >>> 100 in filtered
    False
    """
    pass


def classify_by_percentile(arr: np.ndarray) -> np.ndarray:
    """
    Classify each value into quartile groups (1, 2, 3, or 4).
    
    Values are classified based on which quartile they fall into:
    - 1: Below 25th percentile
    - 2: Between 25th and 50th percentile
    - 3: Between 50th and 75th percentile
    - 4: Above 75th percentile
    
    Parameters
    ----------
    arr : np.ndarray
        Input array of numerical values
    
    Returns
    -------
    np.ndarray
        Array of same shape with quartile labels (1, 2, 3, 4)
    
    Examples
    --------
    >>> arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    >>> groups = classify_by_percentile(arr)
    >>> groups[0]  # First element in lowest quartile
    1
    """
    pass


# =============================================================================
# Problem 3: Broadcasting and Vectorization (15 points)
# =============================================================================

def pairwise_distances(points: np.ndarray) -> np.ndarray:
    """
    Compute Euclidean distances between all pairs of points.
    
    Use broadcasting to efficiently compute the distance matrix without loops.
    For n points, returns an n×n matrix where element (i,j) is the distance
    between point i and point j.
    
    Parameters
    ----------
    points : np.ndarray
        Array of shape (n, d) where n is number of points and d is dimensions
    
    Returns
    -------
    np.ndarray
        Distance matrix of shape (n, n)
    
    Examples
    --------
    >>> points = np.array([[0, 0], [3, 4], [1, 0]])
    >>> distances = pairwise_distances(points)
    >>> distances[0, 1]  # Distance from point 0 to point 1
    5.0
    
    Hint
    ----
    Use broadcasting: (n, 1, d) - (1, n, d) → (n, n, d)
    Then compute norm along last axis
    """
    pass


def apply_polynomial(x: np.ndarray, coefficients: np.ndarray) -> np.ndarray:
    """
    Evaluate polynomial with given coefficients at each point in x.
    
    For coefficients [a₀, a₁, a₂, ..., aₙ], computes:
    p(x) = a₀ + a₁*x + a₂*x² + ... + aₙ*xⁿ
    
    Use vectorized operations and broadcasting, not loops.
    
    Parameters
    ----------
    x : np.ndarray
        Points at which to evaluate polynomial
    coefficients : np.ndarray
        Polynomial coefficients [a₀, a₁, a₂, ..., aₙ]
    
    Returns
    -------
    np.ndarray
        Polynomial values at each point in x
    
    Examples
    --------
    >>> x = np.array([0, 1, 2])
    >>> coeffs = np.array([1, 2, 3])  # p(x) = 1 + 2x + 3x²
    >>> result = apply_polynomial(x, coeffs)
    >>> result[1]  # p(1) = 1 + 2(1) + 3(1²) = 6
    6.0
    
    Hint
    ----
    Create powers of x: x⁰, x¹, x², ... then multiply by coefficients
    """
    pass


# =============================================================================
# Problem 4: Aggregations and Linear Algebra (15 points)
# =============================================================================

def correlation_matrix(data: np.ndarray) -> np.ndarray:
    """
    Compute the correlation matrix for the columns of data.
    
    The correlation between variables X and Y is:
    corr(X, Y) = cov(X, Y) / (std(X) * std(Y))
    
    Parameters
    ----------
    data : np.ndarray
        Data matrix of shape (n_samples, n_features)
    
    Returns
    -------
    np.ndarray
        Correlation matrix of shape (n_features, n_features)
    
    Examples
    --------
    >>> data = np.array([[1, 2], [2, 4], [3, 6]])
    >>> corr = correlation_matrix(data)
    >>> np.allclose(corr[0, 1], 1.0)  # Perfect correlation
    True
    
    Hint
    ----
    1. Center the data (subtract means)
    2. Compute covariance matrix using matrix multiplication
    3. Divide by standard deviations (use broadcasting)
    """
    pass


def matrix_power_method(A: np.ndarray, num_iterations: int = 100) -> Tuple[float, np.ndarray]:
    """
    Find the dominant eigenvalue and eigenvector using the power method.
    
    The power method iteratively multiplies a random vector by the matrix,
    converging to the eigenvector with largest eigenvalue.
    
    Parameters
    ----------
    A : np.ndarray
        Square matrix
    num_iterations : int, default=100
        Number of iterations
    
    Returns
    -------
    eigenvalue : float
        Dominant eigenvalue (largest in absolute value)
    eigenvector : np.ndarray
        Corresponding normalized eigenvector
    
    Algorithm
    ---------
    1. Start with random vector v
    2. Repeat:
       - v = A @ v
       - v = v / ||v||  (normalize)
    3. Eigenvalue ≈ v^T @ A @ v
    
    Examples
    --------
    >>> A = np.array([[2, 1], [1, 2]])
    >>> eigenval, eigenvec = matrix_power_method(A)
    >>> eigenval  # Should be approximately 3
    3.0
    """
    pass


# =============================================================================
# Problem 5: Numerical Integration - Euler's Method (20 points)
# =============================================================================

def euler_step(f, t: float, y: float, dt: float, *args) -> float:
    """
    Perform one step of Euler's method for solving dy/dt = f(t, y).
    
    Euler's method approximates:
    y(t + dt) ≈ y(t) + f(t, y(t)) * dt
    
    Parameters
    ----------
    f : callable
        Derivative function f(t, y, *args) that returns dy/dt
    t : float
        Current time
    y : float
        Current value
    dt : float
        Time step
    *args
        Additional arguments to pass to f
    
    Returns
    -------
    float
        Approximation of y(t + dt)
    
    Examples
    --------
    >>> def exponential_growth(t, y, k): return k * y
    >>> y_next = euler_step(exponential_growth, 0, 1, 0.1, 0.5)
    >>> y_next  # ≈ 1 + 0.5 * 1 * 0.1 = 1.05
    1.05
    """
    pass


def solve_ode_euler(f, y0: float, t_span: Tuple[float, float], 
                    dt: float, args: tuple = ()) -> Tuple[np.ndarray, np.ndarray]:
    """
    Solve ODE dy/dt = f(t, y) using Euler's method.
    
    Parameters
    ----------
    f : callable
        Derivative function f(t, y, *args)
    y0 : float
        Initial condition y(t0)
    t_span : tuple
        Time interval (t_start, t_end)
    dt : float
        Time step size
    args : tuple, default=()
        Additional arguments for f
    
    Returns
    -------
    t : np.ndarray
        Array of time points
    y : np.ndarray
        Array of solution values
    
    Examples
    --------
    >>> def exp_growth(t, y, k): return k * y
    >>> t, y = solve_ode_euler(exp_growth, 1.0, (0, 1), 0.1, args=(0.5,))
    >>> len(t)
    10
    """
    pass


# =============================================================================
# Problem 6: SIR Epidemic Model (20 points)
# =============================================================================

def sir_derivatives(t: float, state: np.ndarray, beta: float, 
                   gamma: float, N: float) -> np.ndarray:
    """
    Compute derivatives for the SIR epidemic model.
    
    The SIR model describes disease spread using three compartments:
    - S: Susceptible individuals
    - I: Infectious individuals  
    - R: Recovered individuals
    
    The model equations are:
    dS/dt = -β*S*I/N
    dI/dt = β*S*I/N - γ*I
    dR/dt = γ*I
    
    Parameters
    ----------
    t : float
        Time (not used but required for ODE solver interface)
    state : np.ndarray
        Current state [S, I, R]
    beta : float
        Transmission rate (contacts per day × probability per contact)
    gamma : float
        Recovery rate (1 / infectious period in days)
    N : float
        Total population
    
    Returns
    -------
    np.ndarray
        Derivatives [dS/dt, dI/dt, dR/dt]
    
    Examples
    --------
    >>> state = np.array([990, 10, 0])
    >>> derivs = sir_derivatives(0, state, beta=0.5, gamma=0.1, N=1000)
    >>> derivs[1] > 0  # Infections should be increasing initially
    True
    """
    pass


def simulate_sir(S0: float, I0: float, R0: float, beta: float, 
                gamma: float, t_max: float, dt: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Simulate the SIR epidemic model using Euler's method.
    
    Parameters
    ----------
    S0, I0, R0 : float
        Initial number of susceptible, infectious, and recovered individuals
    beta : float
        Transmission rate
    gamma : float
        Recovery rate
    t_max : float
        Maximum simulation time (days)
    dt : float
        Time step size (days)
    
    Returns
    -------
    t : np.ndarray
        Time points
    S : np.ndarray
        Susceptible population over time
    I : np.ndarray
        Infectious population over time
    R : np.ndarray
        Recovered population over time
    
    Examples
    --------
    >>> t, S, I, R = simulate_sir(990, 10, 0, 0.5, 0.1, 100, 1)
    >>> S[0]  # Initial susceptible
    990.0
    >>> I.max() > I[0]  # Peak infections exceed initial
    True
    """
    pass


def analyze_sir_outbreak(S0: float, I0: float, R0: float, beta: float, 
                        gamma: float, t_max: float, dt: float) -> dict:
    """
    Simulate SIR model and compute key epidemic metrics.
    
    Compute and return:
    - 'R0': Basic reproduction number (beta / gamma)
    - 'peak_time': Day when infections peak
    - 'peak_infections': Maximum number of simultaneous infections
    - 'attack_rate': Percentage of population eventually infected (R_final/N)
    - 'final_size': Total number infected by end (R_final)
    
    Parameters
    ----------
    S0, I0, R0 : float
        Initial populations
    beta : float
        Transmission rate
    gamma : float
        Recovery rate
    t_max : float
        Simulation time (days)
    dt : float
        Time step (days)
    
    Returns
    -------
    dict
        Dictionary with epidemic metrics
    
    Examples
    --------
    >>> metrics = analyze_sir_outbreak(990, 10, 0, 0.5, 0.1, 160, 1)
    >>> metrics['R0']
    5.0
    >>> metrics['attack_rate'] > 50  # More than 50% infected
    True
    """
    pass


# =============================================================================
# Problem 7: Advanced SIR - Intervention Analysis (Bonus: +10 points)
# =============================================================================

def sir_with_intervention(S0: float, I0: float, R0: float, 
                         beta_before: float, beta_after: float,
                         gamma: float, intervention_day: int,
                         t_max: float, dt: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Simulate SIR model with intervention that reduces transmission.
    
    Models a public health intervention (e.g., social distancing, mask mandate)
    implemented on a specific day that reduces the transmission rate.
    
    Parameters
    ----------
    S0, I0, R0 : float
        Initial populations
    beta_before : float
        Transmission rate before intervention
    beta_after : float
        Transmission rate after intervention (should be < beta_before)
    gamma : float
        Recovery rate (unchanged by intervention)
    intervention_day : int
        Day when intervention is implemented
    t_max : float
        Total simulation time (days)
    dt : float
        Time step (days)
    
    Returns
    -------
    t, S, I, R : np.ndarray
        Time points and populations over time
    
    Examples
    --------
    >>> t, S, I, R = sir_with_intervention(990, 10, 0, 0.5, 0.25, 
    ...                                     0.1, 30, 160, 1)
    >>> # Peak should be lower than without intervention
    
    Hint
    ----
    Modify your simulate_sir function to use different beta values
    before and after intervention_day
    """
    pass


def compare_interventions(S0: float, I0: float, R0: float, beta: float,
                         gamma: float, reduction_percentages: list,
                         intervention_day: int, t_max: float, 
                         dt: float) -> dict:
    """
    Compare effectiveness of different intervention strengths.
    
    Simulates epidemics with different levels of transmission reduction
    and returns key metrics for comparison.
    
    Parameters
    ----------
    S0, I0, R0 : float
        Initial populations
    beta : float
        Baseline transmission rate (before intervention)
    gamma : float
        Recovery rate
    reduction_percentages : list
        List of reduction levels (e.g., [0, 25, 50, 75] for 0%, 25%, etc.)
    intervention_day : int
        Day when intervention starts
    t_max : float
        Simulation time
    dt : float
        Time step
    
    Returns
    -------
    dict
        Dictionary mapping reduction percentage to epidemic metrics:
        {reduction_pct: {'peak_infections': float, 'attack_rate': float, ...}}
    
    Examples
    --------
    >>> results = compare_interventions(990, 10, 0, 0.5, 0.1, 
    ...                                [0, 50], 30, 160, 1)
    >>> results[50]['peak_infections'] < results[0]['peak_infections']
    True
    """
    pass


# =============================================================================
# Testing Code (DO NOT MODIFY)
# =============================================================================

def test_homework():
    """Test all homework functions with basic examples."""
    
    print("Testing Problem 1: Array Fundamentals")
    print("-" * 50)
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    try:
        stats = array_statistics(arr)
        print(f"✓ array_statistics: mean = {stats['mean']}")
    except:
        print("✗ array_statistics not implemented")
    
    try:
        normalized = normalize_array(arr, 'minmax')
        print(f"✓ normalize_array: min = {normalized.min()}, max = {normalized.max()}")
    except:
        print("✗ normalize_array not implemented")
    
    print("\nTesting Problem 2: Indexing and Boolean Masking")
    print("-" * 50)
    arr_outliers = np.array([1, 2, 3, 4, 5, 100])
    try:
        filtered = filter_outliers(arr_outliers)
        print(f"✓ filter_outliers: removed {len(arr_outliers) - len(filtered)} outliers")
    except:
        print("✗ filter_outliers not implemented")
    
    try:
        groups = classify_by_percentile(arr)
        print(f"✓ classify_by_percentile: groups = {np.unique(groups)}")
    except:
        print("✗ classify_by_percentile not implemented")
    
    print("\nTesting Problem 3: Broadcasting and Vectorization")
    print("-" * 50)
    points = np.array([[0, 0], [3, 4], [1, 0]])
    try:
        distances = pairwise_distances(points)
        print(f"✓ pairwise_distances: distance[0,1] = {distances[0, 1]:.2f}")
    except:
        print("✗ pairwise_distances not implemented")
    
    try:
        poly_result = apply_polynomial(np.array([0, 1, 2]), np.array([1, 2, 3]))
        print(f"✓ apply_polynomial: p(1) = {poly_result[1]}")
    except:
        print("✗ apply_polynomial not implemented")
    
    print("\nTesting Problem 4: Aggregations and Linear Algebra")
    print("-" * 50)
    data = np.array([[1, 2], [2, 4], [3, 6]])
    try:
        corr = correlation_matrix(data)
        print(f"✓ correlation_matrix: shape = {corr.shape}")
    except:
        print("✗ correlation_matrix not implemented")
    
    try:
        A = np.array([[2, 1], [1, 2]])
        eigenval, _ = matrix_power_method(A, 100)
        print(f"✓ matrix_power_method: dominant eigenvalue = {eigenval:.2f}")
    except:
        print("✗ matrix_power_method not implemented")
    
    print("\nTesting Problem 5: Numerical Integration")
    print("-" * 50)
    def exp_growth(t, y, k): return k * y
    try:
        y_next = euler_step(exp_growth, 0, 1, 0.1, 0.5)
        print(f"✓ euler_step: y_next = {y_next}")
    except:
        print("✗ euler_step not implemented")
    
    try:
        t, y = solve_ode_euler(exp_growth, 1.0, (0, 1), 0.1, args=(0.5,))
        print(f"✓ solve_ode_euler: computed {len(t)} time points")
    except:
        print("✗ solve_ode_euler not implemented")
    
    print("\nTesting Problem 6: SIR Model")
    print("-" * 50)
    try:
        state = np.array([990, 10, 0])
        derivs = sir_derivatives(0, state, 0.5, 0.1, 1000)
        print(f"✓ sir_derivatives: dI/dt = {derivs[1]:.2f}")
    except:
        print("✗ sir_derivatives not implemented")
    
    try:
        t, S, I, R = simulate_sir(990, 10, 0, 0.5, 0.1, 100, 1)
        print(f"✓ simulate_sir: peak infections = {I.max():.0f}")
    except:
        print("✗ simulate_sir not implemented")
    
    try:
        metrics = analyze_sir_outbreak(990, 10, 0, 0.5, 0.1, 160, 1)
        print(f"✓ analyze_sir_outbreak: R0 = {metrics['R0']}, attack rate = {metrics['attack_rate']:.1f}%")
    except:
        print("✗ analyze_sir_outbreak not implemented")
    
    print("\nTesting Problem 7: Interventions (Bonus)")
    print("-" * 50)
    try:
        t, S, I, R = sir_with_intervention(990, 10, 0, 0.5, 0.25, 0.1, 30, 160, 1)
        print(f"✓ sir_with_intervention: peak after intervention = {I[30:].max():.0f}")
    except:
        print("✗ sir_with_intervention not implemented")
    
    try:
        results = compare_interventions(990, 10, 0, 0.5, 0.1, [0, 50], 30, 160, 1)
        print(f"✓ compare_interventions: compared {len(results)} scenarios")
    except:
        print("✗ compare_interventions not implemented")


if __name__ == "__main__":
    test_homework()
