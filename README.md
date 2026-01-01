# AI Prompt Workflow

This project is a simple Python-based prompt engineering workflow.

It generates structured, reusable prompts for AI assistants, helping standardize tasks such as text improvement, summarization, or content generation.

## Project Structure

- assistant.py – Builds a complete prompt using predefined templates
- prompts.py – Stores prompt templates (role, task, output format)
- example_output.txt – Example of a generated prompt output

## How It Works

1. Define prompt templates in prompts.py
2. Call build_prompt() in assistant.py
3. The script outputs a fully structured prompt ready to be used in an AI tool

## Example

Input:

This is a simple text that needsd improvement.

Output:

Role: You are an AI writing assistant.
Task: Improve the clarity and professionalism of the text below.
Output format: Rewritten text with better struture.

## Purpose

This project demonstrates:
- Prompt engineering fundamentals
- Python modularization
- Clean and reusable code structure

Ideal for junior developers and AI-assisted workflows.
