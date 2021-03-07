class TShirt:
    objs_num = 0

    def __init__(self, size, message):
        self.size = size
        self.message = message

        TShirt.objs_num += 1
        print("TShirt.objs_num is now", TShirt.objs_num)


class LotteryTicket:
    objs_num = 0

    def __init__(self):
        self.golden = False
        LotteryTicket.objs_num += 1

        print("TShirt.objs_num is now", TShirt.objs_num)

        self.golden = True if LotteryTicket.objs_num % 5 == 0 else False


ticket1 = LotteryTicket()
ticket2 = LotteryTicket()
ticket3 = LotteryTicket()
ticket4 = LotteryTicket()
ticket5 = LotteryTicket()
print(ticket1.golden)
print(ticket2.golden)
print(ticket3.golden)
print(ticket4.golden)
print(ticket5.golden)