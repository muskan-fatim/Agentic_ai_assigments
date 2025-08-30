# Guardrails Project

This project demonstrates the implementation of three different types of guardrails using Python. Guardrails are used to enforce specific rules or constraints on input data or processes. Below is an overview of the guardrails implemented in this project.

## Guardrails Overview

### 1. GIAIC Student Checker
- **File**: `input_guardrails.py`
- **Function**: `giaic_student_checker`
- **Purpose**: Verifies if the input corresponds to a GIAIC student. If not, the guardrail triggers a tripwire to block further execution.

### 2. Class Timings Guardrail
- **File**: `input_guardrails.py`
- **Function**: `class_timings_guardrail`
- **Purpose**: Ensures that the input is related to class timings. If

### 3. Temprature checker
- **File**: `input_guardrails.py`
- **Function**: `temperature_checker`
- **Purpose**: Verifies if the input temprature below to 26c. If not, the guardrail triggers a tripwire to block further execution.
