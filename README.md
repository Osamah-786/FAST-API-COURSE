# FastAPI Learning Journey 🚀

This repository contains my hands-on practice and mini projects while learning **FastAPI** from the CampusX FastAPI tutorial series. The goal of this repository is to understand how modern APIs are built using FastAPI, Pydantic, request validation, CRUD operations, and deployment concepts.

## What I Learned

During this learning journey, I explored:

- FastAPI fundamentals
- Creating API endpoints
- Path and Query Parameters
- Request and Response Models
- Pydantic Validation
- Field Validators
- Model Validators
- Computed Fields
- Exception Handling
- CRUD Operations
- JSON Data Storage
- API Documentation using Swagger UI
- Building Machine Learning APIs
- Connecting FastAPI with Streamlit Frontend

---

## Projects Included

### 1. Pydantic Validation Practice
Implemented various validation techniques using Pydantic:

- Field Constraints
- Email Validation
- URL Validation
- Optional Fields
- Custom Validators
- Data Type Conversion

### 2. Patient Management System API

A complete CRUD API for managing patient records.

#### Features

- Create Patient
- View All Patients
- View Single Patient
- Update Patient Information
- Delete Patient
- BMI Calculation
- Health Verdict Generation
- Sorting Patients by:
  - Height
  - Weight
  - BMI

#### Technologies Used

- FastAPI
- Pydantic
- JSON Database

---

### 3. Insurance Premium Prediction API

A Machine Learning API built using FastAPI.

#### Features

- User Input Validation
- BMI Calculation
- Lifestyle Risk Analysis
- Age Group Classification
- City Tier Detection
- Insurance Premium Category Prediction

#### Input Parameters

- Age
- Weight
- Height
- Income
- Smoker Status
- City
- Occupation

#### Output

- Predicted Insurance Premium Category

---

### 4. Streamlit Frontend

Created a simple Streamlit interface that interacts with the FastAPI backend and displays prediction results in a user-friendly way.

---

## Project Structure

```text
.
├── 1st_pydantic.py
├── 2nd_field_validator.py
├── 3rd_model_validator.py
├── 4th_computed_field.py
├── main(4).py
├── main2.py
├── main3.py
├── lect_7_app.py
├── fronted.py
├── patient.json
├── model_api.pkl
├── requirements.txt
└── README.md
