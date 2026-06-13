import os

target_dir = r"G:\Agent2026Win\agents\1_foundations\tai lieu"

titles = [
    "13. Day 3 - Multi-LLM API Integration: Comparing OpenAI, Anthropic & Other Models",
    "14. Day 3 - Comparing LLM APIs: Using OpenAI Client Library with Claude, Gemini & ++",
    "15. Day 3 - Multi-Model Orchestration: Creating a System to Evaluate AI Responses",
    "16. Day 3 - Connecting Agentic Patterns to Tool Use: Essential AI Building Blocks",
    "17. Day 4 - Comparing AI Agent Frameworks: Simplicity vs Power in LLM Orchestration",
    "18. Day 4 - Resources vs. Tools: Two Ways to Enhance LLM Capabilities in Agentic AI",
    "19. Day 4 - Build a Web Chatbot That Acts Like You Using Gradio & OpenAI",
    "20. Day 4 - Using Gemini to Evaluate GPT-4 Responses: A Multi-LLM Pipeline",
    "21. Day 4 - Building Agentic LLM Workflows: Resources, Tools & Structured Outputs",
    "22. Day 5 - Building Your Career Alter Ego: LLM Function Calling with Push Alerts",
    "23. Day 5 - LLM Tool Calls Demystified: How to Process and Execute Function Requests",
    "24. Day 5 - Building AI Assistants: Implementing Tools for Handling Unknown Questions",
    "25. Day 5 - Creating & Deploying an AI Agent: From Chat Loop to HuggingFace Spaces",
    "26. Day 5 - Deploying Career Conversation Chatbots to Gradio",
    "27. Day 5 - Foundation Week Wrap-up: Building Complete AI Agents with APIs & Tools",
    "28. Day 5 [Extra] - Building Your First Agent Loop with OpenAI Tools from Scratch"
]

os.makedirs(target_dir, exist_ok=True)

for title in titles:
    # Replace ':' with '-' as Windows filenames cannot contain ':'
    safe_title = title.replace(":", " -")
    filename = f"{safe_title}.txt"
    filepath = os.path.join(target_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("")  # Create empty file
    print(f"Created: {filename}")
