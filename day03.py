input_ = open("data/day3.txt", "r").read()


def parse_(x):
    """The input string should be in the format X,Y if valid, where X and Y are 1 to 3 digit integers"""
    if " " in x or "," not in x:
        raise

    comma_ix = x.find(",")
    num1 = int(x[:comma_ix])
    num2 = int(x[comma_ix + 1 :])
    assert num1 < 1000
    assert num2 < 1000

    return num1 * num2


start_ix = 0
vals = []
while start_ix > -1:
    start_ix = input_.find("mul(", start_ix + 1)
    end_ix = input_.find(")", start_ix)

    try:
        vals.append(parse_(input_[start_ix + 4 : end_ix]))
    except:
        pass


print("pt1", sum(vals))
