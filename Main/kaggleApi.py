#pull data from kaggledan with api
import os
from zipfile import ZipFile
from kaggle.api.kaggle_api_extended import KaggleApi
import warnings

#Kaggle'dan api ile veri çekme, çekilen veriyi zip'ten çıkarma ve zip'i silme sınıfı oluşturuldu.

class DataCollection():
    def __init__(self):
        self.dataset_name = "whenamancodes/predict-diabities" #veri setinin adı
        self.file_path = "../Data/predict-diabities}" #zip dosyasının yolu
    def download_dataset(self):
        api = KaggleApi()
        api.authenticate()
        api.dataset_download_files(self.dataset_name, path='../Data', unzip=True)
        print("Dataset is downloaded")



    # diabetes.csv dosyası zip'ten çıkarıldıktan sonra ../Data klasörünün altına taşıyalım

def move_file(self):
        os.rename(f'../Data/predict-diabities/diabetes.csv', f'../Data/diabetes.csv')
        print("Dataset is moved")

def delete_file(self):
        os.remove(self.file_path)
        print("Zip file is deleted")

#Kaggle'dan çekilen veri setinin içindeki dosyaların isimlerini döndüren fonksiyon oluşturuldu.
def get_file_names():
    file_names = []
    for dirname, _, filenames in os.walk('/kaggle/input'):
        for filename in filenames:
            file_names.append(os.path.join(dirname, filename))
    return file_names

#Dosya varsa veri çekme, çekilen veriyi zip'ten çıkarma ve zip'i silme fonksiyonları çağırıldı.
if __name__ == "__main__":
    data_collection = DataCollection()
    data_collection.download_dataset()
    data_collection.move_file()
    data_collection.delete_file()