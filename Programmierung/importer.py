# 1. Import the requests library
import requests

URL = "https://cvltnation.com/wp-content/uploads/2019/01/SLAVES_OF_FEAR_INSTA8.jpg"

# 2. download the data behind the URL
response = requests.get(URL)

# 3. Open the response into a new file called instagram.ico
open("health.jpg", "wb").write(response.content)