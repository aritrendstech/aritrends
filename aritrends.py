from docx2pdf import convert
import qrcode
import zipfile
import datetime
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import webbrowser
print("http://aritrends.tech\nType 'aritrends.credits()', 'aritrends.license()' or 'aritrends.github()' for more information")

def rnm():
	return str(datetime.datetime.now()).replace("-","").replace(".","").replace(":","").replace(" ","")

class aritrends:
	def docx2pdf(filename):
		try:
			convert(filename, rnm()+".pdf")
		except Exception as e:
			print(e)
	def zip(list):
		n= rnm()
		var = zipfile.ZipFile(n+".zip","w")
		try:
			for i in list:
				var.write(i)
		except Exception as e:
			print(e)
	def image2pdf(list):
		n = rnm()
		t=[]
		try:
			for i in list:
				t.append(Image.open(i).convert("RGB"))
			k = t[0]
			t.remove(t[0])
			k.save(str(n)+".pdf", save_all=True, append_images=t)
		except Exception as e:
			print(e)
	def qrcode(text):
		qrcode.make(text).save(rnm()+".png")
	def github():
		webbrowser.open("http://github.com/aritrendstech")
	def credits():
		print("This project is developed by Abhineet Raj (github-> @abhineetraj1).")
	def write_text_on_image(text, image, font)
		if ("" in [text,image]):
			print("Enter valid details")
		elif (None in [text,image]):
			print("Enter valid details")
		else:
			try:
				# Open an Image
				img = Image.open(image)
				# Call draw Method to add 2D graphics in an image
				I1 = ImageDraw.Draw(img)
				if (font == None):
					# Custom font style and font size
					myFont = ImageFont.truetype("arial.tff",25)
				else:
					# default font style and font size
					myFont = ImageFont.truetype(font[0].lower()+".tff",font[1])
				# Add Text to an image
				I1.text((10, 10), text, font=myFont, fill =(255, 0, 0))
				# Display edited image
				img.show() 
				# Save the edited image
				img.save(image)
			except Exception as e:
				print(e)
	def license():
		print("""MIT License
Copyright (c) 2022 Aritrends

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.""")
