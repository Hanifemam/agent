#!/usr/bin/env python
import sys
import warnings
import os
from pathlib import Path
from dotenv import load_dotenv

from datetime import datetime

from coder.crew import Coder

# Load local environment variables before CrewAI initializes any providers.
load_dotenv("/Users/hanifemamgholizadeh/Desktop/Projects/Agent/.env")

# Create output directory if it doesn't exist
os.makedirs("output", exist_ok=True)

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

assignment = os.makedirs("output", exist_ok=True)

assignment = "Write a python program to calculate the first 10,000 terms \
    of this series, multiplying the total by 4: 1 - 1/3 + 1/5 - 1/7 + ..."


def run():
    """
    Run the crew.
    """
    inputs = {"assignment": assignment}

    try:
        result = Coder().crew().kickoff(inputs=inputs)
        print(result.raw)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
