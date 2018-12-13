import SlackbotLambda



def test_answer():
    assert SlackbotLambda.lambda_handler(None, None)
