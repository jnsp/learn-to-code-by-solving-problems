from take_number import dispenser


def test_take_ticket():
    taken_tickets = 0
    unsolved_tickets = 0
    next_number = 23

    expected_taken_tickets = 1
    expected_unsolved_tickets = 1
    expected_next_number = 24

    assert dispenser(taken_tickets, unsolved_tickets, next_number, "TAKE") == (
        expected_taken_tickets,
        expected_unsolved_tickets,
        expected_next_number,
    )


def test_take_ticket_end_of_cycle():
    taken_tickets = 0
    unsolved_tickets = 0
    next_number = 999

    expected_taken_tickets = 1
    expected_unsolved_tickets = 1
    expected_next_number = 1

    assert dispenser(taken_tickets, unsolved_tickets, next_number, "TAKE") == (
        expected_taken_tickets,
        expected_unsolved_tickets,
        expected_next_number,
    )


def test_serve_ticket():
    taken_tickets = 1
    unsolved_tickets = 1
    next_number = 23

    expected_taken_tickets = 1
    expected_unsolved_tickets = 0
    expected_next_number = 23

    assert dispenser(taken_tickets, unsolved_tickets, next_number, "SERVE") == (
        expected_taken_tickets,
        expected_unsolved_tickets,
        expected_next_number,
    )


def test_close():
    taken_tickets = 1
    unsolved_tickets = 1
    next_number = 23

    expected_taken_tickets = 1
    expected_unsolved_tickets = 1
    expected_next_number = 23

    assert dispenser(taken_tickets, unsolved_tickets, next_number, "CLOSE") == (
        expected_taken_tickets,
        expected_unsolved_tickets,
        expected_next_number,
    )
