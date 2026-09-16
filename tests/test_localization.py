from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from localization import corner_voronoi_eta


def test_eta_is_a_fraction_and_not_the_historical_92():
    r = corner_voronoi_eta(3, region_corner=0)
    assert 0.0 <= r.eta <= 1.0
    assert r.n_region > 0
    assert r.historical_92_reproduced is False


def test_region_defined_before_value():
    r = corner_voronoi_eta(2, region_corner=0)
    assert "voronoi" in r.region_definition
