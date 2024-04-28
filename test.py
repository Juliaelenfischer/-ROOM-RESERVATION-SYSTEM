import datetime
import project

# Check room_availability funtion

def test_check_room_availabilityy(capsys):
        expected_output = "\nRoom Availability:\nRoom 101: Status: Available, Price: $199.99 per night\nRoom 102: Status: Available, Price: $120 per night\nRoom 103: Status: Not available, Price: $150 per night\n"
        project.check_room_availability()
        captured = capsys.readouterr()
        assert captured.out == expected_output

# Make_reservation function

def test_make_reservation(capsys, monkeypatch): 
        monkeypatch.setattr('builtins.input', lambda _: '101\n2025-05-01\n2025-05-03\n')
        project.make_reservation()
        captured = capsys.readouterr()
        assert "Reservation successful!" in captured.out

# Manage_reservation function
def test_manage_reservations(capsys) : 
            expected_output = "\nManage Reservations:\nRoom 101: Check-in: 2025-05-01, Check-out: 2025-05-03\n"
            project.manage_reservations()
            captured = capsys.readouterr()
            assert captured.out == expected_output

# cancel_reservation function
def test_cancel_reservation(capsys, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: '101\n')
        project.cancel_reservation()
        captured = capsys.readouterr()
        assert "Reservation canceled successfully." in captured.out

# generate_invoice function
def test_generate_invoice(capsys, monkeypatch): 
        monkeypatch.setattr('builtins.input', lambda _: '101\n')
        expected_output = "Invoice for Room 101:\nCheck-in: 2025-05-01, Check-out: 2025-05-03\nTotal nights: 2, Total price: $399.98\n"
        project.generate_invoice()
        captured = capsys.readputerr()
        assert captured.out == expected_output


