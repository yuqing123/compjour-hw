-Quick pitch

Data from US census show more and more young adults living with parents since 1980, while their median earning stays relatively stable.

-The old way

1. Go to census bureau website => American community survey => ACS Factfinder
2. Search for "young adults (18-34) percentage living with parent" with desired geolocation
3. Download Data
4. Search for "young adults (18-34) median earning" with desired geolocation
5. Download Data
6. Compare two datasets by themselves

-The new way

1. Go to my website and explore the interactive graphic/table

-Where does the data come from? How is it collected?

Data is downloadable from US census bureau.

-What data-cleaning/processing needs to be done?

Some fields are left blank in the data.

-How will the data be stored?

I will be working with data from 1980, 1990, 2000, 2009-2013. It is going to be four seperate CSV files in my disk. The downloadable data is in CSV format, which needed to bo converted to JSON format to work with Google Charts. 

-Who else has done it and how is your attempt better?
The US census bureau built a website for people to explore the data on young adults, including population, median earning, percentage living with parents, etc. The website has charts, tables, maps on both national, state and county level, which makes it hard to navigate. Readers can easily be overwhelmed by the amount of information.

-Have other people tried to do what you've done? How is your attempt better?
WSJ cited a graphic when writing about the issue, it's not interactive and the y-axis didn't start from 0, making it misleading.
![](http://i.imgur.com/LHXhVbU.png)

-Pre-mortem

People couldn't open the website at all, I somehow didn't connect it to the Internet right.