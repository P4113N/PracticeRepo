import pandas as pd
import numpy as np
from pymc_marketing.mmm.linear_regression import MMM
from pymc_marketing.mmm import GeometricAdstock, HillSaturation


def generate_data(n: int = 100, seed: int = 0) -> pd.DataFrame:
    """Generate synthetic marketing dataset."""
    rng = np.random.default_rng(seed)
    dates = pd.date_range("2023-01-01", periods=n)
    tv = rng.gamma(5, 2, n)
    online = rng.gamma(3, 1, n)
    paper = rng.gamma(2, 1.5, n)
    sales = 100 + 0.5 * tv + 0.4 * online + 0.3 * paper + rng.normal(scale=1, size=n)
    return pd.DataFrame({
        "date": dates,
        "tv": tv,
        "online": online,
        "print": paper,
        "sales": sales,
    })


def load_model(draws: int = 20, tune: int = 20) -> MMM:
    """Fit and return a marketing mix model."""
    df = generate_data()
    model = MMM(
        date_column="date",
        channel_columns=["tv", "online", "print"],
        adstock=GeometricAdstock(l_max=3),
        saturation=HillSaturation(),
    )
    model.fit(
        df[["tv", "online", "print", "date"]],
        df["sales"],
        draws=draws,
        tune=tune,
        chains=2,
        cores=1,
        progressbar=False,
    )
    return model


def optimize_budget(model: MMM, budget: float, periods: int = 4) -> pd.Series:
    """Return optimal budget allocation per channel."""
    allocation, _ = model.optimize_budget(float(budget), num_periods=periods)
    return allocation.to_series().round(2)
