# BioMedStruct – Reproducibility Repository

This repository provides a reproducibility package illustrating the experimental pipeline used in a study on predictive maintenance of biomedical equipment. All materials are based on fully synthetic data.

## Purpose

The repository is intended for methodological reproducibility only. It allows inspection and replication of the main steps of the data structuring, preprocessing, modeling, and validation pipeline without access to real hospital data.

## Contents

- `notebooks/`  
  Jupyter notebooks illustrating the end-to-end experimental workflow on synthetic data.

- `src/`  
  Core scripts for data preprocessing, feature structuring, model training, and validation.

- `config/`  
  Configuration files defining the experimental settings (hyperparameters, validation protocols).

- `data/`  
  Fully synthetic datasets generated for demonstration and reproducibility purposes.

## Reproducibility notes

All experiments are deterministic and executed with a fixed random seed (`random_state = 42`).  
The repository enables replication of the methodological framework on synthetic or equivalent structured datasets.

## License

This repository is provided for academic and reproducibility purposes only.
