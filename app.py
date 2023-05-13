import streamlit as st
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open("RandomForestRegressor.pkl", "rb"))

companies = ["Dell", "Lenovo", "HP", "Asus", "Acer", "MSI", "Toshiba",
	     "Apple", "Samsung", "Razer", "Microsoft", "Xiaomi",
	     "Google", "LG", "Huawei"]

typess = ["Notebook", "Ultrabook", "Gaming", "2 in 1 Convertible", "Workstation", "Netbook"]

rams = [2, 4, 6, 8, 16, 32, 64]

op_sys = ["Windows", "Freedos", "macOS"]

yes_no = ["Evet","Hayır"]

resolutions = ["1366x768", "1600x900", "1920x1080", "2560x1440", "2560x1600",
	       "2880x1880", "3200x1800", "3840x2160"]

hdd_size = [0, 128, 256, 512, 1024, 2048]
ssd_size = [0, 8, 128, 256, 512, 1024]
gpus = ["Intel", "Nvidia", "AMD"]
cpus = ["Intel Core i7", "Intel Core i5", "Intel Core i3", "Other Intel Processor", "AMD Processor"]

st.title("Laptop Price Predictor")
company = st.selectbox("Marka", companies)
types = st.selectbox("Tür", typess)
os = st.selectbox("İşletim Sistemi", op_sys)
weight = st.number_input("Ağırlık")
screen_size = st.number_input("Inc")
resolution = st.selectbox("Ekran Çözünürlüğü", resolutions)
ips = st.selectbox("IPS Ekran", yes_no)
touchscreen = st.selectbox("Dokunmatik", yes_no)
ram = st.selectbox("RAM", rams)
cpu = st.selectbox("İşlemci", cpus)
gpu = st.selectbox("Ekran Kartı", gpus)
hdd = st.selectbox("HDD", hdd_size)
ssd = st.selectbox("SSD", ssd_size)

if st.button("Tahmin"):
	if touchscreen == "Evet":
		touchscreen = 1
	else:
		touchscreen = 0

	if ips == "Evet":
		ips = 1
	else:
		ips = 0

	ppi = None
	X_Res = int(resolution.split("x")[0])
	Y_Res = int(resolution.split("x")[1])
	ppi = pow(((pow(X_Res, 2)) + (pow(Y_Res, 2))), 0.5) / (screen_size)
	data = np.array([company, types, cpu, ram, gpu, os, weight, touchscreen, ips, ppi, ssd, hdd])
	data = data.reshape(1, 12)
	print("PRED:", model.predict(data))
	pred = model.predict(data).item()
	st.success("Tahmin edilen ücret " + str(pred - 100) + "€" + " veya " + str(pred+100) + "€")

