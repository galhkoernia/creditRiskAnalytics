#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 galhkoernia
#

import pandas as pd
import numpy as np


def generate_recommendations(insights):
    """
    Menghasilkan rekomendasi bisnis yang dapat ditindaklanjuti dari insight.
    """
    recommendations = []
    
    recommendations.extend(_get_credit_risk_recommendations(insights))
    recommendations.extend(_get_customer_segmentation_recommendations(insights))
    recommendations.extend(_get_product_strategy_recommendations(insights))
    recommendations.extend(_get_engagement_recommendations(insights))
    recommendations.extend(_get_regional_strategy_recommendations(insights))
    
    return recommendations


def _get_credit_risk_recommendations(insights):
    recommendations = []
    
    for insight in insights:
        if insight['category'] == 'Profil Risiko Kredit' and insight['severity'] == 'Tinggi':
            recommendations.append({
                'category': 'Manajemen Risiko Kredit',
                'priority': 'Tinggi',
                'title': 'Penguatan Proses Penilaian Kredit',
                'description': 'Perusahaan perlu melakukan peninjauan dan pembaruan kriteria penilaian kredit untuk mengidentifikasi nasabah berisiko tinggi sejak awal. Penerapan skoring kredit yang lebih ketat akan membantu mengurangi potensi kerugian akibat gagal bayar.',
                'action_items': [
                    'Meninjau dan memperbarui kriteria penilaian kredit secara berkala',
                    'Menerapkan verifikasi tambahan untuk calon nasabah berisiko tinggi',
                    'Meningkatkan frekuensi pemantauan nasabah eksisting yang masuk kategori berisiko'
                ],
                'expected_impact': 'Menurunkan tingkat gagal bayar sebesar 15-20% dalam 6 bulan',
                'timeline': 'Jangka Pendek (0-3 bulan)'
            })
    
    recommendations.append({
        'category': 'Manajemen Risiko Kredit',
        'priority': 'Tinggi',
        'title': 'Pengembangan Sistem Peringatan Dini',
        'description': 'Membangun model prediktif untuk mengidentifikasi nasabah yang berpotensi gagal bayar sebelum terjadi. Sistem ini akan membantu perusahaan mengambil tindakan preventif secara tepat waktu.',
        'action_items': [
            'Membangun model machine learning menggunakan data historis nasabah',
            'Mengatur notifikasi otomatis untuk indikator risiko tertentu',
            'Menetapkan protokol intervensi untuk setiap tingkat risiko yang teridentifikasi'
        ],
        'expected_impact': 'Mengidentifikasi 80% potensi gagal bayar 3 bulan sebelum terjadi',
        'timeline': 'Jangka Menengah (3-6 bulan)'
    })
    
    return recommendations


def _get_customer_segmentation_recommendations(insights):
    recommendations = []
    
    age_insight = None
    income_insight = None
    
    for insight in insights:
        if insight['category'] == 'Profil Demografi Nasabah' and 'Usia' in insight['title']:
            age_insight = insight
        if insight['category'] == 'Profil Demografi Nasabah' and 'Pendapatan' in insight['title']:
            income_insight = insight
    
    if age_insight and age_insight['severity'] == 'Tinggi':
        recommendations.append({
            'category': 'Segmentasi Nasabah',
            'priority': 'Tinggi',
            'title': 'Implementasi Segmentasi Risiko Berdasarkan Usia',
            'description': 'Mengembangkan strategi yang disesuaikan untuk setiap kelompok usia berdasarkan profil risiko masing-masing. Pendekatan yang personal akan meningkatkan efektivitas manajemen risiko.',
            'action_items': [
                'Membagi nasabah ke dalam kelompok usia (18-25, 26-35, 36-45, 46-55, 56+)',
                'Merancang produk dan layanan yang sesuai untuk setiap segmen usia',
                'Menyesuaikan strategi komunikasi dan pemasaran per kelompok usia'
            ],
            'expected_impact': 'Meningkatkan kinerja portofolio yang disesuaikan risiko sebesar 10%',
            'timeline': 'Jangka Menengah (3-6 bulan)'
        })
    
    if income_insight and income_insight['severity'] == 'Tinggi':
        recommendations.append({
            'category': 'Segmentasi Nasabah',
            'priority': 'Tinggi',
            'title': 'Pengembangan Produk Berdasarkan Tingkat Pendapatan',
            'description': 'Menciptakan paket produk yang disesuaikan dengan tingkat pendapatan nasabah untuk meningkatkan keterjangkauan dan menurunkan risiko gagal bayar.',
            'action_items': [
                'Merancang produk dengan tier yang disesuaikan dengan tingkat pendapatan',
                'Menyesuaikan plafon dan jangka waktu kredit berdasarkan profil pendapatan',
                'Menyelenggarakan program literasi keuangan untuk segmen berpendapatan rendah'
            ],
            'expected_impact': 'Menurunkan risiko gagal bayar pada segmen berpendapatan rendah sebesar 12-15%',
            'timeline': 'Jangka Pendek (0-3 bulan)'
        })
    
    return recommendations


