import streamlit as st
from manager import FinanceManager

if 'finance_manager' not in st.session_state:
    st.session_state.finance_manager = FinanceManager()
    st.session_state.finance_manager.load_from_json('data.json')

qarzhy_esebi = st.session_state.finance_manager

st.title("💰 Personal Finance Tracker")

st.sidebar.header("Жаңа транзакция қосу (Добавить)")
amount = st.sidebar.number_input("Сомасы (tg):", min_value=0.0, step=100.0)
category = st.sidebar.text_input("Санаты (Категория):")
description = st.sidebar.text_input("Сипаттамасы (Описание):")
trans_type = st.sidebar.selectbox("Түрі:", ["Income", "Expense"])

if st.sidebar.button("Қосу"):
    if category and description:
        qarzhy_esebi.add_transaction(amount, category, description, trans_type)
        st.sidebar.success("Сәтті қосылды!")
    else:
        st.sidebar.error("Барлық жолдарды толтырыңыз.")

balance = qarzhy_esebi.calculate_balance()
st.header(f"Қазіргі баланс: {balance} tg.")

st.subheader("Барлық транзакциялар")
transactions = qarzhy_esebi.get_all_transactions()

if transactions:
    table_data = []
    for t in transactions:
        table_data.append({
            "Уақыты": t.date,
            "Түрі": t.type,
            "Санаты": t.category,
            "Сомасы": t.amount,
            "Сипаттамасы": t.description
        })
    st.dataframe(table_data, use_container_width=True)
else:
    st.info("Әзірге транзакциялар жоқ.")