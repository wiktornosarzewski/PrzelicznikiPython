def mbps_to_mbs(mbps: float) -> float:
    return mbps / 8

def mbs_to_mbps(mbs: float) -> float:
    return mbs * 8

once = False
while True:
    if once: 
        user_input = input("Wpisz r, aby wykonać ponownie: ")
    else:
        user_input = "r"
    if user_input == "r":
        while True:
            inp = int(input("Wprowadz predkosc: "))
            mbps = inp
            mbs = mbps_to_mbs(mbps)
            print(f"{mbps} Mbps to {mbs} MB/s")
            mbps = mbs_to_mbps(inp)
            print(f"{inp} MB/s to {mbps} Mbps")
            once = True
            break
            
            continue
    else:
        break
