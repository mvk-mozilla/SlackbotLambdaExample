import app



def test_answer():
    assert app.lambda_handler(None, None)
