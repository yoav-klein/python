
import validate_structure


def test_get_files():
    files = validate_structure._get_files_by_regex('.\test_dir/ba.+/fo.+/ben.t', '.')
    assert(len(files) == 2)

    files = validate_structure._get_files_by_regex('tes[ert]_d.+/.+/.+/ben.t', '.')
    assert(len(files) > 1)

    