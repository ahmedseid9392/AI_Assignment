import tkinter as tk
import random

# -----------------------------
# Environment
# -----------------------------
class RoomEnvironment:
    def __init__(self, temperature=24):
        self.temperature = temperature

    def update(self, ac_state):
        if ac_state == "ON":
            self.temperature -= 0.8
        else:
            self.temperature += 0.4

        # small fluctuation
        self.temperature += random.uniform(-0.2, 0.2)


# -----------------------------
# Simple Reflex Agent
# -----------------------------
class ThermostatAgent:
    def __init__(self):
        self.ac_state = "OFF"

    def decide(self, temperature):

        if temperature > 25:
            self.ac_state = "ON"

        elif temperature <= 22:
            self.ac_state = "OFF"

        return self.ac_state


# -----------------------------
# GUI Application
# -----------------------------
class ThermostatGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("AI Thermostat Controller")
        self.root.geometry("420x350")
        self.root.configure(bg="#1e1e2f")

        self.env = RoomEnvironment()
        self.agent = ThermostatAgent()

        # Title
        title = tk.Label(
            root,
            text="AI Thermostat Controller",
            font=("Segoe UI", 20, "bold"),
            bg="#1e1e2f",
            fg="white"
        )
        title.pack(pady=15)

        # Temperature label
        self.temp_label = tk.Label(
            root,
            text="Temperature: -- °C",
            font=("Segoe UI", 16),
            bg="#1e1e2f",
            fg="#00d9ff"
        )
        self.temp_label.pack(pady=10)

        # AC state label
        self.ac_label = tk.Label(
            root,
            text="AC State: OFF",
            font=("Segoe UI", 16, "bold"),
            bg="#1e1e2f",
            fg="#ff6b6b"
        )
        self.ac_label.pack(pady=10)

        # Status label
        self.status_label = tk.Label(
            root,
            text="System Ready",
            font=("Segoe UI", 12),
            bg="#1e1e2f",
            fg="white"
        )
        self.status_label.pack(pady=10)

        # Button Frame
        btn_frame = tk.Frame(root, bg="#1e1e2f")
        btn_frame.pack(pady=15)

        start_btn = tk.Button(
            btn_frame,
            text="Start",
            width=12,
            bg="#00c853",
            fg="white",
            font=("Segoe UI", 11),
            command=self.start
        )
        start_btn.grid(row=0, column=0, padx=10)

        stop_btn = tk.Button(
            btn_frame,
            text="Stop",
            width=12,
            bg="#d50000",
            fg="white",
            font=("Segoe UI", 11),
            command=self.stop
        )
        stop_btn.grid(row=0, column=1, padx=10)

        self.running = False

    def update_system(self):

        if not self.running:
            return

        temp = self.env.temperature
        action = self.agent.decide(temp)

        self.env.update(action)

        self.temp_label.config(text=f"Temperature: {temp:.2f} °C")

        if action == "ON":
            self.ac_label.config(text="AC State: ON", fg="#00ff9c")
            self.status_label.config(text="Cooling Room ❄")
        else:
            self.ac_label.config(text="AC State: OFF", fg="#ff6b6b")
            self.status_label.config(text="Room Warming ☀")

        self.root.after(2000, self.update_system)

    def start(self):
        self.running = True
        self.status_label.config(text="Simulation Running")
        self.update_system()

    def stop(self):
        self.running = False
        self.status_label.config(text="Simulation Stopped")


# -----------------------------
# Run Program
# -----------------------------
root = tk.Tk()
app = ThermostatGUI(root)
root.mainloop()