
# Thermostat Controller (Simple Reflex Agent)

## Project Overview

This project demonstrates the implementation of a **Simple Reflex AI Agent** using Python.
The agent controls an air conditioner based on room temperature using predefined condition–action rules.

A graphical user interface is implemented using **Tkinter** to visualize the interaction between the agent and the environment.



# AI Concept Demonstrated

The project implements a **Simple Reflex Agent**.

A Simple Reflex Agent:

* Reacts only to the **current percept**
* Uses **condition–action rules**
* Has **no memory of past states**
* Does **not perform planning**

---

# Agent Rule

IF temperature > 25°C → Turn ON AC
IF temperature ≤ 22°C → Turn OFF AC

---

# System Components

## 1 Environment

Represents the room and maintains the temperature state.

Temperature changes based on:

* AC state
* Natural warming
* Random environmental fluctuation

---

## 2 Agent

The thermostat agent:

* Reads current temperature
* Applies condition–action rules
* Decides whether the AC should be ON or OFF

---

## 3 Sensor

Measures the current room temperature.

---

## 4 Actuator

The air conditioner which affects the room temperature.

---

# Technologies Used

Python
Tkinter GUI
Object-Oriented Programming
Artificial Intelligence (Agent-Based Model)

---

# Program Workflow

Environment → Sensor → Agent → Action → Environment

The system runs continuously and updates temperature every second.

---

# Features

Interactive GUI
Real-time temperature simulation
AI reflex decision making
Clear visualization of agent-environment interaction

---

# Educational Purpose

This project is useful for understanding:

* AI agent architectures
* Reflex-based decision systems
* Environment-agent interaction
* GUI simulation for AI models

---

# Future Improvements

Model-Based Agent implementation
Smart energy optimization
Machine learning temperature prediction
Graph visualization of temperature changes
