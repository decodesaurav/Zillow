# Zillow Spider Executer

Zillow Spider Executer is a simple tool that scrapes the homes info from Zillow's page

## Requirements

The latest version of Python  
Anaconda Navigator(for the virtual environment)  
IDEs (VS Code or any other)  
git  
Scrapy  
Pillow (for media pipeline)

Make sure to run on a virtual environment after installation. For Windows users, I recommend you install Anaconda Navigator manually as it's a little tricky to install using pip command. Make sure you install everything using a Virtual environment. If you're using an anaconda command terminal make sure you use "conda" commands rather than normal.    

## Installing Scrapy Using Anaconda Navigator Terminal

You can see the documentation of how to set up virtual environment using  [Anaconda Navigator](https://docs.anaconda.com/navigator/getting-started/)

```
conda install -c scrapinghub scrapy
```

## Usage

To run the spider, open the app.py file on the root of Zillow. Run the below command

```
python .\app.py
```
You'll see the app running. You can select the spider you want to run (homes in this case) and you can select the format in which you wish your datasets to be saved. You can select your preferred destination folder on the browse option. On the remaining space, you can give a name to your dataset(homes, houses, listings, etc)

Currently, I've limited the item's scrap count to 200. You can remove it if you want to extract all the data. For that, you should go to the settings.py file and just comment on the below setting

```
CLOSESPIDER_ITEMCOUNT = 200
```
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

