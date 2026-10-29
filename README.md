# Distributed Process Communication Simulator

This project models asynchronous message passing between four logical processes (P1, P2, P3, P4) using a FIFO communication queue.

## Features
- Independent process inbox management
- Asynchronous FIFO queue-based message delivery
- Full event logging (`SEND`, `DELIVER`, `REJECT`)
- Message metadata tracking (`message_id`, `sequence`, `sender`, `receiver`, `payload`)

## How to Run
Run the Python script directly using standard Python 3.7+:

```bash
python simulator.py
```
