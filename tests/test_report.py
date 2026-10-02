"""Locks for the printed graph proxy. Not a 92% measurement."""
from localization import (
    HISTORICAL_ETA,
    corner_residual,
    locks_hold,
    main,
    report_rows,
    residual_supported_only_on_corners,
)


def test_default_report_locks_and_misses_92():
    rows = report_rows()
    assert locks_hold(rows)
    assert HISTORICAL_ETA == 0.92
    for row in rows:
        assert row["historical_92"] == [False, False, False]
        assert abs(abs(row["eta"][0] - 0.92) - 0.42) < 1e-12
        assert row["support_corners_only"] is True
        assert residual_supported_only_on_corners(row["level"]) is True


def test_level0_residual_and_three_fifths_scale():
    r0 = corner_residual(0)
    assert abs(r0[0] - 2.5) < 1e-12
    assert abs(r0[1] - (-2.0)) < 1e-12
    assert abs(r0[2] - (-0.5)) < 1e-12
    for level in range(1, 6):
        got = corner_residual(level)
        factor = (3.0 / 5.0) ** level
        assert abs(got[0] - 2.5 * factor) < 1e-9
        assert abs(got[1] - (-2.0) * factor) < 1e-9
        assert abs(got[2] - (-0.5) * factor) < 1e-9


def test_main_prints_the_miss_and_exits_clean(capsys):
    main()
    out = capsys.readouterr().out
    assert "0.500000  0.400000  0.100000" in out
    assert "short of 0.92 by 0.420000" in out
    assert "historical_92_reproduced is false" in out
    assert "thrust_validated = false" in out
    assert "Not a Maxwell-stress integral" in out
    assert "0.08" in out
