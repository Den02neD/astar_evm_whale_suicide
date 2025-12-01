import requests, time

def astar_suicide():
    print("Astar EVM — Whale Suicide Watch (> 1M ASTR self-destruct)")
    seen = set()
    while True:
        # Astar EVM self-destruct monitoring via contract calls
        r = requests.get("https://blockscout.com/astar/api?module=account&action=txlist"
                        "&address=0x000000000000000000000000000000000000dead&sort=desc")
        for tx in r.json().get("result", [])[:40]:
            h = tx["hash"]
            if h in seen: continue
            seen.add(h)

            # selfdestruct sends funds to 0xdead...dead
            if tx["to"].lower() != "0x000000000000000000000000000000000000dead": continue
            if tx.get("contractAddress"): continue  # ignore creations

            value = int(tx["value"]) / 1e18
            if value >= 1_000_000:  # > 1 million ASTR
                print(f"WHALE COMMITTED SUICIDE\n"
                      f"{value:,.0f} ASTR sent to the void (0xdead)\n"
                      f"Contract: {tx['from']}\n"
                      f"Tx: https://blockscout.com/astar/tx/{h}\n"
                      f"→ This smart contract chose permanent death\n"
                      f"→ Funds unrecoverable forever\n"
                      f"→ Usually rage-quit or final distribution\n"
                      f"{'-'*70}")
        time.sleep(3.5)

if __name__ == "__main__":
    astar_suicide()
