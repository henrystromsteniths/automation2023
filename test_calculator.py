import calculator

def test_add():
    result = calculator.calculate.henryadd(10, 15)
    assert result == 25

def test_sub():
    result = calculator.calculate.henrysub(10, 15)
    assert result == -5

def test_mult():
    result = calculator.calculate.henrymult(10, 15)
    assert result == 150

def test_div():
    result = calculator.calculate.henrydiv(30, 15)
    assert result == 2

def test_omkrets():
    result = calculator.calculate.henryomkrets(20, 15)
    assert result == 70


