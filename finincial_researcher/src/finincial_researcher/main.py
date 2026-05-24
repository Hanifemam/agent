#!/usr/bin/env python
# src/finincial_researcher/main.py
import os
from pathlib import Path
from dotenv import load_dotenv
from finincial_researcher.crew import ResearchCrew

# Load local environment variables before CrewAI initializes any providers.
load_dotenv("/Users/hanifemamgholizadeh/Desktop/Projects/Agent/.env")

# Create output directory if it doesn't exist
os.makedirs("output", exist_ok=True)


def run():
    """
    Run the research crew.
    """
    inputs = {"company": "Apple"}

    # Create and run the crew
    result = ResearchCrew().crew().kickoff(inputs=inputs)

    # Print the result
    print("\n\n=== FINAL REPORT ===\n\n")
    print(result.raw)

    print("\n\nReport has been saved to output/report.md")


if __name__ == "__main__":
    run()
