from .moves import *
from .cards import *
from caravanassets import get_args

def main():
    args = get_args()
    try:
        if len(args.caravan) == 0:
            print("it's empty...")
            return
        if len(args.caravan) % 2 == 1:
            print("should be an even number of arguments")
            return
        for i in range(len(args.caravan)):
            if type(args.caravan[i]) != int:
                print("only ints allowed")
                return
            elif i % 2 == 0:
                if args.caravan[i] < 1 or args.caravan[i] > 13:
                    print("enter card in range (1-13)")
                    return
                if args.caravan[i] == 11:
                    print("jacks cannot be used")
                    return
            elif i % 2 == 1:
                if args.caravan[i] < 1 or args.caravan[i] > 4:
                    print("enter suit in range (1-4)")
                    return
        if args.caravan[0] > 10:
            print("only numbers at first card")
            return
    except:
        print("invalid type... i think so...")
        return

    try:
        if args.addjack > len(args.caravan) // 2 or args.addjack < 1:
            print("invalid range, should be at 1-(len(caravan) // 2)")
        elif args.caravan[args.addjack * 2 - 2] > 10:
            print("can put jack only on a number")
        else:
            newjack = Card(10, 0)
            Caravan = []
            for i in range(0, len(args.caravan) - 1, 2):
                Caravan.append(Card(args.caravan[i] - 1, args.caravan[i + 1] - 1))
            Caravan = add_card(Caravan, newjack, args.addjack - 1)
            for card in Caravan:
                print(card.name, card.suit)

    except:
        print("unknown error")



if __name__ == "__main__":
    main()