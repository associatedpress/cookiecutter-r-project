# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

*Created by {{ cookiecutter.full_name }} (<{{ cookiecutter.email }}>)*

*Reporter: {{ cookiecutter.full_name }} (<{{ cookiecutter.email }}>)*

## Project goal

*TK: Briefly describe this project*

## Project notes

[Responsibility matrix](url-to-responsibility matrix)

[HIRUFF Q&A](url-to-hiruff)

## Technical

*TK: Instructions on how to bootstrap project, run ETL processes, etc.*

### Getting started

After cloning the git repo:

`datakit data pull` to rerieve the data files.

Open `{{ cookiecutter.project_slug }}.Rproj` in RStudio.

#### Rebuilding the project

*TK: A pointer to a 'master rebuild' R script, if there is one in the project

### Dependencies

- The usual suspects:
  - `tidyverse`
  - `apstyle`
- Project-specific dependencies:
  - *TODO: Add other dependencies here, ideally with version numbers.*

## Data notes

*Add important caveats, limitations, and source contact info here.*
