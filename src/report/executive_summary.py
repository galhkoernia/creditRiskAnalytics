#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 galhkoernia
#

import pandas as pd
import json
from datetime import datetime


def generate_executive_summary(df, insights, recommendations, metrics):
    """
    Menghasilkan executive summary dalam format markdown bahasa Indonesia.
    """
    sections = []
    
    sections.append(_get_header())
    sections.append(_get_executive_overview(metrics))
    sections.append(_get_key_findings(insights))
    sections.append(_get_recommendations_summary(recommendations))
    sections.append(_get_risk_analysis(df))
    sections.append(_get_next_steps(recommendations))
    sections.append(_get_footer())
    
    return "\n\n".join(sections)


def _get_header():
    return f"""# Ringkasan Eksekutif
## Analisis Risiko Kredit FinanKu
### Tanggal Laporan: {datetime.now().strftime('%d %B %Y')}

---"""


def _get_executive_overview(metrics):
    return f"""## 1. Gambaran Umum Portofolio

### Ringkasan Portofolio
| Metrik | Nilai |
|--------|-------|
| Total Nasabah | {metrics['total_customers']:,} |
| Tingkat Gagal Bayar | {metrics['default_rate']:.1f}% |
| Rata-rata Saldo Mengendap | Rp{metrics['avg_balance']:,.0f} |
| Rata-rata Produk per Nasabah | {metrics['avg_products']:.1f} |
| Rata-rata Usia Nasabah | {metrics['avg_age']:.1f} tahun |
| Rata-rata Pendapatan Bulanan | Rp{metrics['avg_income']:,.0f} |
| Tingkat Nasabah Aktif | {metrics['active_rate']:.1f}% |
| Tingkat Kepemilikan Kartu Kredit | {metrics['credit_card_rate']:.1f}% |

### Temuan Utama
- {metrics['default_rate']:.1f}% nasabah teridentifikasi berisiko gagal bayar
- {metrics['high_risk_count']} nasabah masuk dalam kategori risiko sangat tinggi
- {'Jakarta' if 'Jakarta' in metrics.get('default_by_city', {}) else 'Wilayah tertentu'} menunjukkan tingkat gagal bayar tertinggi

---"""


def _get_key_findings(insights):
    output = ["## 2. Temuan Utama"]
    output.append("")
    
    high_severity = [i for i in insights if i['severity'] == 'Tinggi']
    medium_severity = [i for i in insights if i['severity'] == 'Sedang']
    
    if high_severity:
        output.append("### Temuan Prioritas Tinggi")
        for i, insight in enumerate(high_severity[:4], 1):
            output.append(f"{i}. **{insight['title']}**")
            output.append(f"   {insight['description']}")
            output.append("")
    
    if medium_severity:
        output.append("### Temuan Tambahan")
        for i, insight in enumerate(medium_severity[:3], 1):
            output.append(f"{i}. **{insight['title']}**")
            output.append(f"   {insight['description']}")
            output.append("")
    
    output.append("---")
    return "\n".join(output)


def _get_recommendations_summary(recommendations):
    output = ["## 3. Rekomendasi Strategis"]
    output.append("")
    
    high_priority = [r for r in recommendations if r['priority'] == 'Tinggi']
    medium_priority = [r for r in recommendations if r['priority'] == 'Sedang']
    
    if high_priority:
        output.append("### Tindakan Segera (Prioritas Tinggi)")
        for i, rec in enumerate(high_priority[:4], 1):
            output.append(f"{i}. **{rec['title']}**")
            output.append(f"   - Dampak yang Diharapkan: {rec['expected_impact']}")
            output.append(f"   - Timeline: {rec['timeline']}")
            output.append("")
    
    if medium_priority:
        output.append("### Tindakan Jangka Pendek hingga Menengah")
        for i, rec in enumerate(medium_priority[:3], 1):
            output.append(f"{i}. **{rec['title']}**")
            output.append(f"   - Dampak yang Diharapkan: {rec['expected_impact']}")
            output.append(f"   - Timeline: {rec['timeline']}")
            output.append("")
    
    output.append("---")
    return "\n".join(output)


