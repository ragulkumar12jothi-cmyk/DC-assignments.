from dataclasses import dataclass
from collections import deque

@dataclass
class Message:
    message_id: int
    sender: str
    receiver: str
    payload: str
    sequence: int

class Process:
    def __init__(self, name: str):
        self.name = name
        self.inbox = []

    def receive(self, message: Message):
        self.inbox.append(message)

class CommunicationSimulator:
    def __init__(self, names: list):
        self.processes = {n: Process(n) for n in names}
        self.queue = deque()
        self.events = []
        self.next_id = 1
        self.sequence = 1

    def send(self, sender: str, receiver: str, payload: str) -> bool:
        if sender not in self.processes or receiver not in self.processes:
            self.events.append(("REJECT", sender, receiver, payload))
            return False
            
        msg = Message(
            message_id=self.next_id,
            sender=sender,
            receiver=receiver,
            payload=payload,
            sequence=self.sequence
        )
        self.next_id += 1
        self.sequence += 1
        self.queue.append(msg)
        self.events.append(("SEND", msg))
        return True

    def deliver_all(self):
        while self.queue:
            msg = self.queue.popleft()
            receiver = self.processes.get(msg.receiver)
            if receiver:
                receiver.receive(msg)
                self.events.append(("DELIVER", msg))

    def show_report(self):
        print("\n=== COMMUNICATION FLOW ===")
        for event in self.events:
            print(event)
            
        print("\n=== PROCESS INBOXES ===")
        for name, process in self.processes.items():
            inbox_summary = [(m.message_id, m.sender, m.payload) for m in process.inbox]
            print(f"{name} received: {inbox_summary}")


if __name__ == "__main__":
    # Initialize simulator with P1, P2, P3, P4
    sim = CommunicationSimulator(["P1", "P2", "P3", "P4"])

    # Example communication flow (P1 -> P2 -> P3 -> P2/P4)
    sim.send("P1", "P2", "TASK-101")
    sim.send("P2", "P3", "RESULT-101")
    sim.send("P3", "P2", "ACK-101")
    sim.send("P3", "P4", "FINAL-101")

    # Deliver all queued messages
    sim.deliver_all()

    # Print execution report and inbox logs
    sim.show_report()
