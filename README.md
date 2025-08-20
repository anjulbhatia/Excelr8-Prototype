# Excelr8 – AI Survey Data Processing Portal
## Overview

Excelr8 is a prototype developed for Statathon 2025.
It is an AI-powered survey data processing portal that helps statistical agencies automate data cleaning, weighting, estimation, and report generation.

Built with FastAPI (backend) and HTMX + Tailwind (frontend), the tool demonstrates how modern AI + automation can enhance efficiency, consistency, and reliability in survey data workflows.

## Problem Statement

Current workflows for processing large-scale survey data in government agencies are manual, time-consuming, and error-prone.
Preprocessing steps such as missing value imputation, outlier detection, validation, and weighting often lead to delays, inconsistencies, and reduced reproducibility of official statistics.

The challenge: Design and prototype an AI-assisted system that streamlines these steps, reduces errors, and produces standardized, reproducible outputs for statistical reporting.

## Features (Prototype)

- Upload CSV/Excel survey datasets

- Data Cleaning options (imputation, outlier detection, rule-based validation)

- Apply design weights for estimation

- Generate quick summaries & mock reports (HTML/PDF)

- LLM integration (OpenAI/Gemini) for explanations, summaries, insights

## Tech Stack

Frontend: HTMX + TailwindCSS (For Application we will use NextJS)

Backend: FastAPI (Python)

LLM APIs: OpenAI / Gemini (via api_handler.py)

# Team

**Team Quantara**

Anjul Bhatia
Srishti Gupta

# Competition

Event: Statathon 2025
