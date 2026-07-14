#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 galhkoernia
#

import pandas as pd
import numpy as np


def generate_insights(df, eda_results):
    """
    Menghasilkan insight bisnis dari hasil EDA.
    """
    insights = []
    
    insights.extend(_get_target_insights(df))
    insights.extend(_get_demographic_insights(df))
    insights.extend(_get_financial_insights(df))
    insights.extend(_get_behavioral_insights(df))
    insights.extend(_get_geographic_insights(df))
    
    return insights


def _get_target_insights(df):
    insights = []
    
    total = len(df)
    unpaid = df['Unpaid Tagging'].sum()
    unpaid_rate = (unpaid / total) * 100
    
    insights.append({
        'category': 'Profil Risiko Kredit',
        'title': 'Tingkat Gagal Bayar Nasabah',
        'description': f'Berdasarkan analisis terhadap {total} nasabah, ditemukan {unpaid} nasabah ({unpaid_rate:.1f}%) yang masuk dalam kategori gagal bayar. Angka ini menjadi indikator awal bahwa perusahaan perlu melakukan evaluasi portofolio kredit secara berkala.',
        'severity': 'Tinggi' if unpaid_rate > 10 else 'Sedang' if unpaid_rate > 5 else 'Rendah',
        'metric': unpaid_rate
    })
    
    return insights


def _get_demographic_insights(df):
    insights = []
    
    age_unpaid = df[df['Unpaid Tagging'] == 1]['Age'].mean()
    age_paid = df[df['Unpaid Tagging'] == 0]['Age'].mean()
    age_diff = age_unpaid - age_paid
    
    insights.append({
        'category': 'Profil Demografi Nasabah',
        'title': 'Pengaruh Usia terhadap Risiko Gagal Bayar',
        'description': f'Nasabah dengan status gagal bayar memiliki rata-rata usia {age_unpaid:.1f} tahun, sementara nasabah dengan status lancar memiliki rata-rata usia {age_paid:.1f} tahun. Terdapat perbedaan usia sebesar {age_diff:.1f} tahun antara kedua kelompok, yang mengindikasikan bahwa segmen usia tertentu memiliki profil risiko yang berbeda.',
        'severity': 'Tinggi' if abs(age_diff) > 5 else 'Sedang',
        'metric': age_diff
    })
    
    income_unpaid = df[df['Unpaid Tagging'] == 1]['Avg. Annual Income/Month'].mean()
    income_paid = df[df['Unpaid Tagging'] == 0]['Avg. Annual Income/Month'].mean()
    income_ratio = income_unpaid / income_paid if income_paid > 0 else 0
    
    insights.append({
        'category': 'Profil Demografi Nasabah',
        'title': 'Hubungan Tingkat Pendapatan dengan Risiko Kredit',
        'description': f'Nasabah gagal bayar memiliki rata-rata pendapatan bulanan sebesar Rp{income_unpaid:,.0f}, lebih rendah dibandingkan nasabah lancar yang mencapai Rp{income_paid:,.0f}. Kelompok nasabah dengan pendapatan lebih rendah menunjukkan risiko gagal bayar {(1-income_ratio)*100:.1f}% lebih tinggi, sehingga perlu mendapat perhatian dalam penilaian kredit.',
        'severity': 'Tinggi' if income_ratio < 0.7 else 'Sedang',
        'metric': income_ratio
    })
    
    return insights


def _get_financial_insights(df):
    insights = []
    
    balance_unpaid = df[df['Unpaid Tagging'] == 1]['Balance Q4'].mean()
    balance_paid = df[df['Unpaid Tagging'] == 0]['Balance Q4'].mean()
    balance_ratio = balance_unpaid / balance_paid if balance_paid > 0 else 0
    
    insights.append({
        'category': 'Analisis Keuangan',
        'title': 'Korelasi Saldo Mengendap dengan Risiko Gagal Bayar',
        'description': f'Nasabah gagal bayar memiliki rata-rata saldo mengendap sebesar Rp{balance_unpaid:,.0f}, jauh lebih rendah dibandingkan nasabah lancar dengan rata-rata Rp{balance_paid:,.0f}. Saldo mengendap yang rendah berkorelasi dengan risiko gagal bayar {(1-balance_ratio)*100:.1f}% lebih tinggi, yang mengindikasikan pentingnya likuiditas nasabah dalam menjaga kelancaran pembayaran.',
        'severity': 'Tinggi' if balance_ratio < 0.5 else 'Sedang',
        'metric': balance_ratio
    })
    
    return insights


