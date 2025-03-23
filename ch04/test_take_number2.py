from take_number2 import Dispenser


def test_take_ticket():
    dispenser = Dispenser(23)
    dispenser.take()

    assert dispenser.unsolved_tickets == 1
    assert dispenser.taken_tickets == 1
    assert dispenser.next_number == 24


def test_take_ticket_end_of_cycle():
    dispenser = Dispenser(999)
    dispenser.take()

    assert dispenser.unsolved_tickets == 1
    assert dispenser.taken_tickets == 1
    assert dispenser.next_number == 1


def test_serve():
    dispenser = Dispenser(23)
    dispenser.take()
    dispenser.take()

    dispenser.serve()

    assert dispenser.unsolved_tickets == 1
    assert dispenser.taken_tickets == 2
    assert dispenser.next_number == 25


def test_close():
    dispenser = Dispenser(23)
    dispenser.take()
    dispenser.take()
    dispenser.take()
    dispenser.serve()
    status = dispenser.close()

    assert status == (3, 2, 26)
    assert dispenser.unsolved_tickets == 0
    assert dispenser.taken_tickets == 0
    assert dispenser.next_number == 26
