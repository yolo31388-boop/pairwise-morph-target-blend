import pytest
import graphics.morph_target_blend as mod

CASES = [
    ("normalize_all_weights", (1,)),
    ("draw_after_upload", (1,)),
    ("guard_offset", (1,)),
    ("interpolate_weight", (1,)),
    ("map_lod_weights", (1,)),
    ("validate_export", (1,)),
    ("load", (1,)),
    ("upload", (1,)),
    ("blend", (1,)),
    ("draw", (1,)),
    ("validate_morph", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
