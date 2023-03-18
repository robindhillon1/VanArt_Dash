# Proposal

The original proposal for `VanArt` can be found [here](https://github.com/UBC-MDS/VanArt/blob/main/reports/proposal.md). The following proposal is updated slightly to conform to `VanArt_Dash`, while the majority of the proposal still remains the same. 
## Motivation and purpose

|                    |                                                                       |
|--------------------|-----------------------------------------------------------------------|
| Our Role           | Data science team hired by Vancouver Travel and Tourism               |
| Target Audience    | Tourists visiting Vancouver.                                          |
| Secondary Audience | Vancouver locals who enjoy art, other artists hoping to be inspired   |

Public art is an important aspect of any city as it reflects the culture, history, and values of a community. Vancouver is known for its vibrant and diverse arts scene, and as a result, it has a plethora of public art installations that locals and tourists can explore. However, apart from some well-known museums that gather art collections together, with so many public art installations scattered throughout the city, it can be difficult for tourists to find the art they are interested in. As a result, we want to provide tourists with a centralized location to find information on public art in Vancouver.

The `VanArt_Dash` app provides a simpler, interactive dashboard compared to `VanArt` that allows tourists to easily find the public art they are interested in. By providing information on the location, the dashboard will not only help tourists find the public art they are looking for but also provide context and background on each installation. Additionally, `VanArt_Dash` can serve as a tool to promote public art and encourage people to explore Vancouver. Overall, `VanArt_Dash` has the potential to enhance the experience of tourists visiting Vancouver by providing them with a unique and enriching way to explore the city's public art. Although geared towards tourists, `VanArt_Dash` can be used by anyone interested in the Vancouver public art scene; locals who would like to explore their city’s public art are welcome to and encouraged to use `VanArt_Dash`.

## Description of the data
We'll be using a dataset that contains information on roughly 470 public artworks in Vancouver, with each artwork having 11 features/variables. These variables are described below:
-	`Title of Work`: the title of the artwork 
-	`Type`: the type of art (mural, statue, etc.)
-	`Status`: whether this art is in place or deaccessioned 
-	`SiteAddress`: address of artwork
-	`Neighbourhood`: neighbourhood where the work is located
-	`geo_point_2d`: latitude and longitude of the artwork
-	`PhotoURL`: the photo URL
-	`URL`: url with artwork information
-	`DescriptionOfWork`: brief introduction to the artwork
-	`YearOfInstallation`: the year artwork was installed

Note that for `VanArt_Dash`, not all of the aforementioned columns made it to the final product. For example, the popups do not have embedded images. This is simply due to `VanArt_Dash` being a simpler version of `VanArt`. 

## Research questions and usage scenarios

**Some research questions that our project tackles are described below:**

1.	Where can I find publicly displayed art in Vancouver? Which neighbourhoods have the most publicly displayed art?  
2.	Which artists have art displayed across Vancouver? 
3.	What types (e.g. murals, statues) of public art are there in different neighbourhoods in Vancouver? 
4.	What type of art is most abundant in Vancouver? 

**An example usage scenario of our dashboard by a tourist is as follows:**

Imagine you’re a tourist visiting different parts of the world in search of art that speaks to your soul. In your travels, you finally reach the beautiful city of Vancouver. Being the art fiend you are, you quickly exhaust all the art museums and galleries but your craving for art is still not satiated. Since you’re a proper tourist, you wander the streets in hopes of discovering public art that will quench this thirst for art. However, this is a laborious effort and you wish there were a tool that could guide you to these public art pieces. This is where `VanArt_Dash` comes in. 

`VanArt_Dash` is a dashboard that guides the user to various public artworks located in Vancouver. Specifically, `VanArt_Dash` displays the map of Vancouver and geographically shows the locations of the aforementioned public art pieces, and the corresponding number of art pieces belonging to a specific location. 

Wherever these art pieces exist in Vancouver, they would have a corresponding blue point indicating their position. When hovered over these points, a popup provides vital information regarding the artwork such as the title of the work, the art type, and the physical location of the piece. Our dashboard allows the user to select the neighbourhood they're interested in. This gives the tourist more control and convenience regarding where they should travel and look for the art pieces. Depending on the user input, the dashboard also shows a barplot corresponding to the types of art (and their count) in that neighbourhood. By default, the main leaflet map shows all public artworks in Vancouver.

Ultimately, the usage scenarios of our dashboard are immense. Everyone can use this dashboard, not just tourists, to discover public art in Vancouver.
