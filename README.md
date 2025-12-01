# Astar EVM — Whale Suicide Tracker

Detects when a smart contract on Astar (Polkadot parachain with EVM) **self-destructs** and sends **1M+ ASTR** to the dead address (`0xdead...dead`).

This is not a burn.  
This is **digital suicide** — the contract literally deletes itself and makes funds unrecoverable.

## Run

```bash
python astar_evm_whale_suicide.py
