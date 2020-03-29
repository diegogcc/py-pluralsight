"""
A dummy is used when you're forced to pass an argument to the function under test,
but that collaborator isn't used in the scenario.
"""


def fizzbuzz_dummy(n, additional_rules):
    """
    Convert a number to it's name in the game FizzBuzz
    >>> fizzbuzz_dummy(2, None)
    '2'
    >>> fizzbuzz_dummy(3, None)
    'Fizz'
    >>> fizzbuzz_dummy(5, None)
    'Buzz'
    >>> fizzbuzz_dummy(15, None)
    'FizzBuzz'
    >>> fizzbuzz_dummy(7,{7:"Whizz"})
    'Whizz'
    >>> fizzbuzz_dummy(35, {7:"Whizz"})
    'BuzzWhizz'
    """
    answer = ""
    rules = {3: "Fizz", 5: "Buzz"}
    if additional_rules:
        rules.update(additional_rules)
    for divisor in sorted(rules.keys()):
        if n % divisor == 0:
            answer += rules[divisor]
    if not answer:
            answer = str(n)
    return answer

def fizzbuzz_no_dummy(n, additional_rules=None):
    """
    Convert a number to it's name in the game FizzBuzz
    >>> fizzbuzz_no_dummy(2)
    '2'
    >>> fizzbuzz_no_dummy(3)
    'Fizz'
    >>> fizzbuzz_no_dummy(5)
    'Buzz'
    >>> fizzbuzz_no_dummy(15)
    'FizzBuzz'
    >>> fizzbuzz_no_dummy(7,{7:"Whizz"})
    'Whizz'
    >>> fizzbuzz_no_dummy(35, {7:"Whizz"})
    'BuzzWhizz'
    """
    answer = ""
    rules = {3: "Fizz", 5: "Buzz"}
    if additional_rules:
        rules.update(additional_rules)
    for divisor in sorted(rules.keys()):
        if n % divisor == 0:
            answer += rules[divisor]
    if not answer:
            answer = str(n)
    return answer