def _get_behavioral_insights(df):
    insights = []
    
    product_unpaid = df[df['Unpaid Tagging'] == 1]['NumOfProducts Q4'].mean()
    product_paid = df[df['Unpaid Tagging'] == 0]['NumOfProducts Q4'].mean()
    
    insights.append({
        'category': 'Analisis Perilaku Nasabah',
        'title': 'Pola Kepemilikan Produk Perbankan',
        'description': f'Nasabah gagal bayar rata-rata memiliki {product_unpaid:.1f} produk, sementara nasabah lancar memiliki {product_paid:.1f} produk. Semakin banyak produk yang dimiliki nasabah, semakin rendah risiko gagal bayar. Hal ini menunjukkan bahwa nasabah dengan keterikatan produk yang lebih kuat cenderung lebih patuh dalam memenuhi kewajiban pembayaran.',
        'severity': 'Sedang',
        'metric': product_unpaid / product_paid if product_paid > 0 else 0
    })
    
    active_unpaid = df[df['Unpaid Tagging'] == 1]['ActiveMember Q4'].mean() * 100
    active_paid = df[df['Unpaid Tagging'] == 0]['ActiveMember Q4'].mean() * 100
    
    insights.append({
        'category': 'Analisis Perilaku Nasabah',
        'title': 'Tingkat Keaktifan Nasabah dan Risiko Gagal Bayar',
        'description': f'Hanya {active_unpaid:.1f}% nasabah gagal bayar yang masih tercatat sebagai nasabah aktif, dibandingkan {active_paid:.1f}% pada nasabah lancar. Nasabah yang tidak aktif menunjukkan risiko gagal bayar yang signifikan lebih tinggi, sehingga perusahaan perlu meningkatkan engagement untuk mencegah potensi kredit macet.',
        'severity': 'Tinggi' if (active_paid - active_unpaid) > 20 else 'Sedang',
        'metric': active_unpaid / active_paid if active_paid > 0 else 0
    })
    
    cc_unpaid = df[df['Unpaid Tagging'] == 1]['HasCrCard Q4'].mean() * 100
    cc_paid = df[df['Unpaid Tagging'] == 0]['HasCrCard Q4'].mean() * 100
    
    insights.append({
        'category': 'Analisis Perilaku Nasabah',
        'title': 'Dampak Kepemilikan Kartu Kredit terhadap Risiko Kredit',
        'description': f'Kepemilikan kartu kredit tercatat sebesar {cc_unpaid:.1f}% pada nasabah gagal bayar dan {cc_paid:.1f}% pada nasabah lancar. Nasabah pemegang kartu kredit menunjukkan profil risiko yang lebih baik, yang dapat menjadi indikator tambahan dalam proses underwriting untuk menilai kelayakan kredit nasabah.',
        'severity': 'Sedang',
        'metric': cc_unpaid / cc_paid if cc_paid > 0 else 0
    })
    
    return insights


def _get_geographic_insights(df):
    insights = []
    
    city_unpaid = df.groupby('City')['Unpaid Tagging'].mean() * 100
    highest_risk_city = city_unpaid.idxmax()
    highest_risk_rate = city_unpaid.max()
    lowest_risk_city = city_unpaid.idxmin()
    lowest_risk_rate = city_unpaid.min()
    
    insights.append({
        'category': 'Analisis Geografis',
        'title': 'Distribusi Risiko Kredit Berdasarkan Wilayah',
        'description': f'Kota {highest_risk_city} memiliki tingkat gagal bayar tertinggi sebesar {highest_risk_rate:.1f}%, sementara {lowest_risk_city} memiliki tingkat terendah sebesar {lowest_risk_rate:.1f}%. Perbedaan yang signifikan antar wilayah ini mengindikasikan bahwa faktor geografis mempengaruhi profil risiko nasabah. Perusahaan perlu mempertimbangkan pendekatan yang berbeda dalam pengelolaan risiko di setiap wilayah operasional.',
        'severity': 'Tinggi' if highest_risk_rate > 15 else 'Sedang',
        'metric': highest_risk_rate
    })
    
    return insights


def format_insights(insights):
    """
    Memformat insight untuk tampilan laporan.
    """
    output = []
    output.append("\n" + "=" * 80)
    output.append("LAPORAN INSIGHT BISNIS")
    output.append("=" * 80)
    
    categories = {}
    for insight in insights:
        cat = insight['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(insight)
    
    for category, items in categories.items():
        output.append(f"\n{category.upper()}")
        output.append("-" * 60)
        for i, insight in enumerate(items, 1):
            output.append(f"\nInsight {i}: {insight['title']}")
            output.append(f"  Tingkat Prioritas: {insight['severity']}")
            output.append(f"  {insight['description']}")
    
    output.append("\n" + "=" * 80)
    return "\n".join(output)


def save_insights(insights, filepath='report/insights.txt'):
    """
    Menyimpan insight ke file teks.
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(format_insights(insights))
    print(f"Insight disimpan di {filepath}")