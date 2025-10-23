#M4 Projects Split Evens and Odds

from split_evens_and_odds import SplitEvensOdds

def run_demo():
    ll = SplitEvensOdds()
    ll.insert_at_end([1,2,3,4,5,6,7,8,15,14,13,12,11,10,9])
    print(ll.display())
    ev, od = ll.split_evens_and_odds()
    print(ev.display())
    print(od.display())
    print(ll.display())

if __name__ == "__main__":
    run_demo()

    