def _get_risk_analysis(df):
    output = ["## 4. Analisis Risiko"]
    output.append("")
    
    if 'Risk_Category' in df.columns:
        output.append("### Distribusi Tingkat Risiko")
        risk_counts = df['Risk_Category'].value_counts()
        for category, count in risk_counts.items():
            percentage = (count / len(df)) * 100
            output.append(f"- {category}: {count:,} nasabah ({percentage:.1f}%)")
        output.append("")
    
    if 'City' in df.columns:
        output.append("### Distribusi Risiko Berdasarkan Wilayah")
        city_risk = df.groupby('City')['Unpaid Tagging'].mean().sort_values(ascending=False)
        for city, risk_rate in city_risk.items():
            output.append(f"- {city}: {risk_rate*100:.1f}% tingkat gagal bayar")
        output.append("")
    
    if 'Income_Segment' in df.columns:
        output.append("### Risiko Berdasarkan Segmen Pendapatan")
        income_risk = df.groupby('Income_Segment')['Unpaid Tagging'].mean().sort_values(ascending=False)
        for segment, risk_rate in income_risk.items():
            output.append(f"- {segment}: {risk_rate*100:.1f}% tingkat gagal bayar")
        output.append("")
    
    if 'Age_Group' in df.columns:
        output.append("### Risiko Berdasarkan Kelompok Usia")
        age_risk = df.groupby('Age_Group')['Unpaid Tagging'].mean().sort_values(ascending=False)
        for age_group, risk_rate in age_risk.items():
            output.append(f"- {age_group}: {risk_rate*100:.1f}% tingkat gagal bayar")
        output.append("")
    
    output.append("---")
    return "\n".join(output)


def _get_next_steps(recommendations):
    output = ["## 5. Langkah Selanjutnya"]
    output.append("")
    
    output.append("### Roadmap Implementasi")
    output.append("")
    output.append("| Timeline | Tindakan | Penanggung Jawab | Prioritas |")
    output.append("|----------|----------|------------------|-----------|")
    
    for rec in recommendations[:6]:
        output.append(f"| {rec['timeline']} | {rec['title']} | TBD | {rec['priority']} |")
    
    output.append("")
    output.append("### Faktor Kunci Keberhasilan")
    output.append("")
    output.append("1. **Dukungan Eksekutif**: Memastikan komitmen pimpinan untuk mengimplementasikan rekomendasi")
    output.append("2. **Infrastruktur Data**: Memperkuat kapabilitas pengumpulan dan integrasi data")
    output.append("3. **Kapabilitas Tim**: Mengembangkan keahlian di bidang analitik dan manajemen risiko")
    output.append("4. **Investasi Teknologi**: Menerapkan model prediktif dan sistem pemantauan")
    output.append("5. **Manajemen Perubahan**: Mengembangkan program komunikasi dan pelatihan")
    output.append("")
    output.append("---")
    return "\n".join(output)


def _get_footer():
    return f"""## 6. Lampiran

### Metodologi Analisis
- **Periode Data**: Data kuartalan Q1 hingga Q4
- **Jumlah Sampel**: 7.561 nasabah
- **Metode Analisis**: Analisis univariat, bivariat, dan multivariat
- **Skoring Risiko**: Skor komposit berdasarkan indikator keuangan dan perilaku

### Informasi Kontak
**Disusun Oleh:** Galuh Kurnia Pratama
**Email:** galuhkoernia@gmail.com
**LinkedIn:** https://www.linkedin.com/in/galuh-kurnia-pratama-a25b9b325/

---

*Laporan ini bersifat rahasia dan hanya untuk penggunaan internal.*

---"""


def save_executive_summary(df, insights, recommendations, metrics, 
                          filepath='report/executive_summary.md'):
    """
    Menyimpan executive summary ke file markdown.
    """
    summary = generate_executive_summary(df, insights, recommendations, metrics)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(summary)
    
    print(f"Ringkasan eksekutif disimpan di {filepath}")
    return summary