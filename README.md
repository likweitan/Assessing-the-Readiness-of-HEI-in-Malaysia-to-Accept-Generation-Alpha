# Assessing the Readiness of HEI in Malaysia to Accept Generation Alpha

> A Dashboard for the HEI in Malaysia

<div align="center">
  <br>
  <img src="https://img.shields.io/badge/MADE%20WITH-PYTHON%20-red?style=for-the-badge"
      alt="API stability" height="25"/>
  <img src="https://img.shields.io/badge/SERVED%20WITH-Heroku-blue?style=for-the-badge"
      alt="API stability" height="25"/>
  <img src="https://img.shields.io/badge/DASHBOARDING%20WITH-Streamlit-green?style=for-the-badge"
      alt="API stability" height="25"/>
</div>

<br>

The impact of technology in education is getting more common. In the UK, most of the children start to learn coding skills from the age of 5. Generation Alpha will be very different from traditional college students. Technologies will be largely driven in education and educators need to learn how to adapt to it. The traditional method of teaching and learning might not be effective and efficient for Generation Alpha. Institutional culture needs to be changed to prepare the arrival of Generation Alpha students. In a technology-driven period, students need to learn problem-solving skills to help themselves how to think not what to think, and collaboration skills to collaborate with peers around the world. What will the Generation Alpha students behave in higher education? How to define that an institution is ready to accept Generation Alpha? These questions can be answered by finding the unique pattern of generation z using predictive analytics. The proposed system is a dashboard that allows Higher Education Institution (HEI) to capture and analyse useful insights and improve decision making from the student data.

## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

---

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
