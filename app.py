import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import time
import random

st.set_page_config(page_title="National SOC - IRAQ", page_icon="🛡️", layout="wide")

st.title("🛡️ National SOC - IRAQ")
st.markdown("**المركز الوطني للأمن السيبراني | وزارة الاتصالات - العراق**")
st.markdown("---")

# القائمة الجانبية
st.sidebar.title("⚙️ لوحة التحكم")
page = st.sidebar.selectbox("اختر الصفحة", ["الرئيسية", "التهديدات", "الشبكة", "التقارير"])

if page == "الرئيسية":
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🟢 الأنظمة المراقبة", "156", "+12")
    col2.metric("🔴 تهديدات اليوم", "7", "-2")
    col3.metric("🟡 تحذيرات", "23", "+5")
    col4.metric("✅ نسبة الحماية", "98.2%", "+0.4%")

    st.markdown("### 📊 حالة الشبكة الآن")
    if st.button("🔍 افحص الشبكة الآن", type="primary"):
        with st.spinner("جاري فحص الشبكة..."):
            time.sleep(2)
        
        # بيانات وهمية للفحص
        normal = np.random.normal(loc=[20, 5000, 2], scale=[5, 1000, 1], size=(200, 3))
        model = IsolationForest(contamination=0.1, random_state=42)
        model.fit(normal)

        tests = [
            ("192.168.1.10", 2, 5200, 22, "وزارة النفط"),
            ("192.168.1.11", 1, 4800, 18, "وزارة الصحة"),
            ("45.12.88.9", 3, 8000, 1500, "وزارة الداخلية"),
            ("103.45.22.7", 2, 5000000, 25, "وزارة الدفاع"),
            ("91.33.77.5", 80, 5000, 20, "وزارة المالية"),
        ]

        st.markdown("### 📋 نتائج الفحص:")
        for ip, a, b, c, name in tests:
            pred = model.predict([[c, b, a]])[0]
            if pred == -1:
                st.error(f"🚨 خطر! {name} - {ip} | نشاط مشبوه تم اكتشافه")
            else:
                st.success(f"✅ آمن: {name} - {ip} | لا يوجد تهديد")

        st.balloons
