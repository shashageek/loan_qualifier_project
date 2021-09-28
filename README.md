# loan_qualifier_project

The project of creating an application that helps user to screen qualified loans based on user's information. The application works by taking in a `daily_rate_sheet` of loan criteria from various loan providers through the `Path` provided by the user, asking the user a number of questions to evaluate their loan eligibility, and then returning to them a list of qualifying loans. This application then asks whether the user wants to save the list and if so the list is saved to a `Path` provided again by the user. 

---

## Technologies

This project leverages python 3.7 with the following packages:

* [fire](https://github.com/google/python-fire) - For the command line interface, help page, and entrypoint.

* [questionary](https://github.com/tmbo/questionary) - For interactive user prompts and dialogs

---

## Installation Guide

Before running the application first install the following dependencies.

```python
  pip install fire
  pip install questionary
```

---

## Usage


To use the loan qualifier application simply clone the repository and run the **app.py** with:

```python
python app.py
```

Upon launching the loan qualifier application you will be greeted with the following prompts.

![Loan Qualifier Prompts](images/qualifier.png)

The below save prompts will ask you whether to save the result and where to save it. 

![Save csv Prompts](images/save_csv.png)

---

## Contributors

Brought to you by SL Home Loans.

---

## License

SL


