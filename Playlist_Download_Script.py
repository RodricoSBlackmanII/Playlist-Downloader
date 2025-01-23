'''
Created on Nov 18, 2020

@author: Hitma
'''
from selenium import webdriver
import time
import youtube_dl
import os
 
#dl_hw_mny = int(input("How many videos would you like? Default is 6"))
 
video_list = []
driver = webdriver.Chrome()
driver.get('https://www.youtube.com/playlist?list=PLalSVsJOhiwDaGLrfb_s6iOOh-wCVp8fL')

time.sleep(10)

for c in range(0, 30):
    time.sleep(1)
    driver.execute_script("scroll(0, 999999);")

ids = driver.find_elements_by_xpath("//*[@id='video-title']")
for ii in ids:
    #print ii.tag_name
    print(ii.get_attribute('href'))    # id name as string
    video_list.append(ii.get_attribute('href'))
driver.quit()
print("This is video list", video_list)

 #Audio Downloader
params = {
    'format': "bestaudio/best",
    'postprocessors':[{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
        }],
}
    
yt_dl = youtube_dl.YoutubeDL(params)

for x, item in enumerate(video_list):
    yt_dl.download([video_list[x]])
    time.sleep(30)l
    
print("done.")