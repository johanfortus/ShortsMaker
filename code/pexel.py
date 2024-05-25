import pexelsPy
import requests
import os
import sys
import shutil

PEXELS_API = '0brxGQgq3WiookAkfmtb4rmTRzbSR56GmuoJyWKKtE8jsGuDybBjDr0E'
api = pexelsPy.API(PEXELS_API)
pageNumbers = 1 
resultsPage = 5 
path = r'D:\makeAutoShorts\env\project\videos' 


def download_video():
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)
    api.search_videos('Sea', page=pageNumbers, results_per_page=resultsPage)
    videos = api.get_videos()
        

    for data in videos:
        url_video = 'https://www.pexels.com/video/' + str(data.id) + '/download'
        r = requests.get(url_video)
        with open(path + "\\" + data.url.split('/')[-2]+'.mp4', 'wb') as outfile:
            outfile.write(r.content)