def _get_product_strategy_recommendations(insights):
    recommendations = []
    
    recommendations.append({
        'category': 'Strategi Produk',
        'priority': 'Sedang',
        'title': 'Peningkatan Cross-Selling Produk Perbankan',
        'description': 'Mendorong nasabah untuk mengadopsi lebih banyak produk guna meningkatkan engagement dan menurunkan risiko gagal bayar. Nasabah dengan keterikatan produk yang kuat cenderung lebih patuh dalam pembayaran.',
        'action_items': [
            'Membuat bundling produk dengan insentif menarik',
            'Mengembangkan kampanye cross-selling yang tertarget',
            'Memberikan program loyalitas untuk nasabah multi-produk'
        ],
        'expected_impact': 'Meningkatkan rata-rata produk per nasabah sebesar 25%',
        'timeline': 'Jangka Menengah (3-6 bulan)'
    })
    
    recommendations.append({
        'category': 'Strategi Produk',
        'priority': 'Sedang',
        'title': 'Pengoptimalan Produk Kartu Kredit',
        'description': 'Memperluas portofolio kartu kredit untuk menarik lebih banyak nasabah dan meningkatkan profil kredit nasabah. Kartu kredit terbukti menjadi indikator kelayakan kredit yang baik.',
        'action_items': [
            'Merancang produk kartu kredit untuk berbagai segmen nasabah',
            'Menghadirkan program rewards untuk nasabah dengan pembayaran lancar',
            'Menyediakan edukasi kredit bagi pengguna kartu kredit'
        ],
        'expected_impact': 'Meningkatkan adopsi kartu kredit sebesar 20%',
        'timeline': 'Jangka Menengah (3-6 bulan)'
    })
    
    return recommendations


def _get_engagement_recommendations(insights):
    recommendations = []
    
    recommendations.append({
        'category': 'Pengelolaan Engagement Nasabah',
        'priority': 'Tinggi',
        'title': 'Program Aktivasi Nasabah Tidak Aktif',
        'description': 'Mengimplementasikan program engagement untuk meningkatkan aktivitas nasabah dan menurunkan risiko gagal bayar. Nasabah aktif menunjukkan profil risiko yang lebih baik.',
        'action_items': [
            'Merancang kampanye aktivasi untuk nasabah yang sudah tidak aktif',
            'Mengembangkan sistem skor engagement nasabah',
            'Menerapkan strategi komunikasi yang personal dan relevan'
        ],
        'expected_impact': 'Meningkatkan tingkat nasabah aktif sebesar 20%',
        'timeline': 'Jangka Pendek (0-3 bulan)'
    })
    
    return recommendations


def _get_regional_strategy_recommendations(insights):
    recommendations = []
    
    regional_insight = None
    
    for insight in insights:
        if insight['category'] == 'Analisis Geografis':
            regional_insight = insight
    
    if regional_insight and regional_insight['severity'] == 'Tinggi':
        recommendations.append({
            'category': 'Strategi Regional',
            'priority': 'Tinggi',
            'title': 'Optimalisasi Manajemen Risiko Berdasarkan Wilayah',
            'description': 'Mengembangkan strategi yang spesifik untuk setiap wilayah guna mengatasi variasi risiko geografis. Pendekatan regional akan meningkatkan efektivitas pengelolaan risiko kredit.',
            'action_items': [
                'Melakukan analisis mendalam di wilayah dengan risiko tinggi',
                'Menyesuaikan kebijakan kredit untuk setiap wilayah operasional',
                'Mengembangkan kemitraan lokal untuk penagihan dan pemulihan'
            ],
            'expected_impact': 'Menurunkan tingkat gagal bayar di wilayah berisiko tinggi sebesar 18%',
            'timeline': 'Jangka Menengah (3-6 bulan)'
        })
    
    return recommendations


def format_recommendations(recommendations):
    """
    Memformat rekomendasi untuk tampilan laporan.
    """
    output = []
    output.append("\n" + "=" * 80)
    output.append("REKOMENDASI BISNIS")
    output.append("=" * 80)
    
    high_priority = [r for r in recommendations if r['priority'] == 'Tinggi']
    medium_priority = [r for r in recommendations if r['priority'] == 'Sedang']
    
    all_priority = high_priority + medium_priority
    
    for i, rec in enumerate(all_priority, 1):
        output.append(f"\nRekomendasi {i}: {rec['title']}")
        output.append(f"  Prioritas: {rec['priority']}")
        output.append(f"  Kategori: {rec['category']}")
        output.append(f"  Timeline: {rec['timeline']}")
        output.append(f"  Dampak yang Diharapkan: {rec['expected_impact']}")
        output.append(f"  Deskripsi: {rec['description']}")
        output.append("  Langkah Implementasi:")
        for item in rec['action_items']:
            output.append(f"    - {item}")
    
    output.append("\n" + "=" * 80)
    return "\n".join(output)


def save_recommendations(recommendations, filepath='report/recommendations.txt'):
    """
    Menyimpan rekomendasi ke file teks.
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(format_recommendations(recommendations))
    print(f"Rekomendasi disimpan di {filepath}")