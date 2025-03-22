import pytest
from slot_machines import broke_when, which_machine


@pytest.mark.parametrize(
    "n_spins, slotmachine", [(1, "a"), (2, "b"), (3, "c"), (4, "a"), (5, "b"), (6, "c"), (7, "a"), (8, "b"), (9, "c")]
)
def test_which_machine(n_spins, slotmachine):
    assert which_machine(n_spins) == slotmachine


def test_broke():
    quarters = 48
    slot_machine_played = (3, 10, 4)
    assert broke_when(quarters, slot_machine_played) == 66
