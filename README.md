# Agentic AI Systems - Software Lab

**Author:** Ankita Bagal  
**Roll Number:** BT23CSE012  
**Framework:** LangChain  
**LLM:** Google Gemini (1.5 Flash)

## Objective
This repository contains a progressive series of assignments completed for the Agentic AI Systems Software Lab. The objective is to explore the evolution of AI agents, moving from rigid rule-based logic to autonomous, LLM-powered multi-step planning systems capable of utilizing external tools.

Assignment Breakdown
Day 1: Rule-Based AI Agent
A foundational script demonstrating the basic input-decision-action pipeline without an LLM. It relies on hardcoded intent matching (keyword detection) to route user queries to simple Python functions like a basic calculator or date retriever.

Day 2: Tool-Using Agent
Introduces modularity by separating the execution logic into a dedicated tools.py file. The agent parses user input and routes it to specific abstracted tools (calculator, mocked weather API, simple summarizer).

Day 3: LLM-Based Agent
Replaces the hardcoded rule-based logic with an LLM (Google Gemini). LangChain's @tool decorator is used to format Python functions so the LLM can interpret them. The model analyzes the input, autonomously decides which tool is required, and passes the correct arguments to execute it.

Day 4: Multi-Step Agent (Planning)
Implements LangChain's AgentExecutor to create a fully autonomous loop. The agent is prompted to break complex instructions into sequential steps. It utilizes a scratchpad to track intermediate outputs, feeding the results of one tool (like the calculator) directly into another (like the summarizer) to formulate a final, cohesive response.