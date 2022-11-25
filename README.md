<h1 align="center">Color Palette Generator using NASA's API</h1>

![streamlit app](/img/app.png)
The application is deployed to this url https://helloerikaaa-apod-colorpalette-srcapp-v15wh4.streamlit.app

## 🧐 About <a name = "about"></a>

This simple project intention is to create a small application using streamlit to generate a color palette for the current picture of the APOD (A picture of the day) service using NASA's API to retreive the images.

## 🔖 Project structure

```
Project_folder/
|- src/                                # Folder containing all source code
|- img/                                # Folder containing images used in the README file
|- src/api/api_handler.py              # File with code to retreive the image using the NASA's API
|- src/api/color_extractor.py          # Class with necessary code to extract colors from a image
|- src/image/image_handler.py          # Class to handle all image transformations
|- src/consts/                         # Folder containing constanst used inside the project
|- src/consts/consts.py                # File with necessary constants
|- src/consts/paths.py                 # File containing project paths
|- src/app.py                          # Script to execute the streamlit application
|- Makefile                            # Automatize taks through make utility
|- Pipfile                             # Dependencies
```

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Setup your environement and install project dependencies.

Clone the project repository:

```
git clone git@github.com:helloerikaaa/mlflow-server.git
```

Install Depencencies and start environment using Pipenv:
```
pipenv install
pipenv shell
```

## 🔧 Local environment

To run the project locally, it is necessary to use the Makefile, to execute the streamlit use the following command:

```
make run
```

## 🎈 Contributions

To contribute in this project, please setup locally the project following the steps in Getting started section.
I use few packages to guarantee high quality code.

## ✍️ Authors
* Erika Sánchez Femat (helloerikaaa)