#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 galhkoernia
#

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


def create_dashboard(df):
    """
    Create complete dashboard with all visualizations.
    """
    
    fig = plt.figure(figsize=(16, 12))
    fig.suptitle('Credit Risk Analytics Dashboard for FinanKu', fontsize=18, fontweight='bold', y=0.98)
    
    gs = fig.add_gridspec(4, 4, hspace=0.4, wspace=0.3)
    
    # Target Distribution
    ax1 = fig.add_subplot(gs[0, 0])
    target_counts = df['Unpaid Tagging'].value_counts()
    colors = ['#2ecc71', '#e74c3c']
    bars = ax1.bar(['Lancar', 'Gagal Bayar'], target_counts.values, color=colors, edgecolor='black')
    ax1.set_title('Distribusi Target', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Jumlah Nasabah')
    for bar, val in zip(bars, target_counts.values):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 150, 
                f'{val}\n({val/len(df)*100:.1f}%)', 
                ha='center', va='bottom', fontsize=9)
    
    # Age Distribution
    ax2 = fig.add_subplot(gs[0, 1:3])
    ax2.hist(df['Age'], bins=20, color='#3498db', edgecolor='black', alpha=0.7)
    ax2.axvline(df['Age'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df["Age"].mean():.1f}')
    ax2.axvline(df['Age'].median(), color='green', linestyle='--', linewidth=2, label=f'Median: {df["Age"].median():.1f}')
    ax2.set_title('Distribusi Usia Nasabah', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Usia (Tahun)')
    ax2.set_ylabel('Frekuensi')
    ax2.legend()
    
    # Income Distribution
    ax3 = fig.add_subplot(gs[0, 3])
    ax3.boxplot(df['Avg. Annual Income/Month'], vert=True, patch_artist=True,
                boxprops=dict(facecolor='#3498db', alpha=0.7))
    ax3.set_title('Distribusi Pendapatan', fontsize=12, fontweight='bold')
    ax3.set_ylabel('Pendapatan (Rp)')
    ax3.set_xticklabels(['Income'])
    
    # Balance Q4 by Target (Row 2, Col 0-1)
    ax4 = fig.add_subplot(gs[1, 0:2])
    data_balance = [df[df['Unpaid Tagging']==0]['Balance Q4'], 
                    df[df['Unpaid Tagging']==1]['Balance Q4']]
    bp = ax4.boxplot(data_balance, labels=['Lancar', 'Gagal Bayar'], 
                     patch_artist=True, widths=0.5)
    colors_box = ['#2ecc71', '#e74c3c']
    for patch, color in zip(bp['boxes'], colors_box):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    ax4.set_title('Saldo Q4 vs Status Bayar', fontsize=12, fontweight='bold')
    ax4.set_ylabel('Saldo Q4 (Rp)')
    ax4.grid(True, alpha=0.3)
    
    # Active Member Q4 by Target
    ax5 = fig.add_subplot(gs[1, 2:4])
    data_active = [df[df['Unpaid Tagging']==0]['ActiveMember Q4'].mean() * 100,
                   df[df['Unpaid Tagging']==1]['ActiveMember Q4'].mean() * 100]
    bars_active = ax5.bar(['Lancar', 'Gagal Bayar'], data_active, color=colors_box, edgecolor='black')
    ax5.set_title('Tingkat Keaktifan Q4 vs Status Bayar', fontsize=12, fontweight='bold')
    ax5.set_ylabel('Persentase Aktif (%)')
    for bar, val in zip(bars_active, data_active):
        ax5.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
                f'{val:.1f}%', ha='center', va='bottom', fontsize=9)
    ax5.grid(True, alpha=0.3)
    
    # Products by Target
    ax6 = fig.add_subplot(gs[2, 0:2])
    product_data = []
    for target in [0, 1]:
        q1 = df[df['Unpaid Tagging']==target]['NumOfProducts Q1'].mean()
        q2 = df[df['Unpaid Tagging']==target]['NumOfProducts Q2'].mean()
        q3 = df[df['Unpaid Tagging']==target]['NumOfProducts Q3'].mean()
        q4 = df[df['Unpaid Tagging']==target]['NumOfProducts Q4'].mean()
        product_data.append([q1, q2, q3, q4])
    
    x = np.arange(4)
    width = 0.35
    bars1 = ax6.bar(x - width/2, product_data[0], width, label='Lancar', color='#2ecc71', alpha=0.7)
    bars2 = ax6.bar(x + width/2, product_data[1], width, label='Gagal Bayar', color='#e74c3c', alpha=0.7)
    ax6.set_title('Rata-rata Produk per Kuartal', fontsize=12, fontweight='bold')
    ax6.set_xlabel('Kuartal')
    ax6.set_ylabel('Rata-rata Jumlah Produk')
    ax6.set_xticks(x)
    ax6.set_xticklabels(['Q1', 'Q2', 'Q3', 'Q4'])
    ax6.legend()
    ax6.grid(True, alpha=0.3)
    
    # Credit Card Ownership
    ax7 = fig.add_subplot(gs[2, 2:4])
    cc_data = []
    for target in [0, 1]:
        q1 = df[df['Unpaid Tagging']==target]['HasCrCard Q1'].mean() * 100
        q2 = df[df['Unpaid Tagging']==target]['HasCrCard Q2'].mean() * 100
        q3 = df[df['Unpaid Tagging']==target]['HasCrCard Q3'].mean() * 100
        q4 = df[df['Unpaid Tagging']==target]['HasCrCard Q4'].mean() * 100
        cc_data.append([q1, q2, q3, q4])
    
    bars3 = ax7.bar(x - width/2, cc_data[0], width, label='Lancar', color='#2ecc71', alpha=0.7)
    bars4 = ax7.bar(x + width/2, cc_data[1], width, label='Gagal Bayar', color='#e74c3c', alpha=0.7)
    ax7.set_title('Kepemilikan Kartu Kredit (%)', fontsize=12, fontweight='bold')
    ax7.set_xlabel('Kuartal')
    ax7.set_ylabel('Persentase (%)')
    ax7.set_xticks(x)
    ax7.set_xticklabels(['Q1', 'Q2', 'Q3', 'Q4'])
    ax7.legend()
    ax7.grid(True, alpha=0.3)
    
    # City Distribution
    ax8 = fig.add_subplot(gs[3, 0])
    city_counts = df['City'].value_counts()
    colors_city = ['#3498db', '#2ecc71', '#e74c3c', '#f39c12']
    wedges, texts, autotexts = ax8.pie(city_counts.values, labels=city_counts.index, 
                                        autopct='%1.1f%%', colors=colors_city[:len(city_counts)],
                                        startangle=90)
    ax8.set_title('Distribusi Nasabah per Kota', fontsize=12, fontweight='bold')
    
    # Correlation Heatmap
    ax9 = fig.add_subplot(gs[3, 1:4])
    numeric_cols = ['Age', 'Avg. Annual Income/Month', 'Balance Q4', 'NumOfProducts Q4']
    corr = df[numeric_cols].corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    sns.heatmap(corr, mask=mask, annot=True, fmt='.2f', cmap='RdBu_r',
                center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8},
                ax=ax9)
    ax9.set_title('Korelasi Antar Variabel Numerik', fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    plt.subplots_adjust(top=0.94)
    
    return fig


def save_dashboard(df, filename='dashboard.png'):
    """
    Save dashboard to file.
    """
    fig = create_dashboard(df)
    fig.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Dashboard saved as {filename}")