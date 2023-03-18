# VanArt_Dash

Welcome to `VanArt_Dash`! This app is a cousin of the original [VanArt](https://github.com/UBC-MDS/VanArt) project created for DSCI 532 (Data Visualization II); a course in the Master of Data Science program at the University of British Columbia. The mission of this app is to help you explore public art in the city of Vancouver.

**Try out the app [here](https://five32-ia-vanart-dash.onrender.com)!**

---

- [Introduction](#introduction)
- [Usagea and Dashboard Overview](#usage-and-dashboard-description)
- [Reference](#reference-and-data-used)
- [Installation](#installation-and-run-locally)
- [Contributing](#contributing)
- [License](#license)

## Introduction

**The problem**

Public art is an important aspect of any city as it reflects the culture, history, and values of a community. Vancouver is known for its vibrant and diverse arts scene, and as a result, it has a plethora of public art installations that locals and tourists can explore. However, apart from some well-known museums that gather art collections together, with so many public art installations scattered throughout the city, it can be difficult for tourists to find the art they are interested in. As a result, we want to provide tourists with a centralized location to find information on public art in Vancouver.

**The solution**

`VanArt_Dash` provides an interactive dashboard that allows tourists to easily find the public art they are interested in. By providing information on the location (the neighbourhood of interest), the dashboard will not only help tourists find the public art they are looking for but also provide context and background on each installation. Additionally, `VanArt_Dash` can serve as a tool to promote public art and encourage people to explore Vancouver. Overall, `VanArt_Dash` has the potential to enhance the experience of tourists visiting Vancouver by providing them with a unique and enriching way to explore the city's public art. Although geared towards tourists, `VanArt_Dash`, like `VanArt`, can be used by anyone interested in the Vancouver public art scene; locals who would like to explore their city’s public art are welcome to and encouraged to use `VanArt_Dash`.

**Proposal**: The original proposal for `VanArt` can be found [here](https://github.com/UBC-MDS/VanArt/blob/main/reports/proposal.md), while the updated proposal for this dash app can be found [here](reports/proposal.md).


## Usage and Dashboard description

`VanArt_Dash` is a much simpler version of `VanArt`, and this is described below:
-   `The dropdown panel`: The user can select the neighbourhood on the top which filters down the art  
    visible on the map. If someone chooses `Downtown`, for example, only art found in `Downtown`
    will be shown. To deselect inputs, simply press backspace. 
-   `The plots panel`: It displays the locations of the public art. When first opening the application 
    (without any user input) the map will display all the art pieces in Vancouver and the corresponding statistics,
    such as the number of art types in Vancouver. The user can also interact with the map directly.
    Hovering over a datapoint will display a popup which gives vital information such as the name of the artwork, 
    the neighbourhood it's located in, its address, and the type of art.  
-   `The card panel`: The total number of artworks are shown depending on the user input. 

The gif below shows how to use the dashboard. Detailed instructions on how to use the dashboard locally are given [here](Installation and run locally).

![VanArt_Dash Gif](Animation.gif)

## Reference and data used

The data set we used to create this app is modified from [City of Vancouver Open Data Portal](https://opendata.vancouver.ca/explore/dataset/public-art/export/).

Our modified data contains the feature about: the title of the artwork, the type of art (mural, statue, etc.), address of artwork, neighborhood where the work is located, latitude and longitude of the artwork, the photo URL, URL with artwork information, brief introduction to the artwork, and the year artwork was installed. Note, however, that not all of these columns are used for this Dash app. 


## Installation and run locally

To make this app run locally on your computer, please:

1. Clone or fork this repository first, and then navigate to the root directory of the repository.
2. Install the environment by following the installation instructions below.

```{bash}
conda env create --file environment.yaml
```
Activate the conda environment:
```{bash}
conda activate VanArt_dash
```
3. Navigate to the `src` folder and run the command in the terminal below:

```{bash}
python app.py
```

4. Ctrl-Click the `http` link displayed in the terminal, or copy paste it into the browser to use the app locally.
```{bash}
Dash is running on http://127.0.0.1:8050/

* Serving Flask app 'app'
* Debug mode: on
```

## Contributing

Interested in contributing? You are welcome to make contributions on our VanArt App! We would love updated information regarding current art pieces, and information regarding art that we don't have in our database. Some updates include:
-   The up-to-date data that contains the information of more art pieces and the art pieces after 2022
-   The information of the artist of these public arts

Also, please check out the [contributing](CONTRIBUTING.md) guidelines. Please note that this project is released with a [Code of Conduct](CODE_OF_CONDUCT.md). By contributing to this project, you agree to abide by its terms.


## License

`VanArt` is licensed under the terms of the [MIT](LICENSE) license.
