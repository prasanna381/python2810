# Remove HTML Tags
from bs4 import BeautifulSoup

str = """<div class="brand">
            <img src="/img/logo.png" alt="Digital Edify logo">
            <h1>Digital Edify</h1>
            <p>India's #1 Premium Training Institute</p>
        </div>
        """

cleaned_text = BeautifulSoup(str, 'html.parser').get_text()

print(cleaned_text)

# Remove URLs
import re

str = "Check out the trailer at https://youtube.com/GAD89AD"

str2 = "Read the complete article at https://medium.com/@techworld/ai-future-2025"

str3 = "Get more updates on https://linkedin.com/company/digitaledify"

cleaned_text = re.sub(r'http\S+|wwwS+', '', str2 + " " + str3)

print(cleaned_text)
