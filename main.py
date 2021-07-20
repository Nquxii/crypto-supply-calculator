import sys

USAGE = '''
Usage: python3 main.py [options] ...

  --h    help - print this screen
  --mccs divide market cap by circ. supply resulting in price
  --prcs multiply price and circ. supply resulting in mktcap
  --mcpr divide market cap by price resulting in circ. supply

'''

opts = [opt for opt in sys.argv[1:] if opt.startswith("--")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]


# Output raw int
def output_rl(num):
    if ',' in num:
        num.strip()
        num = num.split(",")

        v = ''
        for com in range(len(num)):
            v = v + str(num[com])
        return v


# Outputs based on options
if "--h" in opts:
    print(USAGE)
    sys.exit()
elif "--mccs" in opts:
    print(int(output_rl(sys.argv[2])) / int(output_rl(sys.argv[3])))
elif "--prcs" in opts:
    print(int(output_rl(sys.argv[2])) * int(output_rl(sys.argv[3])))
elif "--mcpr" in opts:
    print(int(output_rl(sys.argv[2])) / int(output_rl(sys.argv[3])))
