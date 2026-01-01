import streamlit as st
import pandas as pd
import os
from utils import plot_bar_chart

st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")
script_dir = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = script_dir


products_order_items_df = pd.read_csv(os.path.join(DATA_DIR, "products_order_items_df.csv"))
customers_orders_order_payments_df = pd.read_csv(os.path.join(DATA_DIR, "customers_orders_order_payments_df.csv"))
customers_orders_order_items_df = pd.read_csv(os.path.join(DATA_DIR, "customers_orders_order_items_df.csv"))
rfm_df = pd.read_csv("rfm_df.csv")

print(f"Product Order Item :")
products_order_items_df.info()
print(f"Customer Orders Order Pyaments :")
customers_orders_order_payments_df.info()
print(f"Customers Orders Order Items :")
customers_orders_order_items_df.info()
print(f"RFM :")
rfm_df.info()



st.title("📊 Dashboard Analisis E-Commerce")
st.markdown("Visualisasi interaktif ini adalah hasil dari analisis https://colab.research.google.com/drive/1nWHYZXLYB1DmkuIP8AmdIdXifmXKhRQM#scrollTo=VC1MBWVyECYh")

tab1, tab2, tab3, tab4 = st.tabs(["🛍️ Produk & 🌍 Wilayah", "💵 Pendapatan", "🕒 Recency & Frequency", "💰 Monetary"])

with tab1:
    st.info("ℹ️ Klik diagram untuk melihat detail")
    col1, col2 = st.columns(2)
    with col1:
        product_cat_highest = products_order_items_df['product_category_name'].value_counts().reset_index()
        product_cat_highest = product_cat_highest.sort_values(by='count', ascending=False).head(10)
        plot_bar_chart(
            df=product_cat_highest, x='count', y='product_category_name',  subheader='Top 10 Kategori Produk Terlaris',
            info='Detail Kategori', is_orientation_h=True, key='p1'
        )

    with col2:
        product_cat_lowest = products_order_items_df['product_category_name'].value_counts().reset_index()
        product_cat_lowest = product_cat_lowest.sort_values(by='count', ascending=True).head(10)
        plot_bar_chart(
            df=product_cat_lowest, x='count', y='product_category_name', subheader='Top 10 Kategori Produk Kurang Laku',
            info='Detail Kategori', is_orientation_h=True, key='p2'
        )
    

    cust_state = customers_orders_order_payments_df['customer_state'].value_counts().reset_index()
    cust_state = cust_state.sort_values(by='count', ascending=False).head(10)
    plot_bar_chart(
        df=cust_state, x='count', y='customer_state', subheader='Wilayah Provinsi Paling Sering Transaksi',
        info='Wilaya', is_orientation_h=True, key='p3'
    )


with tab2:
    st.info("ℹ️ Klik diagram untuk melihat detail")
    col1, col2 = st.columns(2)
    with col1:
        purhcase_highest = customers_orders_order_payments_df.groupby('purchase_month')['payment_value'].sum().reset_index()
        purhcase_highest = purhcase_highest.sort_values(by='payment_value', ascending=False).head(10)
        plot_bar_chart(
            df=purhcase_highest, x='payment_value', y='purchase_month', subheader='Top 10 Total Pendapatan Tertinggi',
            info='Bulan', is_orientation_h=True, key='p4'
        )

    with col2:
        purhcase_lowest = customers_orders_order_payments_df.groupby('purchase_month')['payment_value'].sum().reset_index()
        purhcase_lowest = purhcase_lowest.sort_values(by='payment_value', ascending=True).head(10)
        plot_bar_chart(
            df=purhcase_lowest, x='payment_value', y='purchase_month', subheader='Top 10 Total Pendapatan Terendah',
            info='Bulan', is_orientation_h=True, key='p5'
        )


with tab3:
    st.info("ℹ️ Klik diagram untuk melihat detail")
    col1, col2 = st.columns(2)
    with col1:
        rec_latest = rfm_df.sort_values(by='recency', ascending=True).head(10)
        plot_bar_chart(
            df=rec_latest, x='recency', y='customer_id', subheader='Top 10 Pelanggan Terakhir Transaksi dalam Satuan Hari (recency)',
            info='ID Pengguna', is_orientation_h=True, key='p6'
        )

        freq_highest = rfm_df.sort_values(by='frequency', ascending=True).head(10)
        plot_bar_chart(
            df=freq_highest, x='frequency', y='customer_id', subheader='Top 10 Pelanggan Paling Sering Transaksi (frequency)',
            info='ID Pengguna', is_orientation_h=True, key='p7'
        )

    with col2:
        rec_longest = rfm_df.sort_values(by='recency', ascending=False).head(10)
        plot_bar_chart(
            df=rec_longest, x='recency', y='customer_id', subheader='Top 10 Pelanggan Hampir Berhenti Transaksi dalam Satuan Hari (recency)',
            info='ID Pengguna', is_orientation_h=True, key='p8'
        )

        freq_lowest = rfm_df.sort_values(by='frequency', ascending=False).head(10)
        plot_bar_chart(
            df=freq_lowest, x='frequency', y='customer_id', subheader='Top 10 Pelanggan Paling Rendah Transaksi (frequency)',
            info='ID Pengguna', is_orientation_h=True, key='p9'
        )


with tab4:
    st.info("ℹ️ Klik diagram untuk melihat detail")
    col1, col2 = st.columns(2)
    with col1:
        mon_highest = rfm_df.sort_values(by='monetary', ascending=False).head(10)
        plot_bar_chart(
            df=mon_highest, x='monetary', y='customer_id', subheader='Top 10 Pendapatan Paling Tinggi bagi Perusahaan (monetary)',
            info='ID Pengguna', is_orientation_h=True, key='p10'
        )

    with col2:
        mon_lowest = rfm_df.sort_values(by='monetary', ascending=True).head(10)
        plot_bar_chart(
            df=mon_highest, x='monetary', y='customer_id', subheader='Top 10 Pendapatan Paling Rendah bagi Perusahaan (monetary)',
            info='ID Pengguna', is_orientation_h=True, key='p11'
        )