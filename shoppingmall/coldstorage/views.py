from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.
def index(request):
    render(request, "coldstorage/index.html")

    list_of_food = []
    keyword="bread"
    if request.method == "POST":
        keyword = request.POST['q']
    URL = f"https://coldstorage.com.sg/search?q={keyword}"

    page = requests.get(URL)
    parse_html = BeautifulSoup(page.content, "html.parser")
    parsed_list_of_food = parse_html.find_all("div", class_="open-product-detail" ) #job-container

    for food in parsed_list_of_food:
        foodname = food.find("div", class_="product_name").text
        price = food.find("div", class_="product_price").text
        image = food.find("img").get("src")
        url = "https://coldstorage.com.sg/" + food.find('a').get("href")
        if food.find("span", class_="l-halal"):
            halal = food.find("span", class_="l-halal").find("img").get("src")
        else:
            halal = None

        if food.find("div", class_="category-name"):
            brandname = food.find("div", class_="category-name").text
        else:
            brandname = None

        if food.find("span", class_="l-brand-blurb"):
            print(food.find("span", class_="l-brand-blurb").find("img").get("src"))
            brand = food.find("span", class_="l-brand-blurb").find("img").get("src")
            # brand.get("src")
            # brand.get("alt")

        else:
            brand = None
        


        list_of_food.append({ 
                            "name" : foodname, 
                            "price" : price,
                            "image" : image,
                            "url" : url,
                            "halal" : halal,
                            "brand" : brand,
                            "brandname" : brandname
                            })

    return render(request, "coldstorage/index.html", { "foods" : list_of_food})

    