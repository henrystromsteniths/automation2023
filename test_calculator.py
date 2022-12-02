import calculator

def test_add():
    #result = calculator.calculate.henryadd(10, 15)
    #assert result == 25
    assert calculator.calculate.henryadd(10,15) == 25

def test_sub():
    #result = calculator.calculate.henrysub(10, 15)
    #assert result == -5
    assert calculator.calculate.henrysub(25,15) == 10
    assert calculator.calculate.henrysub(-20,-15) == -5

def test_mult():
    #result = calculator.calculate.henrymult(10, 15)
    assert calculator.calculate.henrymult(10, 15) == 150

def test_div():
    #result = calculator.calculate.henrydiv(30, 15)
    assert calculator.calculate.henrydiv(30, 15) == 2

def test_omkretskvadrat():
    #result = calculator.calculate.henryomkretskvadrat(20, 15)
    assert calculator.calculate.henryomkretskvadrat(20, 15) == 70

def test_omkretscirkel():
    #result = calculator.calculate.henryomkretscirkel(1)
    assert calculator.calculate.henryomkretscirkel(1) == 6.28
