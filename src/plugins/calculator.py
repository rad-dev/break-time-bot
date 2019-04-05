from slackbot.bot import listen_to
from sympy import sympify, SympifyError


@listen_to(r'^([-+*/^%!().\d\s]+)$')
def calculate(message, formula):
    try:
        result = sympify(formula)
        answer = int(result) if result.is_Integer else float(result)
        message.send(f'{answer:,}')
    except SympifyError:
        pass
