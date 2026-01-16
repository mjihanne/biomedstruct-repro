\# BioMedStruct – Reproducibility Package (Synthetic Data)



This repository provides a minimal, self-contained reproducibility package

illustrating the data preprocessing, structuring, and validation pipeline

used in the associated study on predictive maintenance of biomedical equipment.



\## Scope

\- Fully synthetic data only (no real hospital records)

\- End-to-end demonstration of the BioMedStruct preprocessing pipeline

\- Reproducible model training and validation procedures



\## Repository structure

\- `notebooks/` – End-to-end synthetic simulation of the BioMedStruct pipeline

\- `src/` – Core preprocessing and validation scripts

\- `config/` – Configuration files (hyperparameters, validation settings)

\- `data/` – Synthetic data used for demonstration purposes only



\## Reproducibility

All experiments are deterministic and executed with a fixed random seed

(`random\_state = 42`). The repository allows replication of the methodology

on synthetic or equivalent structured datasets, without access to sensitive data.



\## Data availability

Original hospital maintenance data are subject to confidentiality and

data-governance constraints and cannot be publicly released.



\## License

This repository is provided for academic reproducibility purposes only.



