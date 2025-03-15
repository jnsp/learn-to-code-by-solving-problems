from slot_machines import broke_when


def test_broke():
    quarters = 48
    slot_machine_played = (3, 10, 4)
    assert broke_when(quarters, slot_machine_played) == 66
