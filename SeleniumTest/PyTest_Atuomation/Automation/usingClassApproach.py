import pytest

@pytest.mark.usefixtures("dataload")
class dataDriven:

    def test_data_drive_2(self):
        print("\nThis is printed from the 2nd function call of data driven approach\n")