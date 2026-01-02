import streamlit as st
import pandas as pd
import os
from utils import plot_bar_chart

DATA_DIR = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

st.title("📊 E-Commerce Analytics Dashboard")
st.markdown("Dashboard interaktif untuk menganalisis performa penjualan, kategori produk, dan demografi pelanggan.")
st.markdown("Tautan google collabs : https://colab.research.google.com/drive/1nWHYZXLYB1DmkuIP8AmdIdXifmXKhRQM#scrollTo=QnGzqQaHGVZQ")


@st.cache_data
def load_data():
    file_path = os.path.join(DATA_DIR, "customers_orders_order_items_order_payments_products_df.csv")
    df = pd.read_csv(file_path)
    
    datetime_cols = [
        'order_purchase_timestamp', 'order_approved_at', 
        'order_delivered_carrier_date', 'order_delivered_customer_date', 
        'order_estimated_delivery_date'
    ]
    for col in datetime_cols:
        df[col] = pd.to_datetime(df[col], errors='coerce')
        
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("File dataset tidak ditemukan. Pastikan file CSV berada di direktori yang sama.")
    st.stop()


st.sidebar.header("🎛️ Filter Data")

min_date = df['order_purchase_timestamp'].min().date()
max_date = df['order_purchase_timestamp'].max().date()

try:
    start_date, end_date = st.sidebar.date_input(
        "Pilih Rentang Tanggal",
        value=[min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )
except ValueError:
    st.sidebar.error("Harap pilih rentang tanggal yang valid (Start & End).")
    start_date, end_date = min_date, max_date


filtered_df = df[
    (df['order_purchase_timestamp'].dt.date >= start_date) & 
    (df['order_purchase_timestamp'].dt.date <= end_date)
]


all_states = sorted(filtered_df['customer_state'].unique())
selected_states = st.sidebar.multiselect("Pilih Provinsi (State)", all_states, default=all_states[:3])

all_categories = sorted(filtered_df['product_category_name'].astype(str).unique())
selected_categories = st.sidebar.multiselect("Pilih Kategori Produk", all_categories)

all_payment_types = sorted(filtered_df['payment_type'].unique())
selected_payments = st.sidebar.multiselect("Pilih Tipe Pembayaran", all_payment_types)

if selected_states:
    filtered_df = filtered_df[filtered_df['customer_state'].isin(selected_states)]

if selected_categories:
    filtered_df = filtered_df[filtered_df['product_category_name'].isin(selected_categories)]

if selected_payments:
    filtered_df = filtered_df[filtered_df['payment_type'].isin(selected_payments)]


total_sales = filtered_df['payment_value'].sum()
total_orders = filtered_df['order_id'].nunique()
avg_order_value = total_sales / total_orders if total_orders > 0 else 0

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Penjualan", value=f"R$ {total_sales:,.2f}")
    
with col2:
    st.metric(label="Total Pesanan", value=f"{total_orders:,}")

with col3:
    st.metric(label="Rata-rata Nilai Pesanan", value=f"R$ {avg_order_value:,.2f}")

st.markdown("---")


st.subheader("📈 Tren Penjualan Harian")
daily_sales = filtered_df.groupby(filtered_df['order_purchase_timestamp'].dt.date)['payment_value'].sum().reset_index()
daily_sales.columns = ['Date', 'Total Sales']
st.area_chart(daily_sales.set_index('Date'), color="#2980b9")

col_charts1, col_charts2 = st.columns(2)

with col_charts1:
    top_products = filtered_df.groupby('product_category_name')['payment_value'].sum().reset_index()
    top_products = top_products.sort_values(by='payment_value', ascending=True).tail(10) # Ambil top 10

    plot_bar_chart(
        df=top_products,
        x='payment_value',
        y='product_category_name',
        subheader="Top 10 Kategori Produk (by Revenue)",
        info="Detail Kategori",
        is_orientation_h=True,
        key="bar_products"
    )

with col_charts2:
    payment_counts = filtered_df['payment_type'].value_counts().reset_index()
    payment_counts.columns = ['payment_type', 'count']
    payment_counts = payment_counts.sort_values(by='count', ascending=True)
    
    plot_bar_chart(
        df=payment_counts,
        x='count',
        y='payment_type',
        subheader="Distribusi Metode Pembayaran",
        info="Detail Pembayaran",
        is_orientation_h=True,
        key="bar_payment"
    )

st.markdown("---")

st.subheader("🗺️ Wilayah Provinsi Paling Sering Transaksi")
state_counts = filtered_df['customer_state'].value_counts().reset_index()
state_counts.columns = ['customer_state', 'count']
state_counts = state_counts.sort_values(by='count', ascending=True).tail(10) 
plot_bar_chart(
    df=state_counts,
    x='count',
    y='customer_state',
    subheader="",
    info="Detail Provinsi",
    is_orientation_h=True,
    key="bar_states"
)

st.markdown("---")