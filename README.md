# API JSON Dataflow

A modular Python project that demonstrates how to build a simple data pipeline using JSON configuration files, external APIs and structured JSON outputs.

The application reads a user name from a configuration file, queries multiple public APIs and combines the responses into a single processed user profile.

---

## Overview

This project demonstrates a small end-to-end workflow commonly used in backend systems and data pipelines.

The program reads input data from a JSON configuration file, queries public APIs for predictions and processes the responses into structured output files.

The main goal of this project is to practice API communication, JSON processing and clean Python project structure.

---

## Features

* Read input from a JSON configuration file
* Query multiple public APIs
* Convert API responses into Python dictionaries
* Process and combine API results
* Save raw responses for inspection
* Generate a final processed user profile

---

## APIs Used

| API         | Description                             |
| ----------- | --------------------------------------- |
| Agify       | Predicts age based on name              |
| Genderize   | Predicts gender based on name           |
| Nationalize | Predicts likely countries based on name |

---

## Project Structure

```
api-json-dataflow/
│
├── README.md
├── main.py
│
├── config/
│   └── user.json
│
├── data/
│   ├── raw_age_response.json
│   ├── raw_gender_response.json
│   ├── raw_country_response.json
│   └── final_profile.json
│
└── src/
    ├── api_client.py
    ├── file_handler.py
    └── profile_service.py
```

---

## Workflow

```
config/user.json
        ↓
Read input name
        ↓
Call APIs
(Agify / Genderize / Nationalize)
        ↓
Convert API responses to Python dictionaries
        ↓
Process and combine the results
        ↓
Save structured JSON output
```

---

## Example Input

`config/user.json`

```json
{
  "name": "mynul"
}
```

---

## Example Output

`data/final_profile.json`

```json
{
  "name": "mynul",
  "predicted_age": 46,
  "predicted_gender": "male",
  "predicted_country": "BD"
}
```

---

## Installation

Install the required dependency:

```
pip install requests
```

---

## Run the Application

```
python main.py
```

The script generates raw API responses and a final combined profile in the `data` directory.

---

## Learning Objectives

This project demonstrates several core Python engineering concepts:

* Reading and writing JSON files
* Sending REST API requests in Python
* Extracting and processing API responses
* Designing a modular Python project structure
* Building a simple data processing pipeline

---

## License

This project is intended for learning and experimentation.
